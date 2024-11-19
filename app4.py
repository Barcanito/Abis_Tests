import cv2 as cv



def rescaleFrame(frame, scale=0.75):
    width=int(frame.shape[1]*scale)
    height = int(frame.shape[0] * scale)
    dimensions=(width,height)

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

'''img=cv.imread('photos/dog.png')
cv.imshow('Cat',img)
resized_image=rescaleFrame(img)
cv.imshow('Image', resized_image)'''

capture=cv.VideoCapture('videos/dog.mp4')

while True:
    isTrue, frame=capture.read()
    frame_resized=rescaleFrame(frame)
    cv.imshow('video',frame)
    cv.imshow('Video Resized',frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()