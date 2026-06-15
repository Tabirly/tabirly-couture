import json
import os

with open("koleksiyon.json", "r", encoding="utf-8") as f:
    data = json.load(f)

new_item = {
    "id": "item-005",
    "title": "Ritüel 2000",
    "category": "Tarihi ve Yöresel Giysiler",
    "slogan": "Lanetli Kristallerin Y2K Uyanışı.",
    "description": "Erken 2000'lerin kışkırtıcı (McBling) estetiği ile okült ayinlerin ağır ve karanlık aurasını bir araya getiren bu eser, sıradan bir kıyafet değil; ritüelistik bir dekonstrüksiyon. Koyu renkli lüks kadife kumaştan tasarlanmış bu modern Osmanlı kaftanı/pelerini, çıplak ten üzerinde kışkırtıcı bir şekilde taşınmak üzere uyarlandı. Pelerinin üzerindeki parıltılı kristal taşlar sadece süs değil, karanlık kutsal geometri ve gizli okült mühürler (sigil) oluşturuyor. Terkedilmiş, kırmızı kadife koltuklu ezoterik bir sinema salonunun lanetli yansımalarını üzerinde taşıyan bu parça, tabuları yıkan iddialı auraya sahip ruhlar için yaratıldı.",
    "occasion": "Sinema Gecesi / Gizli Ritüeller",
    "bodyType": "Karanlık Aura",
    "pairsWith": ["Bedazzled Takılar", "Gümüş Mühür Yüzükleri", "Parlak Deri Çizmeler"],
    "media": {
        "images": [
            "https://raw.githubusercontent.com/Tabirly/tabirly-couture/main/images/mcbling_occult_front.png",
            "https://raw.githubusercontent.com/Tabirly/tabirly-couture/main/images/mcbling_occult_back.png",
            "https://raw.githubusercontent.com/Tabirly/tabirly-couture/main/images/mcbling_occult_left.png",
            "https://raw.githubusercontent.com/Tabirly/tabirly-couture/main/images/mcbling_occult_right.png"
        ],
        "hasVideo": False
    }
}

data.append(new_item)

with open("koleksiyon.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("koleksiyon.json updated successfully with Ritüel 2000.")
