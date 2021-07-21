

def decorator(func):
    def check_plus(width, height):
        if width > 0 and height > 0:
            func(width, height)
        else:
            print('Error!')
    return check_plus


@decorator
def triangle(width, height):
    print("삼각형의 넓이 : ", 0.5 * width * height)


@decorator
def square(width, height):
    print("사각형의 넓이 : ", width * height)


triangle(3, 5)
square(3, 5)

triangle(-1, -6)
square(-4, -6)
