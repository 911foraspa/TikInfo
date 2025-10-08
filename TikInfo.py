from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import requests

def send_to_discord(webhook_url, message):
    data = {"content": message}
    try:
        response = requests.post(webhook_url, json=data)
        if response.status_code == 204:
            print("Discord-a uğurla göndərildi!")
        else:
            print(f"Discord-a göndərmək olmadı, kod: {response.status_code}")
    except Exception as e:
        print(f"Xəta oldu: {e}")

def tiktok_profile_info(username):
    options = Options()
    options.add_argument('--headless')  # Başsız rejim, brauzer açılmır
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')

    driver = webdriver.Chrome(options=options)

    url = f"https://www.tiktok.com/@{username}"
    driver.get(url)
    time.sleep(5)  # Səhifənin tam yüklənməsi üçün

    try:
        name = driver.find_element(By.TAG_NAME, 'h2').text
    except:
        name = "TAPILMADI"

    try:
        followers = driver.find_element(By.CSS_SELECTOR, "strong[data-e2e='followers-count']").text
    except:
        followers = "TAPILMADI"

    try:
        following = driver.find_element(By.CSS_SELECTOR, "strong[data-e2e='following-count']").text
    except:
        following = "TAPILMADI"

    try:
        profile_pic = driver.find_element(By.CSS_SELECTOR, 'img[alt]').get_attribute('src')
    except:
        profile_pic = "TAPILMADI"

    # TikTok ID burada almaq çətindir, ona görə TAPILMADI qoyuruq
    tiktok_id = "TAPILMADI"

    print(f"\n--- TikTok Məlumatı ---")
    print(f"İstifadəçi adı: @{username}")
    print(f"Profil adı: {name}")
    print(f"İzləyici sayı: {followers}")
    print(f"İzlədikləri: {following}")
    print(f"TikTok ID: {tiktok_id}")
    print(f"Profil şəkli (foto url): {profile_pic}")

    message = f"""
TikTok istifadəçi adı: @{username}
Profil adı: {name}
İzləyici sayı: {followers}
İzlədikləri: {following}
TikTok ID: {tiktok_id}
Profil şəkli: {profile_pic}
"""

    secim = input("Məlumatı Discord-a göndərmək istəyirsən? (bəli/xeyr): ")
    if secim.strip().lower() in ["bəli", "he", "yes"]:
        webhook_url = input("Discord Webhook linkini daxil edin: ")
        send_to_discord(webhook_url, message)

    driver.quit()

def banner():
    print(r"""
████████╗██╗ ██╗██╗██╗██╗██╗███╗   ███╗██████╗
╚══██╔══╝██║ ██║██║██║██║██║████╗ ████║██╔══██╗
   ██║   ██║ ██║██║██║██║██╔████╔██║██║  ██║
   ██║   ██║ ╚██╗██╔╝██║██║██║╚██╔╝██║██║  ██║
   ██║   ██║  ╚████╔╝ ██║██║ ╚═╝ ██║██████╔╝
   ╚═╝   ╚═╝   ╚═══╝  ╚═╝╚═╝     ╚═╝╚═════╝
              TikInfo
    """)
    print("By Aspa & Comet\n")

def menu():
    while True:
        banner()
        print("===== TikTok OSINT Menyu =====")
        print("1 - TikTok profil məlumatını sorğula")
        print("0 - Çıxış et")
        secim = input("Seçiminizi daxil edin: ")
        if secim == "1":
            user = input("TikTok istifadəçi adını daxil edin: ")
            tiktok_profile_info(user)
        elif secim == "0":
            print("Çıxılır...")
            break
        else:
            print("Yanlış seçim! Yenidən cəhd edin.")

if __name__ == "__main__":
    menu()
