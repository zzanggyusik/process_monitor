from pyevsim import BehaviorModelExecutor, SystemSimulator, Infinite
from simulation_process_monitoring_model import MonitoringModel
from config import *

class SimMonitor():
    def __init__(self):        
        # initialize simulation engine
        # System Simulator Initialization
        self.ss = SystemSimulator()
        #-----------------------------------------------------------------------
        self.ss.register_engine(ENGINE_NAME, SIMULATION_TIME, SIMULATION_TIME_UNIT)
        # self.ss.register_engine("monitoring_engine", "REAL_TIME / VIRTUAL_TIME", 1)
        
        self.monitoring_engine = self.ss.get_engine(ENGINE_NAME)
        
        self.monitoring_engine.insert_input_port("monitoring_start")
        self.monitoring_engine.insert_input_port("MONIT")
        self.monitoring_engine.insert_input_port("monitoring_finish")
        
        monitoring_model = MonitoringModel(0, Infinite, MONITORING_MODEL_NAME, ENGINE_NAME, self.monitoring_engine)
        
        self.monitoring_engine.register_entity(monitoring_model)
        
        self.monitoring_engine.coupling_relation(None, "monitoring_start", monitoring_model, "monitoring_start")
        #self.monitoring_engine.coupling_relation(monitoring_model, "IDLE", monitoring_model, "monitor_finish")

    def get_engine(self):
        return self.monitoring_engine
        
    def start_engine(self) -> None:
        # if model == "predict":
        self.monitoring_engine.insert_external_event("monitoring_start", "monitoring_start")
        # self.ai_engine.insert_external_event("predict", "predict")
        self.monitoring_engine.simulate()
        