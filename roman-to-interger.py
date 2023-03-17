class Solution:
    def romanToInt(self, s: str) -> int:
        # dictionary to store values of each Roman numeral
        roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
        # initialize total to zero and previous value to the value of the first numeral
        total = 0
        prev = roman_values[s[0]]
        
        # iterate through the string of Roman numerals
        for i in range(1, len(s)):
            curr = roman_values[s[i]]
            
            # if the current value is greater than the previous value, subtract the previous value
            if curr > prev:
                total -= prev
            # otherwise, add the previous value
            else:
                total += prev
            
            # update the previous value to the current value
            prev = curr
        
        # add the value of the last numeral
        total += prev
        
        return total