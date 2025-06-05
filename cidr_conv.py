import ipaddress
import sys
import os

def cidr():
    file1 = input("Enter the filename containing the CIDR(s): ").strip()
    lst = []

    try:
        with open(file1) as x:
            for line in x:
                net4 = ipaddress.ip_network(line.strip())
                for i in net4:
                    lst.append(str(i))

    except FileNotFoundError:
        print(f"Error: Filename {file1} does not exist in current directory.")
        return

    except ValueError:
        print("Error: Host bits are set in one of the CIDRs.")
        return

    output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'return.csv')
    print(f"\nThe following IPs have been added to return.csv file in {os.path.dirname(os.path.abspath(__file__))}:\n{', '.join(lst)}")

    with open(output_path, 'w') as f:
        f.write("\n".join(lst))
