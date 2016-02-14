/*
1 2 3 4		1 2
4 5 6 7     3 4
			5 6
			7 8 

A row 1 * B col 1 = cell 11
A row 1 * B col 2 = cell 12


cell [2, 3]

A row 2 B col = 3

where A.col = B.row
*/

SELECT A.row_num, B.col_num, SUM(A.value * B.value) 
FROM A
INNER JOIN B
ON A.col_num = B.row_num
GROUP BY A.row_num, B.col_num ;



