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
    os.system(f"zip -r hidden.zip {file_to_hide}")  # zip ফাইল তৈরি
    os.system(f"cat {image_path} hidden.zip > {output_image}")  # ছবি + zip ফাইল একত্রিত
    os.system("rm -rf hidden.zip")  # অস্থায়ী zip ফাইল মুছে ফেলুন

    print(f"{GREEN}[+] ফাইল সফলভাবে লুকানো হয়েছে! নতুন ফাইল: {output_image}{RESET}")

# Windows-এ .bat ফাইল স্বয়ংক্রিয় চালানোর জন্য ব্যাচ স্ক্রিপ্ট তৈরি
def create_windows_bat_launcher(output_image, bat_filename):
    bat_script = f"""
    @echo off
    start {bat_filename}
    exit
    """
    with open("open.bat", "w") as f:
        f.write(bat_script)

    os.system("zip -r hidden.zip open.bat")  # নতুন ব্যাচ ফাইল জিপ
    os.system(f"cat {output_image} hidden.zip > final_{output_image}")  # একত্রিত ছবি + ব্যাচ ফাইল
    os.system("rm -rf hidden.zip open.bat")  # অস্থায়ী ফাইল মুছে ফেলুন
    
    print(f"{GREEN}[+] Windows-এর জন্য প্রস্তুত ফাইল: final_{output_image}{RESET}")

# আরও উন্নত ফাংশন (একাধিক ফাইল লুকানো এবং নতুন ফিচার)
def hide_multiple_files_in_image(image_path, files_to_hide, output_image):
    os.system("zip -r hidden_files.zip " + " ".join(files_to_hide))  # একাধিক ফাইলের zip তৈরি
    os.system(f"cat {image_path} hidden_files.zip > {output_image}")  # ছবি + zip একত্রিত
    os.system("rm -rf hidden_files.zip")  # zip ফাইল মুছে ফেলুন

    print(f"{GREEN}[+] একাধিক ফাইল সফলভাবে লুকানো হয়েছে! নতুন ফাইল: {output_image}{RESET}")

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
    print(f"{BLUE}[2] Hide Multiple Files in Image{RESET}")
    print(f"{BLUE}[3] About Tool{RESET}")
    print(f"{BLUE}[4] Exit{RESET}")

    choice = input(f"{YELLOW}Enter your choice: {RESET}")
    if choice == "1":
        image = input(f"{YELLOW}📂 Image file name (e.g. photo.jpg): {RESET}")
        file_to_hide = input(f"{YELLOW}📂 File to hide (e.g. secret.bat): {RESET}")
        output_image = input(f"{YELLOW}📂 Output image name (e.g. hidden_photo.jpg): {RESET}")
        
        hide_file_in_image(image, file_to_hide, output_image)
        create_windows_bat_launcher(output_image, file_to_hide)

    elif choice == "2":
        image = input(f"{YELLOW}📂 Image file name (e.g. photo.jpg): {RESET}")
        num_files = int(input(f"{YELLOW}📂 How many files do you want to hide? : {RESET}"))
        files_to_hide = []
        for i in range(num_files):
            files_to_hide.append(input(f"{YELLOW}📂 File {i+1} to hide: {RESET}"))
        output_image = input(f"{YELLOW}📂 Output image name (e.g. hidden_photo.jpg): {RESET}")
        
        hide_multiple_files_in_image(image, files_to_hide, output_image)

    elif choice == "3":
        print(f"{BLUE}🔹 This is a Termux Tool for hiding files inside images.{RESET}")
    elif choice == "4":
        print(f"{RED}❌ Exiting...{RESET}")
        exit()
    else:
        print(f"{RED}❌ Invalid Choice!{RESET}")

# প্রোগ্রাম চালানো
show_interface()
