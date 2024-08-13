
# 74. Search a 2D Matrix


link:https://leetcode.com/problems/search-a-2d-matrix/description/

You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

Example1:
```bash
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

```

Example2:
```bash
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
```



Constraints:

```bash
Input:
N = 2
matrix[][] = {{1, 2},
              {3, 4}}
Output: 
Rotated Matrix:
2 4
1 3
```



Brute Force: Time Complexity: O(nLogn), Space Complexity:O(1)

Optimized: Time Complexity: (OLogn), Space Complexity:O(1)



Constraints:

m == matrix.length

n == matrix[i].length

1 <= m, n <= 100

-104 <= matrix[i][j], target <= 104