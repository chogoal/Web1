

def decorator(func):
    def decorated(input_text):
        print('----start----')
        func(input_text)
        print('-----end------')
    return decorated  # 함수 자체를 리턴, 호출하면 안 됨(괄호x)


@decorator
def hello_world(input_text):
    print(input_text)


hello_world('hello world')
