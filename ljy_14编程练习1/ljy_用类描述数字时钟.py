"""
定义一个类描述数字时钟。
"""
import time


class Clock(object):
    """
    数字时钟
    """

    def __init__(self, hour=0, minute=0, second=0):
        """
        初始化方法
        :param hour:时
        :param minute:分
        :param second: 秒
        """
        self._hour = hour
        self._minute = minute
        self._second = second

    @classmethod
    def now(cls):
        ctime = time.localtime(time.time())
        return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)

    def run(self):
        """
        走字
        :return:
        """
        self._second += 1
        if self._second == 60:
            self._minute += 1
            self._second = 0
        elif self._minute == 60:
            self._hour += 1
            self._minute = 0
        elif self._hour == 24:
            self._hour = 0

    def show_time(self):
        """
        显示时间
        :return:
        """
        return f'{self._hour:02d}:{self._minute:02d}:{self._second:02d}'


def main():
    clock = Clock(23, 59, 50)
    while True:
        print(clock.show_time())
        time.sleep(1)

        clock.run()


if __name__ == '__main__':
    main()
