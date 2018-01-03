# A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6 LEDs on the bottom represent the minutes (0-59).
#
# Each LED represents a zero or one, with the least significant bit on the right.
#
# For example, the above binary watch reads "3:25".
#
# Given a non-negative integer n which represents the number of LEDs that are currently on, return all possible times the watch could represent.
#
# Example:
#
# Input: n = 1
# Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
#
# Note:
#
#     The order of output does not matter.
#     The hour must not contain a leading zero, for example "01:00" is not valid, it should be "1:00".
#     The minute must be consist of two digits and may contain a leading zero, for example "10:2" is not valid, it should be "10:02".


# 一种解决方案
class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        return ["%d:%02d" % (h, m) for h in range(12) for m in range(60) if (bin(h) + bin(m)).count('1') == num]


# 另外一种解决方案
class Solution(object):
    def calc_times(self, leds, idx, curr_hr, curr_min, result, n):
        if n == 0:
            if curr_min < 10:
                result.append(str(curr_hr) + ":0" + str(curr_min))
            else:
                result.append(str(curr_hr) + ":" + str(curr_min))

        elif n > 0 and idx < len(leds):
            if 0 <= idx <= 3 and curr_hr + leds[idx] < 12:
                self.calc_times(leds, idx + 1, curr_hr + leds[idx], curr_min, result, n - 1)
            elif idx > 3 and curr_min + leds[idx] < 60:
                self.calc_times(leds, idx + 1, curr_hr, curr_min + leds[idx], result, n - 1)
            self.calc_times(leds, idx + 1, curr_hr, curr_min, result, n)

    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        result = []
        leds = [8, 4, 2, 1, 32, 16, 8, 4, 2, 1]
        self.calc_times(leds, 0, 0, 0, result, num)
        return result
