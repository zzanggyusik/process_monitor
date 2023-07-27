import subprocess
from config import *

script = TARGET_PROCESS
try:
    subprocess.check_output(['pgrep', '-f' , script])
    
    state = 'Is Running'
    
except:
    
    state = 'Is Not Running'
    
print(f'{script} {state}')