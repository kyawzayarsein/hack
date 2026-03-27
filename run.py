import sys

try:
    
    import core 
except ImportError:
    print("\033[91m\n[!] Error: core.so file is missing or incompatible!\033[0m")
    sys.exit()

if __name__ == "__main__":
    try:
        
        core.start_process()
    except KeyboardInterrupt:
        print("\033[91m\n\n[!] Program Terminated by User.\033[0m")
        sys.exit()
