import os
import time

# রঙ পরিবর্তনের জন্য
RED = '\033[91m'
GREEN = '\033[92m'
BLUE = '\033[94m'
YELLOW = '\033[93m'
RESET = '\033[0m'

# সুন্দর ASCII লোগো
logo = f"""{RED}
████████╗ ██████╗  ██████╗ ██╗     ███████╗
╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝
   ██║   ██║   ██║██║   ██║██║     █████╗  
   ██║   ██║   ██║██║   ██║██║     ██╔══╝  
   ██║   ╚██████╔╝╚██████╔╝███████╗███████╗
   ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝
{RESET}
"""

# ফাইল লুকানোর ফাংশন
def hide_file_in_image(image_path, file_to_hide, output_image):
    os.system(f"cat {image_path} {file_to_hide} > {output_image}")  # ছবির মধ্যে ব্যাচ ফাইল যোগ করা
    
    print(f"{GREEN}[+] ফাইল সফলভাবে লুকানো হয়েছে! নতুন ফাইল: {output_image}{RESET}")

# ইন্টারফেস দেখানোর ফাংশন
def show_interface():
    os.system("clear")  # স্ক্রিন পরিষ্কার
    print(logo)
    print(f"{GREEN}🔹 Welcome to My Custom Termux Tool! 🔹{RESET}")
    print(f"{BLUE}🔹 Created by: Your Name 🔹{RESET}")
    print(f"{YELLOW}🔹 Loading... 🔹{RESET}")
    time.sleep(2)
    os.system("clear")
    print(logo)
    print(f"{GREEN}📌 Select an Option:{RESET}")
    print(f"{BLUE}[1] Hide File in Image{RESET}")
    print(f"{BLUE}[2] About Tool{RESET}")
    print(f"{BLUE}[3] Exit{RESET}")

    choice = input(f"{YELLOW}Enter your choice: {RESET}")
    if choice == "1":
        image = input(f"{YELLOW}📂 Image file name (e.g. photo.png): {RESET}")
        file_to_hide = input(f"{YELLOW}📂 File to hide (e.g. file.bat): {RESET}")
        output_image = input(f"{YELLOW}📂 Output image name (e.g. final_photo.png): {RESET}")
        
        hide_file_in_image(image, file_to_hide, output_image)

    elif choice == "2":
        print(f"{BLUE}🔹 This is a Termux Tool for hiding files inside images.{RESET}")
    elif choice == "3":
        print(f"{RED}❌ Exiting...{RESET}")
        exit()
    else:
        print(f"{RED}❌ Invalid Choice!{RESET}")

# প্রোগ্রাম চালানো
show_interface()
