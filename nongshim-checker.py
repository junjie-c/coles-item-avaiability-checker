import requests
import os
import time
import random

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
        "accept-language": "en-AU,en;q=0.9",
        "baggage": "sentry-environment=prod,sentry-release=20250411.2-b318118d33147185028c8ee132c277f8598774fc,sentry-public_key=fe929b0cab4a4e3694d4ce2c52b13210,sentry-trace_id=09941b68ad1a46f7b23a012d3e2fceb5,sentry-sample_rate=0.6,sentry-transaction=%2Fproduct%2F%5Bslug%5D,sentry-sampled=true",
        "priority": "u=1, i",
        "referer": "https://www.coles.com.au/product/nongshim-shin-ramyun-black-4-pack-520g-4209094",
        "sec-ch-ua": '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"macOS"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "sentry-trace": "09941b68ad1a46f7b23a012d3e2fceb5-9e806832c3b936e1-1",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
        "x-nextjs-data": "1"
    }
    cookies = {
        "nlbi_2800108_2670698": "gDooC15IFwwzjLhq5VPXvwAAAADdDf23vEsw5+YXBa3Oiyob",
        "visid_incap_2800108": "gtn5nt3EQJacRlX1TnbxGVY6A2gAAAAAQUIPAAAAAACRFfZdY/4JtpnTrGRIl/NT",
        "incap_ses_363_2800108": "5hMqTm6z2ikMpKTU4qIJBVY6A2gAAAAAb17yfzOXb0y4i3J8sY9CjQ==",
        "ld_user": "93039b6f-6981-4cff-b988-b6d19b9bbfd2",
        "AMCVS_0B3D037254C7DE490A4C98A6%40AdobeOrg": "1",
        "sessionId": "3beb1b5f-bec9-4402-9a40-dd826872482a",
        "visitorId": "f62d23b3-e209-4636-9f13-5eca94913a7f",
        "nlbi_2800108_3037207": "FAbCWyLsozWfFMvp5VPXvwAAAACcrEQSeDGSI5KaOeaeteea",
        "analyticsIsLoggedIn": "false",
        "reese84": "3:9YJi1SA+/Sdan+VyhcOyfw==:6dI2XL2DqYe3vp9F5h7MIShjb4bTbMYGRLETKAjSrG1Si9IGbKVK2fEmqJ3mt+rgivQBAjz//E26Z8FzpN5F6F62tBa8BR3pD6OG0X4MC1xGjTsvC9vVxQKwZkN72KGddiILQxT+k1TsppHQLYfkLw/13yuoCVjba8S2M+cM+y4LO+hZoMrXx2ZTFka7foXa8UD2cJEvuWA7jddKeAh5/ai+Sfp362ZLJ5jjXgv2/2ueGD0gy+Q0LSM7wcnv2sySGVRM7Cm21IW6CpWf/8q9AbH6D0ZToYmkuR7YE8q92756Ods4unLzCLy40GDYLLdDnUumBHPBxaIKiNtEw+tAwBPwDCMWmInnHAuulEYegYg90KiXXfZWcQQqSjoYZb6og9QyJM4H/GY04ggdgUjzktyUUcOAHxd5cgiizTh7/69tOXeIquzWd7/BP/E3YfJRyMHK6V9apZ3l7OnkJXHoEQ==:zc6AajV8miUY/OOZBehj3wBmY57gZ0Wjs+WUkJqDL4A=",
        "AMCV_0B3D037254C7DE490A4C98A6%40AdobeOrg": "179643557%7CMCIDTS%7C20198%7CMCMID%7C59279252353859020041171333180641694744%7CMCAAMLH-1745646808%7C8%7CMCAAMB-1745646808%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1745049208s%7CNONE%7CMCAID%7CNONE%7CMCSYNCSOP%7C411-20205%7CvVersion%7C5.5.0",
        "at_check": "true",
        "kndctr_0B3D037254C7DE490A4C98A6_AdobeOrg_identity": "CiY1OTI3OTI1MjM1Mzg1OTAyMDA0MTE3MTMzMzE4MDY0MTY5NDc0NFIRCL_X7-TkMhgBKgRBVVMzMAPwAb_X7-TkMg==",
        "kndctr_0B3D037254C7DE490A4C98A6_AdobeOrg_cluster": "aus3",
        "_gcl_au": "1.1.1221630937.1745042009",
        "BVBRANDID": "aad75a3d-2bd2-447e-8f40-5a296120802b",
        "BVBRANDSID": "503de155-1636-4ae7-ab8f-744a99ecd58e",
        "s_cc": "true",
        "s_tp": "3773",
        "_ga": "GA1.1.1697092924.1745042014",
        "ORA_FPC": "id=639aaec1-8d9c-436f-8e42-bc62aba723c6",
        "WTPERSIST": "",
        "_fbp": "fb.2.1745042014022.484647091363620707",
        "s_ips": "574",
        "s_ecid": "MCMID|59279252353859020041171333180641694744",
        "nlbi_2800108_2147483392": "hfUwa+ev6DoEUNcK5VPXvwAAAADVz9h/DyqnSiDO3rGeBio2",
        "fs_lua": "1.1745042017558",
        "fs_uid": "#o-210D95-na1#3e9e1579-c6c6-4886-a68c-5209f506ec0a:6a1cb620-e8c3-4d11-96f8-b4a297e335f3:1745042008322::2#adbf77e2#/1776578014",
        "_fs_dwell_passed": "6a1cb620-e8c3-4d11-96f8-b4a297e335f3",
        "gpv_page": "cusp%3Aproduct%3Aproduct-details",
        "s_ppv": "cusp%253Aproduct%253Aproduct-details%2C15%2C15%2C15%2C574%2C6%2C1",
        "_ga_C8RCBCKHNM": "GS1.1.1745042014.1.1.1745042022.52.0.0",
        "s_sq": "colesonline-coles-global-prod%3D%2526c.%2526a.%2526activitymap.%2526page%253Dcusp%25253Aproduct%25253Aproduct-details%2526link%253Dset%252520location%2526region%253Dcollapsible-content%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Dcusp%25253Aproduct%25253Aproduct-details%2526pidt%253D1%2526oid%253Dfunctionrm%252528%252529%25257B%25257D%2526oidt%253D2%2526ot%253DSUBMIT",
        "fulfillmentStoreId": "0439",
        "shopping-method": "clickAndCollect",
        "mbox": "session#a7922524c8564e768c0161fb41a26579#1745043887|PC#a7922524c8564e768c0161fb41a26579.36_0#1808286818"
    }
    response = requests.get(url, headers=headers, cookies=cookies)
    print(f"Response Code: {response.status_code}")
    content_type = response.headers.get("Content-Type", "")
    if response.status_code == 200 and "application/json" in content_type:
        try:
            data = response.json()
        except Exception as e:
            print(f"Failed to parse JSON: {e}")
            print("Response text for debugging:")
            print(response.text)
            return
        available = data.get("pageProps", {}).get("product", {}).get("availability", None)
        print(f"Available: {available}")
        print(f"Store ID: {data.get("pageProps", {}).get("initStoreId", {})}")
        if available:
            print("Product is available!")
            send_wxpusher_notification()
    else:
        print(f"Failed to fetch data: {response.status_code}")
        print("Response headers:", response.headers)
        print("Response text:", response.text)

if __name__ == "__main__":
    print("Starting Coles product availability checker...")
    while True:
        check_availability()
        sleep_time = random.randint(55, 65)
        time.sleep(sleep_time)