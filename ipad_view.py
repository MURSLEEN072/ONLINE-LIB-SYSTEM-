import os
import time

# 🎨 Colors
RED = "\033[1;31m"
GREEN = "\033[1;32m"
BLUE = "\033[1;34m"
RESET = "\033[0m"

os.system("clear")
print(f"{BLUE}≈═══════════════════════════════≈{RESET}")
print(f"{GREEN}   YT-{RESET}{BLUE}MURS{RESET}{GREEN}LEEN{RESET}{RED}VIP{RESET} {BLUE}IPAD{RESET} {GREEN}VIEW{RESET} {BLUE}UNLOCK 🚀{RESET}")
print(f"{BLUE}≈═══════════════════════════════≈{RESET}")
print("")

print(f"{RED}[⚡] Closing PUBG Mobile...{RESET}")
os.system("am force-stop com.tencent.ig")
time.sleep(1)

print(f"{RED}[⚡] Setting DPI to iPad Mode...{RESET}")
os.system("wm density 560")
os.system("wm size 1920x1080")
print(f"{GREEN}[✅] iPad DPI Applied!{RESET}")
time.sleep(1)

print(f"{RED}[⚡] Unlocking iPad View (120° FOV)...{RESET}")
fov_config = "/storage/emulated/0/Android/data/com.tencent.ig/files/UE4Game/ShadowTrackerExtra/ShadowTrackerExtra/Saved/Config/Android/UserSettings.ini"

ipad_view_code = """
[/Script/Engine.LocalPlayer]
AspectRatioAxisConstraint=AspectRatio_MaintainYFOV
"""
with open(fov_config, "a") as file:
    file.write(ipad_view_code)

print(f"{GREEN}[✅] iPad View 120° FOV Activated!{RESET}")
time.sleep(1)

print(f"{RED}[⚡] Opening PUBG Mobile...{RESET}")
os.system("am start -n com.tencent.ig/com.epicgames.ue4.SplashActivity")

print("")
print(f"{BLUE}🎉 iPad View Applied! Enjoy Wider FOV!{RESET}")
print("")