class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for i, string in enumerate(strs):
            count = [0]*26
            for letter in string:
                count[ord("a")-ord(letter)]+=1
            result[tuple(count)].append(string)                
        
        return list(result.values())
            


