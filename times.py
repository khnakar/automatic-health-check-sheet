import random as rd

class GetRandomTime:
    def __init__(self, loop=10):
        self.__loop = loop

    def get_time(self, morning=False, night=False):
        return tuple(f'{rd.choice([i+6 for i in range(3)] if morning else [i+22 for i in range(3)] if night else [])}：{rd.randint(0, 59)}' for _ in range(self.__loop))

if __name__ == '__main__':#デバック用
    a = GetRandomTime(100)
    print(a.get_time(morning=True))
    print(a.get_time(night=True))