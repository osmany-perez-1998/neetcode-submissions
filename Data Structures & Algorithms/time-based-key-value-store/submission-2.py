class TimeMap:

    def __init__(self):
        self.dic = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        values = self.dic.get(key,[])
        values.append((timestamp,value))
        self.dic[key] = values
        

    def get(self, key: str, timestamp: int) -> str:

        base = self.dic.get(key,None)
        if not base or base[0][0] > timestamp:
            return ""

        values = self.dic[key]
        

        _l,h = 0, len(values) -1

        if _l == h :
            return values[0][1]

        
        while _l <= h:

            mid = (_l + h) // 2

            if values[mid][0] == timestamp:
                return values[mid][1]

            if values[mid][0] < timestamp:
                _l = mid + 1
            else:
                h = mid - 1
            

        _min = min(_l,h)
        return values [_min][1] if values[_min][0] < timestamp else values[_min-1][1]