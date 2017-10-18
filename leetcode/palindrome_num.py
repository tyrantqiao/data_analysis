class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        """
        :warning [::-1] [start:stop:step] equal to l=L[::-1] which will use new space
        :choice choose .reverse which modify obj
        """

        if x < 0 or (x != 0 and x % 10 == 0):
            return False

        reverse = 0
        while int(x) > reverse:
            reverse = reverse * 10 + x % 10
            x = int(x / 10)
            print(int(x))

        print("reverse:{}")
        result = (x == reverse) or (x == int(reverse / 10))
        print(type(result))
        print(result)
        return result

    def update(self, x):
        """
        :return: test
        """
        b = str(x)
        a = b[::-1]
        return a == b

    def more(self, x):
        return str(x) == str(x)[::-1]
