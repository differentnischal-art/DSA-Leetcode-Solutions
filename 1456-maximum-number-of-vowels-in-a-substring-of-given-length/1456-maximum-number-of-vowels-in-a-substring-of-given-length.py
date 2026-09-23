class Solution(object):
    def maxVowels(self, s, k):
        count=0
        for i in range(k):
            if s[i] in "aeiou":
                count=count+1
        max_count=count

        for i in range(k,len(s)):
            if s[i-k] in 'aeiou':
                count=count-1
            if s[i] in 'aeiou':
                count =count+1
            if count>max_count:
                max_count=count
            
        return max_count


        