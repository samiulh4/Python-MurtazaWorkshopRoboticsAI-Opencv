import cv2

# Reading an image
# img = cv2.imread('Resources/lena.png')
# cv2.imshow('Output', img)
# cv2.waitKey(0)

# Reading Video
# cap = cv2.VideoCapture('Resources/test_video.mp4')

# while True:
#     success, img = cap.read()
#     cv2.imshow('Video', img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break


# Reading from webcam
cap = cv2.VideoCapture(0) # 0 = default webcam
cap.set(3, 640)
cap.set(4, 480)
cap.set(10, 100) #brightness

while True:
    success, img = cap.read()
    cv2.imshow('Webcam', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break