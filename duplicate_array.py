# Find duplicate in array
class Solution:
    def duplicates(self, arr, n): 
        arr.sort()
        ans = []
        ans_prev = None
        prev = arr[0]
        for i in range(1, n):
            if prev == arr[i]:
                if prev != ans_prev:
                    ans.append(prev)
                    ans_prev = prev
            else:
                prev = arr[i]
        if not ans:
            return [-1]
        return ans

if(__name__=='__main__'):
  t = int(input())
  for i in range(t):
    n = int(input())
    ar = list(map(int, input().strip().split()))
    res = Solution().duplicates(arr, n)
    for i in res:
      print(i, end=" ")
    print()
  


    
