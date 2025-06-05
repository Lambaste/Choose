import sys
from sys import argv
import os

script, file1, file2 = argv

firstlist = []

try:
	with open(file1) as x:
		line = x.readline().strip()
		while line:
			firstlist.append(line)
			line = x.readline().strip()
except FileNotFoundError:
	print(f"\nError: Filename '{file1}' does not exist in current directory(don't forget to specify file/script type - .py, .txt, .csv...etc)")
	sys.exit(1)
	
secondlist = []

try:
	with open(file2) as y:
		line = y.readline().strip()
		while line:
			secondlist.append(line)
			line = y.readline().strip()
except FileNotFoundError:
	print(f"\nError: Filename '{file2}' does not exist in current directory(don't forget to specify file/script type - .py, .txt, .csv...etc)")
	sys.exit(1)
	
overlaplist = []

for elem in firstlist:
	if elem in secondlist:
		overlaplist.append(elem)

if overlaplist == []:
	print("No IP's added")
else:
	print(f"\n The following IPs have been added to 'overlap.csv' in {os.path.dirname(os.path.abspath(__file__))}:\n {','.join(overlaplist)}")

with open('overlap.csv', 'w') as f:
	f.write("\n".join(overlaplist))
