import ipaddress
from sys import argv
import sys
import os

script, file1 = argv

lst = []

try:
	with open(file1) as x:
		for line in x:
			net4 = ipaddress.ip_network(line.strip())
			for i in net4:
				i = str(i)
				lst.append(i)

except FileNotFoundError:
	print(f"Error: Filename {file1} does not exist in current directory.")
	sys.exit(1)

except ValueError:
	print("Error: Host bits are set")
	sys.exit(1)

print(f"\n The following IPs have been added to return.csv file in {os.path.dirname(os.path.abspath(__file__))}:\n {','.join(list)}")

with open('return.csv', 'w') as f:
	f.write("\n".join(lst))
