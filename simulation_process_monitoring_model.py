from pyevsim import BehaviorModelExecutor, Infinite
import sys, os
import subprocess
from config import *

class MonitoringModel(BehaviorModelExecutor):
    def __init__(self, instance_time, destruct_time, name, engine_name, engine):
        BehaviorModelExecutor.__init__(self, instance_time, destruct_time, name, engine_name)
        
        self.monitoring_engine = engine
        self.time_count = 0
        self.target_process = TARGET_PROCESS
        # Define State
        self.init_state("IDLE")
        self.insert_state('MONIT', 1)
        self.insert_state("IDLE", Infinite)
        
        # Define Port
        self.insert_input_port("monitoring_start")
        
        self.insert_input_port("monitoring_finish")
        
    def ext_trans(self, port, msg):
        if port == "monitoring_start":
            print('Wating For simulation start')
            while True:
                try : 
                    subprocess.check_output(['pgrep', '-f' , self.target_process])
                    print('Simulation Start')
                    self._cur_state = 'MONIT'
                    break
                    
                except : 
                    pass
            
        elif port == "monitoring_finish":
            self._cur_state = "IDLE"
        
    def output(self):
        if self._cur_state == "MONIT":
            
            try : 
                subprocess.check_output(['pgrep', '-f' , self.target_process])
                state = 'Is Running'
                self.time_count += 1
                
            except : 
                state = 'Is Not Running'
                self._cur_state = "IDLE"

            print(f'{self.target_process} {state}\nCurrent Time count : {self.time_count}')
            
            if self.time_count == TIMEOUT:
                print(f'Timeout!!!')
                self.process_kill(self.target_process)
                self._cur_state = "IDLE"
        
    def process_kill(self, process):
        try:
            subprocess.run('pkill', '-f', process)
            print(f'{process} is Deleted')
            
        except:
            print("Simulation is Not Running")
                
    def int_trans(self):
        if self._cur_state == "MONIT":
            self._cur_state = "MONIT"
            
        elif self._cur_state == "IDLE":
            self._cur_state = "IDLE"