import re
import subprocess

def bulk_nslookup(domains):
    ip_dict = {}
    for domain in domains:
        ip_dict[domain] = []
        result = subprocess.run([
            "nslookup", domain
        ], capture_output=True, encoding='utf-8')
        result = result.stdout.split("Non-authoritative answer:")
        if len(result) == 2:
            result = result[1]
            result = result.split('\n')
            for line in result:
                if re.match("Address: .*", line):
                    line = line.split(' ')
                    ip_dict[domain].append(line[1])
    return ip_dict
