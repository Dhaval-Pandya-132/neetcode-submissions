class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        result  = []
        for str in strs:
            count = len(str)
            result.append(f"{count}#{str}")
        return "".join(result)     

    def decode(self, s: str) -> List[str]:
        num = []
        index = 0
        result = [] 
        num_index_start = 0
        while index < len(s):
            if s[index].isdigit():
                index +=1
            if s[index] == "#":
                len_str = int(s[num_index_start:index])
                result.append(s[index+1:index+len_str+1])
                num_index_start = index+len_str+1
                index = index+len_str+1
        return result
       
            
