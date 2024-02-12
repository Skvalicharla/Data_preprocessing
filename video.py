import cv2

vid = cv2.VideoCapture('DJI_0619_W.MP4')
num_frames = int(vid.get(cv2.CAP_PROP_FRAME_COUNT))

for i in range(1, num_frames + 1):
    ret, frames = vid.read()
    if not ret:
        break

    if i % 10 == 0:
        cv2.imwrite(f'Image_0619_{i}.jpg', frames)

    #cv2.imwrite(f'Image_0359_{i}.jpg', frames)

vid.release()
cv2.destroyAllWindows()
