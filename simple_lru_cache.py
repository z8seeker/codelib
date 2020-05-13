from collections import OrderedDict


class SimpleLRUCache:
    def __init__(self, capacity: int = 3000):
        self.capacity = capacity
        self._dict = OrderedDict()

    def __getitem__(self, key: str, default=None) -> Any:
        try:
            value = self._dict.pop(key)
        except KeyError:
            return default
        else:
            self._dict[key] = value

        return value

    def __setitem__(self, key: str, value: Any) -> None:
        if len(self._dict) >= self.capacity:
            self._dict.popitem(last=False)
        self._dict[key] = value

