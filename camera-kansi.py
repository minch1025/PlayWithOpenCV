import cv2

save_path = "./"
def main():

    cam = cv2.VideoCapture(0)

    img1 = img2 = img3 = get_image(cam)
    th = 300
    num = 1
    while True:

        if cv2.waitKey(1) == 13: break

        diff = check_image(img1, img2, img3)

        cnt = cv2.countNonZero(diff)
        if cnt > th:
            print("find it")
            cv2.imshow('PUSH ENTER KEY', img3)

            cv2.imwrite(save_path + str(num) + ".jpg", img3)
            num += 1
        else:
            cv2.imshow('PUSH ENTER KEY', diff)

        img1, img2, img3 = (img2, img3, get_image(cam))

    cam.release()
    cv2.destroyAllWindows()


def check_image(img1, img2, img3):

    gray1 = cv2.cvtColor(img1, cv2.COLOR_RGB2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_RGB2GRAY)
    gray3 = cv2.cvtColor(img3, cv2.COLOR_RGB2GRAY)

    diff1 = cv2.absdiff(gray1, gray2)
    diff2 = cv2.absdiff(gray2, gray3)
    diff_and = cv2.bitwise_and(diff1, diff2)
    _, diff_wb = cv2.threshold(diff_and, 30, 255, cv2.THRESH_BINARY)
    diff = cv2.medianBlur(diff_wb, 5)
    return diff

def get_image(cam):
    img = cam.read()[1]
    img = cv2.resize(img, (600, 400))
    return img
main()
