import cv2 as cv


def make_generator(start_at: int):
    pos = start_at

    def generate():
        nonlocal pos
        pos += 1
        return pos

    return generate



if __name__ == '__main__':
    gen = make_generator(3)
    print(gen())
    print(gen())
    print(gen())
    # img = cv.imread("test.jpg")
    # cv.imshow("test", img)
    # cv.waitKey(0)
