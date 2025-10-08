import requests

def tiktok_profile_apify(username, api_token):
    url = "https://api.apify.com/v2/acts/clockworks~free-tiktok-scraper/run-sync-get-dataset-items"
    # Parametreleri Apify dökümantasyonuna göre güncelle!
    payload = {
        "input": {
            "user": username
        }
    }
    headers = {
        "Content-Type": "application/json"
    }
    params = {
        "token": api_token
    }
    response = requests.post(url, json=payload, params=params, headers=headers)
    if response.status_code == 200:
        try:
            data = response.json()
            print("Kullanıcı bilgisi başarıyla çekildi!\n")
            print(data)
        except Exception as e:
            print(f"JSON'da hata: {e}\nYanıt: {response.text}")
    else:
        print(f"Hata oluştu: {response.status_code} - {response.text}")

if __name__ == "__main__":
    # Buraya kendi TikTok kullanıcı adını ve Apify API token'ını yaz!
    username = "derekhale656"
    api_token = "apify_api_Fq9d0TFs0AN5DmP5EPdrNoPOqMMJqW1Ssr1K"
    tiktok_profile_apify(username, api_token)
