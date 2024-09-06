
# 3217. Delete Nodes From Linked List Present in Array



link:https://leetcode.com/problems/search-a-2d-matrix/description/

You are given an array of integers nums and the head of a linked list. Return the head of the modified linked list after removing all nodes from the linked list that have a value that exists in nums.
Example1:
```bash
Input: nums = [1,2,3], head = [1,2,3,4,5]

Output: [4,5]

Explanation:



Remove the nodes with values 1, 2, and 3.



```

Example2:
```bash
Input: nums = [5], head = [1,2,3,4]

Output: [1,2,3,4]


```



Constraints:

```bash
1 <= nums.length <= 105
1 <= nums[i] <= 105
All elements in nums are unique.
The number of nodes in the given list is in the range [1, 105].
1 <= Node.val <= 105
The input is generated such that there is at least one node in the linked list that has a value not present in nums.
```


