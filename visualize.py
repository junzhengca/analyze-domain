import sys
import json

if len(sys.argv) != 2:
    raise ValueError('Usage: python3 visualize.py <RESULT_FILE>')

result_file = sys.argv[1]

result_map = {}
with open(result_file) as file:
    result_map = json.loads(file.read())

for domain in result_map:
    print(domain)
    for ip in result_map[domain]:
        print('    ' + ip)
        for port in result_map[domain][ip]:
            print('        ' + port['port'] + ' ' + port['status'] + ' ' + port['service'])
    print('') # Python already injects newline automatically