import cv2
from matplotlib import pyplot as plt

#画像の読み込み
img = cv2.imread("mountain.jpeg", 0)

#閾値の設定
th = 95 
#画像輝度の最大値
i_max = 255  
#画像の二値化処理                                              
ret, i_binary = cv2.threshold(img, th, i_max, cv2.THRESH_BINARY) 

#保存する画像のパス
img_o = 'mountain_binary.jpeg'                       
cv2.imwrite(img_o, i_binary) 

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