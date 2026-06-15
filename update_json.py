import json
import os

with open("koleksiyon.json", "r", encoding="utf-8") as f:
    data = json.load(f)

new_item = {
    "id": "item-006",
    "title": "Kutsal Oran Pelerini",
    "category": "Dış Giyim",
    "slogan": "Yaşamın ve Evrenin Matematiksel Rahmi",
    "description": "Tabirly Couture, 'Ulzzang' tarzının kusursuz minimalizmini ezoterik doğanın sırlarıyla birleştiriyor. Hamile (Maternity) aurası için özel tasarlanmış bu kaban-pelerin, dış giyim kavramını yepyeni bir okült seviyeye taşıyor. Kumaşın her bir katmanı, volümü ve asimetrik dökümü; Altın Oran'a (Golden Ratio) ve Fibonacci spiraline milimetrik hesaplarla sadık kalarak dikildi. İnsanlığın varoluş ve doğum döngüsünü doğanın en kutsal matematiğiyle onurlandıran bu karanlık ve avangart pelerin, anne adayını adeta ezoterik bir kozanın içine alarak onu dünyevi kaostan koruyor. (Görseller: Karakter Konsept Analiz Sayfası)",
    "occasion": "Hamilelik / Yaratım Süreci",
    "bodyType": "Ulzzang Aura / Gebe Beden",
    "pairsWith": ["Sade Siyah Balıkçı Yaka", "Sivri Burunlu Botlar"],
    "media": {
        "images": [
            "https://raw.githubusercontent.com/Tabirly/tabirly-couture/main/images/ulzzang_maternity_front.png",
            "https://raw.githubusercontent.com/Tabirly/tabirly-couture/main/images/ulzzang_maternity_left.png",
            "https://raw.githubusercontent.com/Tabirly/tabirly-couture/main/images/ulzzang_maternity_back.png",
            "https://raw.githubusercontent.com/Tabirly/tabirly-couture/main/images/ulzzang_maternity_right.png"
        ],
        "hasVideo": False
    }
}

data.append(new_item)

with open("koleksiyon.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("koleksiyon.json updated successfully with Kutsal Oran Pelerini.")
