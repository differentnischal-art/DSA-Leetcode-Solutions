class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
      sum = 0

        # First window
      for i in range(k):
            sum = sum + arr[i]

      count = 0

        # Check first window
      if sum >= threshold * k:
            count = count + 1

        # Slide the window
      for i in range(k, len(arr)):
            sum = sum + arr[i] - arr[i-k]

            if sum >= threshold * k:
                count = count + 1
      return count
            