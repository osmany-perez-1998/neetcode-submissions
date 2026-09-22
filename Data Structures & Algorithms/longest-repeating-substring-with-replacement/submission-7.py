class Solution:
    def characterReplacement(self, s: str, k: int) -> int: 

        if len(s) <= k:
            return k

        curr_max = k+1
        aux_key = None
        index = {}

        for i in range(len(s)):
            try:
                index[s[i]].append(i)
            except KeyError:
                index[s[i]] = [i]


        for key,value in index.items():

            if len(value) >= len(s):
                return len(s)

            left = 0
            right = len(value) -1

            while  value[right] - value[left] - (right - left) >k:
                if value[left +1 ] - value [left] >  value[right] - value [right - 1]:
                    left+=1
                else:
                    right -=1

            not_me = value[right] - value[left] - (right - left)

            aux_max = curr_max
            curr_max = max(curr_max,value[right] - value[left] + k+1 - not_me )
            if aux_max < curr_max:
                aux_key = key

        return curr_max if curr_max <= len(s) else len(s)