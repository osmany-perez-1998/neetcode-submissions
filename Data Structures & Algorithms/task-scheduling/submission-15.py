from typing import List
import heapq


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        _freq_dic = {}
        _max = 0

        for t in tasks:
            _freq_dic [t] = _freq_dic.get(t,0) + 1
            _max  = max(_max,_freq_dic[t])          

        task_queue = []

        for value in _freq_dic.values():
            if value < _max:
                heapq.heappush(task_queue, -value)

        _max_letters_count = len(_freq_dic) - len(task_queue)
        counter = 0
        cycles = _max_letters_count

        while task_queue:
            neg_freq= heapq.heappop(task_queue)
            counter -= neg_freq
            cycles += counter // (_max -1)
            counter %= (_max -1) 

        ans = 0        
        if cycles < n + 1:
            ans = (n+1) * (_max - 1) + _max_letters_count
        else:
            ans = cycles * (_max - 1) + counter + _max_letters_count

        return ans