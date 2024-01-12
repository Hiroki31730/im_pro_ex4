import cv2
from matplotlib import pyplot as plt

#画像の読み込み
img = 'shogi.jpeg'                                               
i = cv2.imread(img, 0)                                        
 
#画像の最大輝度
i_max = 255                                                   
 
# 適応的閾値処理による二値化
i_binary = cv2.adaptiveThreshold(i, i_max, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 39, 2)

#ここからグラフ設定
fig = plt.figure()
ax1 = fig.add_subplot(111)
 
# 画像をプロット
ax1.imshow(i_binary, cmap = 'gray')
 
# 軸を消す設定
ax1.tick_params(labelbottom = False, bottom = False)
ax1.tick_params(labelleft = False, left = False)
 
fig.tight_layout()
plt.show()
plt.close()