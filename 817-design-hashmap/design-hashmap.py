class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.space = [[] for _ in range(self.size)]
        

    def put(self, key: int, value: int) -> None:
        ind = key % self.size
        bucket = self.space[ind]
        for i , (k,v) in enumerate (bucket) :
            if k == key :   # already exist
                bucket[i] = (key,value)
                return
        # else append
        bucket.append((key,value))

        

    def get(self, key: int) -> int:
        bucket = self.space[key%self.size]
        for k,v in bucket :
            if k == key :   # found the key
                return v
        return -1        

    def remove(self, key: int) -> None:
        bucket = self.space[key%self.size]
        for i ,(k,v) in enumerate (bucket) :
            if k == key :
                bucket.pop(i)
                return
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)