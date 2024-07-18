import cv2
import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib


image = cv2.imread('', cv2.IMREAD_GRAYSCALE)


_, binary_image = cv2.threshold(image, 0, 255, cv2.THRESH_OTSU)

# ヒストグラムを計算
hist_original = cv2.calcHist([image], [0], None, [256], [0, 256])
hist_binary = cv2.calcHist([binary_image], [0], None, [256], [0, 256])

# ヒストグラムを表示
plt.figure(figsize=(12, 7))
plt.subplot(121)
plt.plot(hist_original, color='blue')
plt.title('元画像のヒストグラム')
plt.xlabel('ピクセル値')
plt.ylabel('頻度')
plt.grid()

plt.subplot(122)
plt.plot(hist_binary, color='blue')
plt.axvline(x=_, color='red', linestyle='--', label=f'大津の2値化での閾値 ({_:.2f})')
plt.title('大津の2値化後の画像のヒストグラム')
plt.xlabel('ピクセル値')
plt.ylabel('頻度')
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()
