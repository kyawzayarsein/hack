import core  
import os
import sys

if __name__ == "__main__":
    try:
        
        did = core.get_device_id()
        
        authorized = False
        expiry = None
        LICENSE_FILE = os.path.join(os.path.expanduser("~"), ".turbo_license")

        if os.path.exists(LICENSE_FILE):
            with open(LICENSE_FILE, "r") as f:
                saved_key = f.read().strip()
            is_valid, msg, expiry = core.validate_key(did, saved_key)
            if is_valid:
                authorized = True

        core.print_banner(did, expiry)

        if not authorized:
            print("\033[96m[?] INPUT REQUIRED: ENTER ACTIVATION KEY TO START\033[0m")
            key = input("\033[92mroot@turbo:~# \033[0m").strip().upper()
            is_valid, msg, expiry = core.validate_key(did, key)
            if is_valid:
                with open(LICENSE_FILE, "w") as f: f.write(key)
                core.print_banner(did, expiry)
                print("\033[92m[+] ACTIVATION SUCCESSFUL!\033[0m\n")
                authorized = True
            else:
                print(f"\033[91m[X] FATAL ERROR: {msg}\033[0m")
                sys.exit()

        if authorized:
            core.start_process()

    except KeyboardInterrupt:
        print("\n\033[91m[!] STOPPED BY USER.\033[0m")
    except Exception as e:
        print(f"\n\033[91m[!] ERROR: {e}\033[0m")
        
