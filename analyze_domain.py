# A Python script to automate domain analyze, it runs various pipelines like
# amass, nslookup, etc...
import os
import sys
from subdomains import get_all_subdomains
from bulk_nslookup import bulk_nslookup
from bulk_nmap import get_nmap_results
import json

if len(sys.argv) != 3:
    raise ValueError('Usage: python3 analyze_domain.py <DOMAIN> <OUTPUT_FILE>')

domain = sys.argv[1]
output_path = sys.argv[2]

print('Getting all subdomains...')
subdomains = get_all_subdomains(domain)
print('Resolving domains to IPs...')
ip_map = bulk_nslookup(subdomains)
ips = []
for host in ip_map:
    ips = ips + ip_map[host]
print('Running nmap scripts...')
nmap_results = get_nmap_results(ips)

result_map = {}
for host in ip_map:
    result_map[host] = {}
    for ip in ip_map[host]:
        result_map[host][ip] = nmap_results[ip]

with open(output_path, 'w') as output_file:
    output_file.write(json.dumps(result_map))

print('\n\n=================================================\n')
for domain in subdomains:
    print(domain)
    for ip in result_map[domain]:
        print('    ' + ip)
        for port in result_map[domain][ip]:
            print('        ' + port['port'] + ' ' + port['status'] + ' ' + port['service'])
    print('') # Python already injects newline automatically