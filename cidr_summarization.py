import tabulate
import netaddr
from netaddr import IPNetwork
iplist =[
    IPNetwork('10.84.238.128/255.255.255.128'),
    IPNetwork('10.84.239.0/255.255.255.128'),
    IPNetwork('10.84.239.128/255.255.255.128'),
    IPNetwork('10.84.234.1')]

print("Length before summarization = ", len(iplist))
summary = netaddr.cidr_merge(iplist)
print("Length after summarization = ", len(summary))
# print(summary)

for item in summary:
    ip_ip = item.ip
    ip_mask = item.netmask
    # prefixlen = IPNetwork(item).prefixlen
    print(ip_ip, ip_mask)
    # print(prefixlen)
