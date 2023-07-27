from simulation_monitoring_manager import SimMonitor
import logging
import test_code
import os
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

def main() -> None:
    SimMonitor().start_engine()

if __name__ == '__main__':
    #option = input("Success mode : S\nFail mode : F\n").lower()
    main()