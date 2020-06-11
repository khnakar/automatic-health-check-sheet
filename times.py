import random as rd

class GetRandomTime:
    def __init__(self, loop=10,):
        self.__loop = loop

    def get_random_time(self, morning=False, night=False):
        if morning:
            return tuple(f'{rd.randint(6, 9)}:{rd.randint(0, 59)}' for _ in range(self.__loop))
        elif night:
            return tuple(f'{rd.randint(22, 24)}:{rd.randint(0, 59)}' for _ in range(self.__loop))
        else:
            raise AttributeError( "'bool' object has no attribute 'get_random_time'\n引数`morning`又は`evening`を指定してください")

if __name__ == '__main__':#デバック用
    a = GetRandomTime(100)
    print(a.get_random_time(morning=True))
    print(a.get_random_time(night=True))
    print(a.get_random_time())