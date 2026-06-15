import json
import os

with open("koleksiyon.json", "r", encoding="utf-8") as f:
    data = json.load(f)

new_item = {
    "id": "item-004",
    "title": "Parizyen Nostalji",
    "category": "Elbise",
    "slogan": "Geçmişin serin rüzgarlarına ipek bir dokunuş.",
    "description": "Nostaljik ve romantik bir hava taşıyan, Fransız şıklığından (French Girl Chic) ilham alan vintage esintili anvelop elbise tasarımı. Tozlu gül kurusu rengindeki hafif ipek şifon kumaşı, rüzgarlı geçiş mevsimlerinde rüzgarla dans edecek şekilde özel olarak uyarlandı. 35mm sinematik bir film karesinden fırlamış gibi hissettiren bu tasarım, ruhunuzdaki geçmişe özlemi dışa vuruyor.",
    "occasion": "Rüzgarlı Havalar / Geçiş Mevsimi",
    "bodyType": "Her beden için ideal",
    "pairsWith": ["Deri Ceket", "Minimalist Takılar", "Nostaljik Çizmeler"],
    "media": {
        "images": [
            "https://raw.githubusercontent.com/Tabirly/tabirly-couture/main/images/french_chic_front.png",
            "https://raw.githubusercontent.com/Tabirly/tabirly-couture/main/images/french_chic_back.png",
            "https://raw.githubusercontent.com/Tabirly/tabirly-couture/main/images/french_chic_left.png",
            "https://raw.githubusercontent.com/Tabirly/tabirly-couture/main/images/french_chic_right.png"
        ],
        "hasVideo": False
    }
}

data.append(new_item)

with open("koleksiyon.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("koleksiyon.json updated successfully with Parizyen Nostalji.")
