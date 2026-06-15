from PIL import Image
import glob
import os

# Bulunan dosyayi al
file_pattern = r"C:\Users\User\.gemini\antigravity\brain\515fab05-44ca-451b-a77a-95db1e726bd0\turnaround_maternity_cape_*.png"
files = glob.glob(file_pattern)
if not files:
    print("Resim bulunamadı.")
    exit(1)

img_path = files[0]
img = Image.open(img_path)
w, h = img.size

# 4 esit parcaya bol (front, left, back, right)
w_piece = w // 4

repo_img_dir = r"C:\Users\User\Documents\GitHub\tabirly-couture\images"
os.makedirs(repo_img_dir, exist_ok=True)

# Parca isimleri
names = ["ulzzang_maternity_front", "ulzzang_maternity_left", "ulzzang_maternity_back", "ulzzang_maternity_right"]

for i in range(4):
    box = (i * w_piece, 0, (i + 1) * w_piece, h)
    piece = img.crop(box)
    out_path = os.path.join(repo_img_dir, f"{names[i]}.png")
    piece.save(out_path)
    print(f"Saved: {out_path}")

print("All pieces saved.")
