class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)-1
        current_max= max(arr[n], -1)
        arr[n] = -1
        n = n-1

        while n >= 0:
            current_val = arr[n]
            arr[n] = current_max
            current_max = max(current_val,current_max)
            n= n-1
        return arr

