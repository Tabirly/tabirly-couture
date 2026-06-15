import json

file_path = r'C:\Users\User\Documents\GitHub\tabirly-couture\koleksiyon.json'

with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

new_item = {
    "id": "item-003",
    "title": "Kayıp Atlantis",
    "category": "Elbise",
    "occasion": "Özel Davetler / Mezuniyet",
    "slogan": "Derinliklerin Antik Gizemi",
    "description": "Mermaidcore estetiği ile antik arkeolojik uygarlıkların kayıp gizemlerini harmanlayan bu tasarım, unutulmuş bir Atlantis tapınağından gün yüzüne çıkmış gibi hissettiriyor. Üst parça, su altı florasının nazik hareketlerini taklit eden dalgalı yarasa kollu, yarı saydam ve yanardöner akuamarin şifon bluzdan oluşurken; fosilleşmiş nautilus kabuklarını andıran yapılandırılmış geometrik bir korse ile desteklenmektedir. Alt parça, deniz dalgalarının köpüklerini ve antik mercan dokularını barındıran sıvı görünümlü gümüş ve deniz mavisi ipekten asimetrik pilili bir etektir. Bu ihtişamlı görünüm, antik bir motif taşıyan oksitlenmiş bronz mühür yüzük, kırık deniz camlarını andıran eklem yüzükleri ve köprücük kemiklerinden süzülen balık ağı formundaki zarif metalik vücut zinciriyle tamamlanmaktadır. Kusursuz ve tekil bir ihtişam arayanlar için.",
    "bodyType": "Her beden için ideal",
    "pairsWith": ["", ""],
    "media": {
      "images": [
        "https://raw.githubusercontent.com/Tabirly/tabirly-couture/main/images/mermaid_front_view.png",
        "https://raw.githubusercontent.com/Tabirly/tabirly-couture/main/images/mermaid_back_view.png",
        "https://raw.githubusercontent.com/Tabirly/tabirly-couture/main/images/mermaid_right_profile.png",
        "https://raw.githubusercontent.com/Tabirly/tabirly-couture/main/images/mermaid_left_profile.png"
      ],
      "hasVideo": False
    }
}

data.append(new_item)

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("koleksiyon.json updated successfully.")
