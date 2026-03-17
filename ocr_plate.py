import cv2
import easyocr
import os

# 初始化 OCR 模組
reader = easyocr.Reader(['en'])

# 指定 YOLO 輸出結果的圖片路徑（改成你要的圖片）
img_path = "runs/detect/predict/000.jpg"  # 改成實際檔名
img = cv2.imread(img_path)

# 手動裁一塊範圍（模擬車牌區域）
cropped = img[150:250, 100:300]  # 根據實際圖片調整位置
cv2.imwrite("cropped.jpg", cropped)

# 執行 OCR
results = reader.readtext(cropped)
for (bbox, text, prob) in results:
    print(f"🔤 辨識內容：{text}（信心分數：{prob:.2f}）")

#yolo predict task=detect model=runs/detect/train/weights/best.pt source=Taiwan-License-Plate-Recognition-Research-TLPRR-1/test/images
