import random as rd

class BodyTemp:
    def __init__(self, min_temp=36.0, max_temp=37.0):
        self.min_temp = min_temp
        self.max_temp = max_temp
        if self.min_temp > self.max_temp:
            raise ValueError("`min_temp < max_temp`を満たしていません")
    def get_random_body_temp(self, loop=1):
        return tuple(rd.uniform(self.min_temp, self.max_temp).__round__(1)for _ in range(loop))
if __name__ == '__main__':#デバック用
    a =BodyTemp()
    print(a.get_random_body_temp(100))




