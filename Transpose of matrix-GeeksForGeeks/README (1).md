
# Transpose of Matrix
link:https://www.geeksforgeeks.org/problems/transpose-of-matrix-1587115621/1?utm_source=geeksforgeeks&utm_medium=ml_article_practice_tab&utm_campaign=article_practice_tab

Write a program to find the transpose of a square matrix of size N*N. Transpose of a matrix is obtained by changing rows to columns and columns to rows.
 


Example1:
```bash
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

```

Example2:
```bash
Input:
N = 4
mat[][] = {{1, 1, 1, 1},
           {2, 2, 2, 2}
           {3, 3, 3, 3}
           {4, 4, 4, 4}}
Output: 
{{1, 2, 3, 4},  
 {1, 2, 3, 4}  
 {1, 2, 3, 4}
 {1, 2, 3, 4}} 
```

Constraints:

```bash
Input:
N = 2
mat[][] = {{1, 2},
           {-9, -2}}
Output:
{{1, -9}, 
 {2, -2}}

```

Your Task:
You dont need to read input or print anything. Complete the function transpose() which takes matrix[][] and N as input parameter and finds the transpose of the input matrix. You need to do this in-place. That is you need to update the original matrix with the transpose. 


Expected Time Complexity: O(N * N)
Expected Auxiliary Space: O(1)

Constraints:

1 <= N <= 103

-109 <= mat[i][j] <= 109