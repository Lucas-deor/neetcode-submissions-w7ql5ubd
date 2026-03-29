class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)
        res = []
        
        for i in range(len(nums)):
            hashmap[nums[i]] += 1
        
        for i in range(k):
            max_key = max(hashmap, key=hashmap.get)
            res.append(max_key)
            deleted_key = hashmap.pop(max_key)
        
        return res

