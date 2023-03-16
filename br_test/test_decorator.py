# decorator 装饰器

def aop(func):
    def wrapper():
        print('before func')
        func()
        print('after func')

    return wrapper

# @aop
def hi():
    print('hi')

# @aop
def hello():
    print('hello')

if __name__ == "__main__":
    hi()
    
    print("")

    hi = aop(hi)
    hi()
