import cv2

#画像の読み込み
img = cv2.imread('mountain.jpeg')

img_c = img.copy()
#グレースケール化
img_c = cv2.cvtColor(img_c,cv2.COLOR_BGR2GRAY)

#閾値処理
ret,thresh = cv2.threshold(img_c,100,255,cv2.THRESH_BINARY)
#輪郭検出 （cv2.ChAIN_APPROX_SIMPLE）
contours1, hierarchy1 = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#輪郭の描画
cv2.drawContours(img, contours1, -1, (0, 255, 0), 2, cv2.LINE_AA)

#実行結果
cv2.imshow('contours', img)
cv2.imshow('Original', img_c)
cv2.waitKey(0)
cv2.destroyAllWindows()