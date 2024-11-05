import itertools

def generate_anagrams(word):
    # Generate all possible permutations of the word
    permutations = itertools.permutations(word)
    # Convert permutations to strings and remove duplicates using a set
    unique_anagrams = set(''.join(p) for p in permutations)
    return unique_anagrams

# Example usage
word = "abc"
anagrams = generate_anagrams(word)
print(anagrams) # {'bac', 'cba', 'acb', 'bca', 'abc', 'cab'}

# Check i 2 anagrams
from collections import Counter
def is_anagram(s, t):
    return Counter(s) == Counter(t)
print(is_anagram("anagram", "nagaram"))  # Output: True


def max_sum_subarray(arr, k):
    n = len(arr)
    if n < k:
        return None  # Not enough elements for a subarray of size k
    # Compute the sum of the first window
    window_sum = sum(arr[:k])
    max_sum = window_sum
    # Slide the window over the array
    for i in range(n - k):
        window_sum = window_sum - arr[i] + arr[i + k]
        max_sum = max(max_sum, window_sum)
    return max_sum
print(max_sum_subarray([2, 1, 5, 1, 3, 2], 3))  # Output: 9

def longest_unique_substring(s):
    n = len(s)
    if n == 0:
        return 0
    char_index = {}
    max_length = 0
    start = 0
    for end in range(n):
        if s[end] in char_index:
            start = max(start, char_index[s[end]] + 1)
        char_index[s[end]] = end
        max_length = max(max_length, end - start + 1)
    return max_length
s = "abcabcbb"
print(longest_unique_substring(s))  # Output: 3


## Two pointers 
def two_sum_sorted(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return (left, right)
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return None
print(two_sum_sorted([1, 2, 3, 4, 6], 6))  # Output: (1, 3)



"""
Consider the array nums = [1, 3, -1, -3, 5, 3, 6, 7] with a window size k = 4.

Window Position	Subarray	Maximum
[1, 3, -1, -3] 5 3 6 7	[1, 3, -1, -3]	3
1 [3, -1, -3, 5] 3 6 7	[3, -1, -3, 5]	5
1 3 [-1, -3, 5, 3] 6 7	[-1, -3, 5, 3]	5
1 3 -1 [-3, 5, 3, 6] 7	[-3, 5, 3, 6]	6
1 3 -1 -3 [5, 3, 6, 7]	[5, 3, 6, 7]	7
The output is [3, 5, 5, 6, 7], representing the maximum values in each sliding window.

Efficient Solution Using Deque:

To solve this problem efficiently, we can use a double-ended queue (deque) to keep track of indices of array elements. The deque helps in maintaining the elements in a way that the maximum element of the current window is always at the front.
"""
from collections import deque

def max_sliding_window(nums, k):
    if not nums or k == 0:
        return []
    deq = deque()
    result = []
    for i in range(len(nums)):
        # Remove elements not within the sliding window
        if deq and deq[0] < i - k + 1:
            deq.popleft()

        # Remove elements smaller than the current element from the deque
        while deq and nums[deq[-1]] < nums[i]:
            deq.pop()
        # Add current element at the end of the deque
        deq.append(i)
        # Append the maximum element of the current window to the result
        if i >= k - 1:
            result.append(nums[deq[0]])
    return result
# Example usage
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 4
print(max_sliding_window(nums, k))  # Output: [3, 5, 5, 6, 7]



"""

To merge overlapping intervals in a list, you can follow these steps:

Sort the Intervals: Begin by sorting the list of intervals based on their starting points.
Initialize the Merged List: Create a list to hold the merged intervals, starting with the first interval.
Iterate and Merge: Traverse through the sorted intervals and merge them if they overlap; otherwise, add them to the merged list.
Here's how you can implement this in Python:
"""
def merge_intervals(intervals):
    if not intervals:
        return []

    # Step 1: Sort intervals by their start times
    intervals.sort(key=lambda x: x[0])

    # Step 2: Initialize the merged list with the first interval
    merged = [intervals[0]]

    # Step 3: Iterate through the sorted intervals
    for current in intervals[1:]:
        last_merged = merged[-1]

        # If the current interval overlaps with the last merged interval, merge them
        if current[0] <= last_merged[1]:
            last_merged[1] = max(last_merged[1], current[1])
        else:
            # No overlap; add the current interval to the merged list
            merged.append(current)

    return merged
print(merge_intervals([[1, 4], [3, 6], [7, 10], [11, 15]]))  # Output: [[1, 6], [7, 10], [11, 15]]













## Fast and slow pointt s
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

# Example usage
# Creating a cycle for demonstration
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2  # Cycle here

print(has_cycle(node1))  # Output: True



