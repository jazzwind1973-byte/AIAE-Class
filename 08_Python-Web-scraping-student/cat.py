import requests

# 從 891305124 到 891305160
for sticker_id in range(891305124, 891305161):
    url = f"https://stickershop.line-scdn.net/stickershop/v1/sticker/{sticker_id}/android/sticker.png"
    response = requests.get(url)
    
    if response.status_code == 200:
        with open(f"{sticker_id}.png", "wb") as f:
            f.write(response.content)
        print(f"已成功下載: {sticker_id}.png")
    else:
        print(f"找不到或網址失效: {sticker_id}")