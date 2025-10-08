from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time

def tiktok_profile_info(username):
    options = Options()
    options.headless = True  # Başsız mod, ekran açılmaz
    driver = webdriver.Firefox(options=options)
    url = f"https://www.tiktok.com/@{username}"
    driver.get(url)
    time.sleep(5)

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

    tiktok_id = "TAPILMADI"
    print(f"İstifadəçi adı: @{username}")
    print(f"Profil adı: {name}")
    print(f"İzləyici sayı: {followers}")
    print(f"İzlədikləri: {following}")
    print(f"TikTok ID: {tiktok_id}")
    print(f"Profil şəkli: {profile_pic}")
    driver.quit()

if __name__ == "__main__":
    user = input("TikTok istifadəçi adını daxil edin: ")
    tiktok_profile_info(user)
