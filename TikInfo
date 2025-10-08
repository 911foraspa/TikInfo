import requests
from bs4 import BeautifulSoup
import re

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
    url = f"https://www.tiktok.com/@{username}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    }
    resp = requests.get(url, headers=headers)
    if resp.status_code != 200:
        print("İstifadəçi tapılmadı və ya giriş bloklandı!")
        return

    soup = BeautifulSoup(resp.text, "html.parser")

    name = soup.find("h2")
    name = name.text if name else "TAPILMADI"

    follower_span = soup.find("strong", {"data-e2e": "followers-count"})
    followers = follower_span.text if follower_span else "TAPILMADI"

    following_span = soup.find("strong", {"data-e2e": "following-count"})
    following = following_span.text if following_span else "TAPILMADI"

    img_tag = soup.find("img", {"alt": True})
    profile_pic = img_tag['src'] if img_tag and 'src' in img_tag.attrs else "TAPILMADI"

    userid_search = re.search(r'"id":"(\d+)"', resp.text)
    tiktok_id = userid_search.group(1) if userid_search else "TAPILMADI"

    print(f"\n--- TikTok Məlumatı ---")
    print(f"İstifadəçi adı: @{username}")
    print(f"Profil adı: {name}")
    print(f"İzləyici sayı: {followers}")
    print(f"İzlədikləri: {following}")
    print(f"TikTok ID: {tiktok_id}")
    print(f"Profil şəkli (foto url): {profile_pic}")

    # Discord-a göndərmək üçün mesaj
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
