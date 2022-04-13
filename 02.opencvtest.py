import numpy as np
import cv2

image = np.zeros((300, 400), np.uint8)
image.fill(200)                     # 혹은 image[:] = 200

print(type(image))
print(dir(image))

cv2.imshow("Window title", image)
cv2.waitKey(0)                      # 함수 매개 변수로 넣는 키 입력 대기 시간은 ms 단위이고 0이면 무한대기이다
cv2.destroyAllWindows()

##
##
##
##
##
##