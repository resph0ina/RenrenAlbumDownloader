import time
import cv2
import cv2.cv as cv

def detect(img, cascade_fn='haarcascade_frontalface.xml',
           scaleFactor=1.3, minNeighbors=4, minSize=(20, 20),
           flags=cv.CV_HAAR_SCALE_IMAGE):
    cascade = cv2.CascadeClassifier(cascade_fn)
    rects = cascade.detectMultiScale(img, scaleFactor=scaleFactor,
                                     minNeighbors=minNeighbors,
                                     minSize=minSize, flags=flags)
    if len(rects) == 0:
        return []
    rects[:, 2:] += rects[:, :2]
    return rects

def draw_rects(img, rects, color):
    for x1, y1, x2, y2 in rects:
        cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)

def face_detect(imgfile):
    print imgfile
    img_color = cv2.imread(imgfile)
    if img_color.shape[2] > 2:
        img_gray = cv2.cvtColor(img_color, cv.CV_RGB2GRAY)
    else:
        img_gray = img_color
    img_gray = cv2.equalizeHist(img_gray)
    return detect(img_gray)


def demo(in_fn, out_fn):
    print ">>> Loading image..."
    img_color = cv2.imread(in_fn)
    img_gray = cv2.cvtColor(img_color, cv.CV_RGB2GRAY)
    img_gray = cv2.equalizeHist(img_gray)
    print in_fn, img_gray.shape

    print ">>> Detecting faces..."
    start = time.time()
    rects = detect(img_gray)
    end = time.time()
    print 'time:', end - start
    img_out = img_color.copy()
    draw_rects(img_out, rects, (0, 255, 0))
    cv2.imwrite(out_fn, img_out)


def main():
    demo('y:/face.jpg', 'y:/pic.detect.jpg')


if __name__ == '__main__':
    main()