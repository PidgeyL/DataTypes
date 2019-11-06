class RangedList():
    def __init__(self, default=None):
        self._data   = {}
        self.default = default


    def set(self, start, stop, value):
        stop_i  = self._get_id(stop)
        # Set start and stop
        next_val = self.get(stop+1)
        self._data[start] = value
        self._data[stop+1] = next_val
        # Delete the keys in between
        for index in set(self._data.keys()).intersection(range(start+1, stop)):
            del self._data[index]
        # Optimize by removing subsequent similar keys
        if self.get(start-1) == value:
            del self._data[start]
        if self._data.get(stop+1) and self.get(stop+1) == value:
            del self._data[stop+1]


    def get(self, index):
        _range = self._get_id(index)
        if _range is not None:
            return self._data[_range]
        else:
            return self.default


    def get_range(self):
        return list(sorted(self._data.keys()))


    def _get_id(self, index):
        ranges = self.get_range()
        _range = None
        for i in ranges:
            if i <= index:
                _range = i
            else:
                break
        return _range

