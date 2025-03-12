import os
import webbrowser
import subprocess

# ✅ TOOL CONFIGURATION
TOOL_KEY = "YT-MURSLEEN .h"
TELEGRAM_LINK = "https://t.me/YT_MURSLEEN_CHEATS_VIP"
STORAGE_PATH = "/storage/emulated/0/"
INPUT_FOLDER = os.path.join(STORAGE_PATH, "input_pngs")
OUTPUT_FOLDER = os.path.join(STORAGE_PATH, "output_headers")

# ✅ COLOR CONFIG
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
CYAN = "\033[96m"
WHITE = "\033[97m"
MAGENTA = "\033[95m"
RESET = "\033[0m"

def banner():
    os.system("clear")
    print(f"{MAGENTA}========================================{RESET}")
    print(f"""{RED}{GREEN}{YELLOW}{CYAN}{BLUE}{MAGENTA}{WHITE}{RESET} {YELLOW}Y{RED}T{BLUE}-M{GREEN}URS{YELLOW}LEEN {CYAN}VIP {MAGENTA}TOOL {WHITE} PNG {RED}TO {GREEN}.H{RESET}""")
    print(f"{MAGENTA}========================================{RESET}")

def open_telegram():
    print(f"\n{BLUE}📢 Opening {GREEN}Telegram {RED}Channel...{RESET}")

    try:
        subprocess.run(["termux-open-url", TELEGRAM_LINK], check=True)
    except:
        webbrowser.open(TELEGRAM_LINK)

    print(f"{GREEN}✅ Join Here: {TELEGRAM_LINK}{RESET}\n")

def check_key():
    print(f"\n🔑 {CYAN}ENTER TOOL KEY TO CONTINUE{RESET}")
    user_key = input(f"{YELLOW}🔐 Enter Key: {RESET}")

    if user_key == TOOL_KEY:
        print(f"\n✅ {RED}C{GREEN}o{YELLOW}r{BLUE}r{MAGENTA}e{WHITE}c{CYAN}t {RED}K{GREEN}e{YELLOW}y{RESET}! {GREEN}Tool Unlocked 🚀{RESET}\n")
        return True
    else:
        print(f"\n❌ {RED}Wrong Key! {YELLOW}Join {BLUE}Telegram {GREEN}for {MAGENTA}Access {WHITE}🔒{RESET}")
        open_telegram()
        return False

def png_to_header(png_file, header_file):
    try:
        with open(png_file, "rb") as f:
            data = f.read()

        with open(header_file, "w") as f:
            f.write("/*\n")
            f.write("==============================\n")
            f.write("CREATED-BY : YT-MURSLEEN TOOL\n")
            f.write("==============================\n")
            f.write("*/\n\n")

            f.write("#ifndef IMAGE_H\n#define IMAGE_H\n\n")
            f.write("const unsigned char image_data[] = {\n    ")

            hex_data = ', '.join(f"0x{byte:02X}" for byte in data)
            f.write(hex_data)

            f.write("\n};\nconst unsigned int image_size = sizeof(image_data);\n\n#endif")

        print(f"{GREEN}[✅ SUCCESS] {YELLOW}{png_file} {BLUE}→ {RED}{header_file}{RESET}")

    except Exception as e:
        print(f"{RED}[❌ ERROR] {png_file}: {WHITE}{e}{RESET}")

def batch_convert():
    if not os.path.exists(INPUT_FOLDER):
        os.makedirs(INPUT_FOLDER)
        print(f"{CYAN}📂 {RED}Folder Created: {GREEN}{INPUT_FOLDER} {WHITE}(Add PNGs Here){RESET}")

    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)
        print(f"{CYAN}📂 {MAGENTA}Folder Created: {GREEN}{OUTPUT_FOLDER} {WHITE}(Headers Will Save Here){RESET}")

    png_files = [f for f in os.listdir(INPUT_FOLDER) if f.endswith(".png")]

    if not png_files:
        print(f"{YELLOW}[⚠️] {RED}No PNG files found! {GREEN}Add PNGs to {MAGENTA}'input_pngs'{RESET}")
        return

    for png in png_files:
        png_path = os.path.join(INPUT_FOLDER, png)
        header_path = os.path.join(OUTPUT_FOLDER, png.replace(".png", ".h"))
        png_to_header(png_path, header_path)

def main_menu():
    while True:
        banner()
        print(f"{GREEN}🎨 {BLUE}PNG {MAGENTA}TO {YELLOW}.H {RED}CONVERTER - {CYAN}YT-MURSLEEN {WHITE}VIP TOOL{RESET}")
        print(f"{RED}1️⃣ {GREEN}Convert {YELLOW}PNGs {BLUE}to {MAGENTA}.h{RESET}")
        print(f"{CYAN}2️⃣ {MAGENTA}Join {WHITE}Telegram {GREEN}Channel{RESET}")
        print(f"{RED}3️⃣ {YELLOW}Exit{RESET}")

        choice = input(f"\n👉 {WHITE}Choose {BLUE}Option: {RESET}")

        if choice == "1":
            batch_convert()
        elif choice == "2":
            open_telegram()
        elif choice == "3":
            print(f"\n👋 {RED}Exiting {YELLOW}Tool...{RESET}")
            break
        else:
            print(f"\n❌ {RED}Invalid {WHITE}Option! {CYAN}Try {GREEN}Again.{RESET}")

if __name__ == "__main__":
    banner()
    if check_key():
        main_menu()