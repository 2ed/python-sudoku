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
	[ 0,0,9,7,0,0,2,0,5 ], # 8
	[ 1,3,7,0,0,8,4,0,0 ],
	[ 0,6,0,9,3,0,1,0,0 ],
	[ 0,7,0,0,5,3,0,4,0 ],
	[ 8,4,0,0,0,9,0,7,2 ],
	[ 0,9,3,0,4,0,6,0,1 ],
	[ 9,2,8,0,0,0,0,6,4 ],
	[ 7,0,6,4,0,5,0,0,3 ], # 9
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
			if (j+1) % size == 0 and j != size*size - 1 :
				s = s + '| '
		print s
		s = ' '
		if (i+1) % size == 0 and i != size*size - 1 :
			print " ------|-------|------"
	print
		
def inzone(matr, place,	pos, num = None):
	occ = []
	size = int(math.sqrt(len(matr)))
	if place == 'row':
		ax = by = 0
		bx = pos / 10
		ay = sax = 1
		say = 10
	elif place == 'col':
		ax = sax = 1
		bx = ay = 0
		by = pos % 10
		say = 10
	elif place == 'sec':
		sax = say = size
		ax = ay = 1
		bx = pos / 10 / size * size
		by = pos % 10 / size * size
	for i in range(len(matr)):
		mx = i / sax * ax + bx
		my = i % say * ay + by
		item = matr[ mx ][ my ]
		#print i, mx, my, ax, sax, bx, ay, say, by
		if (not num and num != 0) or item == num :
			#matr[ mx ][ my ] = 'z'
			occ.append(mx * 10 + my)
	return occ

def inrow( matr, row, num = None) : # Occurrences of a number in a row.
	occ = []
	for i in range(len(matr[row])):
		if not num or matr[row][i] == num :
			occ.append(row * 10 + i)
	return occ
	
def incol( matr, col, num = None) : # Occurrences of a number in a column.
	occ = []
	for i in range(len(matr)) :
		if not num or matr[i][col] == num :
			occ.append(i * 10 + col)
	return occ

def insec( matr, sec, num = None) : # Occurrences in sector.
	occ = []
	size = int(math.sqrt(len(matr)))
	for i in range(len(matr)) :
		if not num or matr[ sec / size * size + i / size ]\
				[ sec % size * size + i % size ] == num :
			occ.append((sec / size * size + i / size) * 10 \
				+ sec % size * size + i % size )
	return occ

def inscope( matr, pos, num = None ): # Occurrences is sector + row + col.
	size = int(math.sqrt(len(matr)))
	row = pos / 10
	col = pos % 10
	occ = list(set(inrow(matr, row, num) + incol (matr, col, num) + \
		insec(matr, row / 3 * 3 + col / 3, num)))
	occ.sort()
	if num == 0:
		occ.remove(pos)
	return occ

def zeros(matr): # Returns list of existing zeros.
	z = []
	for i in range(len(matr)):
		for j in range(len(matr)):
			if matr[i][j] == 0:
				z.append( i*10 + j )	
	return z
	
def whichnum(matr, pos): # Wich numbers can be placed at pos.
	occ = []
	bag = range(1, len(matr) + 1)
	for j in inscope(matr, pos):
		num = matr[ j / 10 ][ j % 10 ]
		if bag.count(num) > 0:
			bag.remove(num)
	return bag
		
def simplecheck(matr, pos): 
	avail = whichnum(matr, pos)
	if pos == 82:
		print avail, 'check'
	if len(avail) == 1:
		#print 'one',avail[0],pos
		return avail[0]
	elif len(avail) == 0:
		return 10
	else:
		for item in avail:
			for rownum in inrow(matr, pos / 10, 0):
				if item in whichnum(matr, rownum):
					if pos == 82:	
						print whichnum(matr, rownum), 'row', rownum, pos, item
					break
			else:
				#print 'two',item,pos
				return item
			for colnum in incol(matr, pos % 10, 0):
				if colnum != pos and item in whichnum(matr, colnum):
					break
			else:
				#print 'three',item,pos
				return item
			for secnum in insec(matr, pos / 30 * 3 + pos % 10 / 3 , 0): 
				if secnum != pos and item in whichnum(matr, secnum):
					break
			else:
				#print 'four',item,pos
				return item					

def solve(x):
	pt(x)
	errors = []
	while True:
		zero = zeros(x)
		for z in zero:
			res = simplecheck( x , z )
			if res and res != 10 :
				x[ z / 10 ][ z % 10 ] = res
			elif res == 10 :
				errors.append(z)
		if len(zeros(x)) == 0:
			print "Done! ^ v^\n"
			break
		elif len(zeros(x)) == len(zero):
			print "I'm stuck ._.\n"
			break
	pt(x)
	if len(errors) > 0 :
		print "Errors: ", errors
	
#solve(c)
