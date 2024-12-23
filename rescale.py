import cv2 as cv

# Reading images
img = cv.imread('Resources/Photos/cat.jpg')
cv.imshow('Cat', img)

def rescaleFrame(frame, scale=0.75):
    # Images, videos and live videos
    width = int(frame.shape[1] * scale) 
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# Reading images
img = cv.imread('Resources/Photos/cat.jpg')
resized_image = rescaleFrame(img)
cv.imshow('Image', resized_image)
cv.waitKey(0)


def changeRes(width, height):
    # Live videos
    capture.set(3, width)
    capture.set(4, height)

# Reading Videos
# capture = cv.VideoCapture('Resources/Videos/dog.mp4')

# while True:
#     isTrue, frame = capture.read()

#     frame_resized = rescaleFrame(frame, scale=.2)

#     cv.imshow('Video', frame)
#     cv.imshow('Video Resized', frame_resized)

#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break

# capture.release()
# cv.destroyAllWindows()