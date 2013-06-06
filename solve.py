#!/usr/bin/python

import math

a =[[ 6,7,0,3,4,1,0,5,0 ],
	[ 5,0,0,0,8,0,0,7,0 ],
	[ 0,8,0,0,5,0,3,1,2 ],
	[ 0,5,0,0,6,0,0,9,7 ],
	[ 7,0,0,4,2,8,0,0,1 ],
	[ 3,1,4,5,0,0,2,0,0 ],
	[ 1,4,7,0,0,5,0,0,9 ],
	[ 8,0,0,0,0,4,7,6,0 ],
	[ 0,0,3,0,0,2,1,0,5 ]]
	
b = [
	[ 0,0,9,7,0,0,2,0,5 ],
	[ 1,3,7,0,0,8,4,0,0 ],
	[ 0,6,0,9,3,0,1,0,0 ],
	[ 0,7,0,0,5,3,0,4,0 ],
	[ 8,4,0,0,0,9,0,7,2 ],
	[ 0,9,3,0,4,0,6,0,1 ],
	[ 9,2,8,0,0,0,0,6,4 ],
	[ 7,0,6,4,0,5,0,0,3 ],
	[ 0,0,0,0,8,2,7,1,0 ],
]

c = [
	[ 3,0,7,4,0,0,2,0,0 ],
	[ 0,0,4,0,0,0,0,0,0 ],
	[ 0,0,0,0,0,0,5,1,0 ],
	[ 0,0,0,0,1,3,0,9,0 ],
	[ 0,0,0,5,9,0,0,0,8 ],
	[ 0,0,0,2,0,0,0,0,0 ],
	[ 7,6,0,0,2,0,0,0,0 ],
	[ 0,0,0,8,0,0,0,2,0 ],
	[ 9,1,0,0,3,0,0,0,0 ],
]

h = [
	[ 0,0,0,3,2,0,0,0,7 ],
	[ 0,0,0,0,0,0,1,0,0 ],
	[ 0,0,3,0,0,0,0,2,0 ],
	[ 0,0,0,0,0,0,2,0,0 ],
	[ 3,2,0,0,0,0,0,7,0 ],
	[ 0,0,1,0,0,9,4,0,0 ],
	[ 0,0,0,7,0,0,0,0,0 ],
	[ 0,0,0,0,0,0,0,9,2 ],
	[ 0,0,0,8,0,3,0,0,0 ],	
]
	
def pt(matr) : # Prints out the matrix.
	s = ' '
	size = int(math.sqrt(len(matr)))
	for i in range(len(matr)) :
		for j in range(len(matr[i])) :
			s = s + str(matr[i][j]) + ' '
			#c1 += 1
			#if c1 == 3 or c1 == 6 :
			if (j+1) % size == 0 and j != size*size - 1 :
				s = s + '| '
		print s
		s = ' '
		if (i+1) % size == 0 and i != size*size - 1 :
			print " ------|-------|------"
	print
		
def inrow( matr, row, num ) :
	occ = []
	for i in range(len(matr[row])):
		if matr[row][i] == num :
			occ.append(row * 10 + i)
	return occ
	
def incol( matr, col, num ) :
	occ = []
	for i in range(len(matr)) :
		if matr[i][col] == num :
			occ.append(i * 10 + col)
	return occ

def insec( matr, sec, num ) :
	occ = []
	size = int(math.sqrt(len(matr)))
	for i in range(len(matr)) :
		if matr[ sec / size * size + i / size ][ sec % size * size + i % size ] == num :
			occ.append((sec / size * size + i / size) * 10 + sec % size * size + i % size )
	return occ

def inscope( matr, pos, num ):
	size = int(math.sqrt(len(matr)))
	row = pos / 10
	col = pos % 10
	occ = list(set(inrow(matr, row, num) + incol (matr, col, num) + insec(matr, row / 3 * 3 + col / 3, num)))
	occ.sort()
	return occ

#def isleft( matr, pos, num)
	

pt(h)
occ = inscope( h, 5, 0)
print occ, len(occ)
