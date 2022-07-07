import sys
import subprocess
import re

if len(sys.argv) != 3:
    raise ValueError('Usage: python3 builk-nslookup.py <DOMAINS_FILE> <OUTPUT_FILE>')

domains = []
with open(sys.argv[1]) as file:
    # Read all lines from the file and remove trailing \n character
    domains = list(map(lambda x: x.rstrip('\n'), file.readlines()))

mapped = ""
ips = ""

for domain in domains:
    result = subprocess.run(["nslookup", domain], capture_output=True, encoding='utf-8')
    mapped += (domain + '==========================================\n')
    result = result.stdout.split("Non-authoritative answer:")
    if len(result) == 2:
        result = result[1]
        result = result.split('\n')
        for line in result:
            if re.match("Address: .*", line):
                line = line.split(' ')
                mapped += line[1] + '\n'
                ips += line[1] + '\n'

with open(sys.argv[2], 'w') as output:
    output.write(mapped + '\n************************STARTING IP BLOCK ************************\n' + ips)