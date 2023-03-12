class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split(' ')
        for x in range(len(arr)):
            arr[x] = arr[x][::-1]
        return ' '.join(arr)