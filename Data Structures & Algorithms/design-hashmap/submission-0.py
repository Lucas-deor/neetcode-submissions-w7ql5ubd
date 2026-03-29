class MyHashMap:

    def __init__(self):
        self.data = [[] for i in range(10000)]

    def put(self, key: int, value: int) -> None:
        for sublist in self.data:
            if not sublist:
                sublist.append(key)
                sublist.append(value)
                break
            if sublist and key == sublist[0]:
                sublist[1] = value
                break


    def get(self, key: int) -> int:
        for sublist in self.data:
            if sublist and key == sublist[0]:
                return sublist[1]
        
        return -1

    def remove(self, key: int) -> None:
        for sublist in self.data:
            if sublist and key == sublist[0]:
                sublist.pop()
                sublist.pop()
                break


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)