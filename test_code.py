import time
import sys

def main(option):
    cnt = 0
    
    if option == 's':
        time.sleep(2)
        while True:
            cnt += 1   
            if cnt == 1000: break
    
    elif option == 'f':
        while True:
            time.sleep(1)
            cnt += 1
            if cnt == 1000 : break
            
        
if __name__ == "__main__":
    #option = input("Success mode : S\nFail mode : F\n").lower()
    option = sys.argv[1]
    main(option)