from typing import List
import heapq


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        _freq_dic = {}
        _max = 0
        _max_letters = ""

        for t in tasks:
            _freq_dic [t] = _freq_dic.get(t,0) + 1
            _prev_max = _max
            _max  = max(_max,_freq_dic[t])

            if _max == _freq_dic[t]:
                if _prev_max == _max:
                    _max_letters+=t
                else:
                    _max_letters = t            

        task_queue = []

        for key,value in _freq_dic.items():
            if value < _max:
                heapq.heappush(task_queue, (-value,key))


        counter = 0
        cycles = len(_max_letters)

        while task_queue:
            neg_freq, value = heapq.heappop(task_queue)
            freq = -neg_freq

            counter += freq
            cycles += counter // (_max -1)
            counter %= (_max -1) 

        ans = 0
        if cycles < n + 1:
            ans = (n+1) * (_max - 1) + len(_max_letters)
        else:
            ans = cycles * (_max - 1) + counter + len(_max_letters)  

        return ans
        