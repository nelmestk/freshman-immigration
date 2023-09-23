import math 
import string

class Solution(object):
    def isPalindrome(self, x):
        if x == 0: 
            return True
        elif x < 0: 
            return False
        trials = []
        while x>0: 
            x, itsRemainder = divmod(x, 10)
            trials.append(itsRemainder)
        
        reversedTry = trials[::-1]
        if reversedTry == trials: 
            return True
        else: 
            return False
        """
        :type x: int
        :rtype: bool
        """
        