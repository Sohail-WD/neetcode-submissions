class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for i in strs:
            count = [0] * 26

            for c in i:
                count[ord(c) - ord('a')] +=1
            key = tuple(count)

            anagrams[key] = anagrams.get(key, [])
            anagrams[key].append(i)


        return list(anagrams.values())


            

            

                 
            
        
