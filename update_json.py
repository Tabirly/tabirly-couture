import json
import os

with open("koleksiyon.json", "r", encoding="utf-8") as f:
    data = json.load(f)

new_item = {
    "id": "item-007",
    "title": "Piri Reis Seyahat Botu",
    "category": "Ayakkabı / Bot",
    "slogan": "Antik Haritaların Mistik Adımları",
    "description": "Tabirly Couture'ün yeni nesil keşif ayakkabısı. 1950'lerin 'New Look' zarafetinden ilham alan bu çorap formlu botlar (sock boots), sıradan bir seyahat ayakkabısı değil. Lüks siyah deri ve antik parşömen görünümlü kanvasın melezlenmesiyle doğan bu eserin üzerinde, Piri Reis'in 1513 tarihli dünya haritasının gizemli çizgileri, pusula gülleri ve okült haritacılık motifleri işlendi. Her adımda yeni bir mistik koordinat belirleyen bu botlar, sıradan tatillere değil, gizemli diyarlara yapılan astral ve fiziksel seyahatlere eşlik etmek için yaratıldı.",
    "occasion": "Tatil ve Keşif Seyahati",
    "bodyType": "Gezgin Ruh",
    "pairsWith": ["Minimalist Kaban", "Deri Trençkot", "Pusula Kolyeleri"],
    "media": {
        "images": [
            "https://raw.githubusercontent.com/Tabirly/tabirly-couture/main/images/piri_reis_boots_front.png",
            "https://raw.githubusercontent.com/Tabirly/tabirly-couture/main/images/piri_reis_boots_back.png",
            "https://raw.githubusercontent.com/Tabirly/tabirly-couture/main/images/piri_reis_boots_left.png",
            "https://raw.githubusercontent.com/Tabirly/tabirly-couture/main/images/piri_reis_boots_right.png"
        ],
        "hasVideo": False
    }
}

data.append(new_item)

with open("koleksiyon.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("koleksiyon.json updated successfully with Piri Reis Seyahat Botu.")
