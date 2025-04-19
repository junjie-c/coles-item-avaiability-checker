import requests
import time
import os

def send_wxpusher_notification():
    """
    Send a notification to WxPusher.
    You must fill in your appToken and uids.
    """
    content = "Nongshim-Black-4-Pack is available!"
    wxpusher_token = os.environ.get("WXPUSHER_TOKEN")
    url = f"https://wxpusher.zjiecode.com/api/send/message/{wxpusher_token}/{content}"
    try:
        resp = requests.get(url, timeout=10)
        print(f"WxPusher notification sent: {resp.status_code}, {resp.text}")
    except Exception as e:
        print(f"Failed to send WxPusher notification: {e}")

def check_availability():
    url = "https://www.coles.com.au/_next/data/20250411.2-b318118d33147185028c8ee132c277f8598774fc/en/product/nongshim-shin-ramyun-black-4-pack-520g-4209094.json?slug=nongshim-shin-ramyun-black-4-pack-520g-4209094"
    headers = {
        "accept": "*/*",
        "accept-language": "en-AU,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
        "baggage": "sentry-environment=prod,sentry-release=20250411.2-b318118d33147185028c8ee132c277f8598774fc,sentry-public_key=fe929b0cab4a4e3694d4ce2c52b13210,sentry-trace_id=7cfc8e335e8640a98ab1c828686a9bd2,sentry-sample_rate=0.6,sentry-transaction=%2Fproduct%2F%5Bslug%5D,sentry-sampled=true",
        "priority": "u=1, i",
        "referer": "https://www.coles.com.au/search/products?q=nongshim",
        "sec-ch-ua": '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"macOS"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "sentry-trace": "7cfc8e335e8640a98ab1c828686a9bd2-9c65ede4ee181891-1",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
        "x-nextjs-data": "1"
    }
    response = requests.get(url, headers=headers)
    print(f"Response Code: {response.status_code}")
    if response.status_code == 200:
        data = response.json()
        available = data.get("pageProps", {}).get("product", {}).get("availability", None)
        print(f"Available: {available}")
        if available:
            print("Product is available!")
            send_wxpusher_notification()
    else:
        print(f"Failed to fetch data: {response.status_code}")

print("Starting Coles product availability checker...")
check_availability()