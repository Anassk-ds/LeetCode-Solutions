class Solution:
    def minSumOfLengths(self, arr, target):
        n = len(arr)

        # best[i] = minimum length of a valid subarray
        # completely inside arr[0:i]
        best = [float('inf')] * (n + 1)

        left = 0
        current_sum = 0
        answer = float('inf')

        for right in range(n):
            current_sum += arr[right]

            while current_sum > target:
                current_sum -= arr[left]
                left += 1

            if current_sum == target:
                length = right - left + 1

                # Check if there was a non-overlapping
                # subarray before this one
                if best[left] != float('inf'):
                    answer = min(answer, length + best[left])

                # Store the shortest subarray ending at right
                best[right + 1] = min(best[right], length)
            else:
                best[right + 1] = best[right]

        return answer if answer != float('inf') else -1