"""
https://www.codewars.com/kata/52685f7382004e774f0001f7/train/python
    HH = hours, padded to 2 digits, range: 00 - 99
    MM = minutes, padded to 2 digits, range: 00 - 59
    SS = seconds, padded to 2 digits, range: 00 - 59
"""
from Tester import verdict, log


def make_readable(seconds):
    minute = 60
    hour = 60 * minute

    hours = int(seconds / hour)
    seconds -= hour * hours

    minutes = int(seconds / minute)
    seconds -= minute * minutes

    print("H: {}    M: {}   S: {}".format(hours, minutes, seconds))



    return None
if __name__ == '__main__':

    make_readable(3600 )

    # verdict(make_readable(0), "00:00:00")
    # verdict(make_readable(5), "00:00:05")
    # verdict(make_readable(60), "00:01:00")
    # verdict(make_readable(86399), "23:59:59")
    # verdict(make_readable(359999), "99:59:59")

