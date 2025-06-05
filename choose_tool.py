import cidr_conv
import ip_lookup
import ip_diff

def choice():
    choose_tool = int(input('''
---Please choose a tool---
CIDR Converter | 1
IP Lookup      | 2
Compare IPs    | 3
>> '''))
    if choose_tool == 1:
        cidr_conv.cider()
    elif choose_tool == 2:
        ip_lookup.look()
    elif choose_tool == 3:
        ip_diff.compare()
             
choice()


