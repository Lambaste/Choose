import csv
import socket
from sys import argv

script, file1 = argv

failed, lst = [], []

with open(file1) as f:
	for line in f:
		try:
			x = socket.gethostbyname(line.strip())
			lst.append((x, line))
			l = line.rstrip('\n')
			print(f" {l} : {x}")
		except socket.gaierror:
			failed.append(line.strip())

print("Failed to resolve the following hosts: ")
print("\n".join(failed))

with open(r"resolved_hosts.csv", 'w', newline='') as r:
    writer = csv.writer(r, delimiter=",")
    writer.writerows(lst)
