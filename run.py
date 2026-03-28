# core.so ဖိုင်ကို Import လုပ်ခြင်း
import core

if __name__ == "__main__":
    try:
        # core.so ထဲက check_license() ကို အရင်ခေါ်စစ်ပါမယ်
        if core.check_license():
            # License အောင်မြင်မှသာ start_process() ကို ဆက်ခေါ်ပါမယ်
            core.start_process()
            
    except KeyboardInterrupt:
        # user က Ctrl+C နှိပ်ပြီး ပိတ်လိုက်ရင် ပြမယ့်စာ
        print(f"\n\033[91m[!] PROCESS TERMINATED BY USER.\033[0m")
