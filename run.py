
import core

if __name__ == "__main__":
    try:
        # 
        if core.check_license():
            # 
            core.start_process()
            
    except KeyboardInterrupt:
        # 
        print(f"\n\033[91m[!] PROCESS TERMINATED BY USER.\033[0m")
