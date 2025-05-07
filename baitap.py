import requests

ACCESS_TOKEN = "EAAaY3QeHVX0BO1ZCERaZAdah6EFgPPAzhLYw2WFs6X6MsGPTo5bAR0c5qolhGvJy2okZA3UeHhqrbgeZAHC5AukNvBRLsxDCXxRVjcVflllznd4ytQXZBqcoVTEV9aRswEF1ihFax7LypWtfcuyDhoZAZAcRWNYbWYeSKoZA1iyOSU9OZCbsQfzD2WuEjJDZCfuXzgUjXyS2TyTaBcOI4gKV4fKvN2"
PAGE_ID = "145118935550090"  
MESSAGE = "Nguyen Lam Son đã xong bài thực hành 06-05-2025"

url = f"https://graph.facebook.com/v22.0/{"668766549647641"}/feed"
payload = {
    "message": MESSAGE,
    "access_token": ACCESS_TOKEN
}

response = requests.post(url, data=payload)

if response.status_code == 200:
    print("✅ Đăng bài thành công!")
else:
    print("❌ Lỗi:", response.json())
