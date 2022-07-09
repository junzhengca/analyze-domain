import os
import sys
import threading
import time
import random
import subprocess

RESULTS_PATH = './results'
NUM_THREADS = 32

if not os.path.isdir(RESULTS_PATH):
    print('Cannot find results directory, creating at', RESULTS_PATH)
    os.mkdir(RESULTS_PATH)
existing_files = os.listdir(RESULTS_PATH)

if len(sys.argv) != 2:
    raise ValueError('Usage: python3 builk-nmap.py <DOMAINS_FILE>')

domains = []
with open(sys.argv[1]) as file:
    # Read all lines from the file and remove trailing \n character
    domains = list(map(lambda x: x.rstrip('\n'), file.readlines()))

thread_lock = threading.Lock()
threads = []
total_domains = len(domains)
completed_domains = []

class NmapThread(threading.Thread):
    def __init__(self, id):
        threading.Thread.__init__(self)
        self.id = id
    
    def run(self):
        while True:
            thread_lock.acquire()
            if len(domains) == 0:
                print(f'Thread {self.id} has no more jobs, exiting...')
                thread_lock.release()
                return
            next_domain = domains.pop(0)
            completed_domains.append(next_domain)
            thread_lock.release()
            print(f'Thread {self.id} processing {next_domain}, ({len(completed_domains)}/{total_domains})')
            result = subprocess.run(["nmap", "-sT", "-p-", "-Pn", next_domain], capture_output=True, encoding='utf-8')
            output_path = os.path.join(RESULTS_PATH, f'{next_domain}.result')
            with open(output_path, 'w') as output_file:
                output_file.write(result.stdout)

for i in range(NUM_THREADS):
    thread = NmapThread(i)
    thread.start()
    threads.append(thread)

for t in threads:
    t.join()

print(f'All jobs finished, check {RESULTS_PATH} for scanning results')