import time
import sys

def main(option):
    cnt = 0
    
    if option == 's':
        while True:
            cnt += 1   
            if cnt == 1000: 
                time.sleep(2)
                break
    
    elif option == 'f':
        while True:
            cnt += 1
            if cnt == 1000 : 
                time.sleep(100)
                break
            
        
if __name__ == "__main__":
    #option = input("Success mode : S\nFail mode : F\n").lower()
    option = sys.argv[1]
    main(option)