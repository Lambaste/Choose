import cidr_conv
import ip_lookup
import ip_diff

def choice():
    while True:
        try:
            choose_tool = int(input('''
---Please choose a tool---
CIDR Converter | 1
IP Lookup      | 2
Compare IPs    | 3
Exit           | 0
>> '''))
            if choose_tool == 1:
                cidr_conv.cidr()
            elif choose_tool == 2:
                ip_lookup.look()
            elif choose_tool == 3:
                ip_diff.compare()
            elif choose_tool == 0:
                print("Exiting.")
                break
            else:
                print("Invalid choice. Please enter 1, 2, 3, or 0 to exit.")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    choice()
