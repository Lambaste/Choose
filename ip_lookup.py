import csv
import socket

def look():
    file1 = input("Enter the filename containing the hostnames to look up: ").strip()
    failed, lst = [], []

    try:
        with open(file1) as f:
            for line in f:
                host = line.strip()
                try:
                    ip = socket.gethostbyname(host)
                    lst.append((ip, host))
                    print(f" {host} : {ip}")
                except socket.gaierror:
                    failed.append(host)
    except FileNotFoundError:
        print(f"Error: Filename '{file1}' does not exist in the current directory.")
        return

    if failed:
        print("\nFailed to resolve the following hosts:")
        print("\n".join(failed))

    with open("resolved_hosts.csv", 'w', newline='') as r:
        writer = csv.writer(r, delimiter=",")
        writer.writerows(lst)
