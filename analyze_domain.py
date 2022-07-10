# A Python script to automate domain analyze, it runs various pipelines like
# amass, nslookup, etc...
import os
import sys
from subdomains import get_all_subdomains
from bulk_nslookup import bulk_nslookup
from bulk_nmap import get_nmap_results
import json

if len(sys.argv) != 3:
    raise ValueError('Usage: python3 analyze_domain.py <DOMAIN> <WORKSPACE>')

domain = sys.argv[1]
workspace_name = sys.argv[2]
workspace_path = os.path.join('.', domain + '-analyze-domain-workspace')

subdomains = get_all_subdomains(domain)
ip_map = bulk_nslookup(subdomains)
ips = []
for host in ip_map:
    ips = ips + ip_map[host]
nmap_results = get_nmap_results(ips)

result_map = {}
for host in ip_map:
    result_map[host] = {}
    for ip in ip_map[host]:
        result_map[host][ip] = nmap_results[ip]

print(result_map)