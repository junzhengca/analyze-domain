import threading
import subprocess
import re

NUM_THREADS = 32

class NmapThread(threading.Thread):
    def __init__(self, id, queue, lock, results):
        threading.Thread.__init__(self)
        self.id = id
        self.queue = queue
        self.lock = lock
        self.results = results
    
    def run(self):
        while True:
            self.lock.acquire()
            if len(self.queue) == 0:
                self.lock.release()
                return
            next_host = self.queue.pop(0)
            self.lock.release()
            print(f'Pocessing {next_host}')
            result = subprocess.run([
                "nmap",
                "-sT",
                "-p-",
                "-Pn",
                next_host
            ], capture_output=True, encoding='utf-8')
            result = result.stdout.split('\n')

            self.lock.acquire()
            self.results[next_host] = []
            for line in result:
                if re.match("^[0-9]+.*$", line):
                    line = re.split("\s+", line)
                    self.results[next_host].append({
                        'port': line[0],
                        'status': line[1],
                        'service': line[2],
                    })
            self.lock.release()
            print(f'Finished processing {next_host}')

def get_nmap_results(ips):
    queue = ips[:]
    threads = []
    thread_lock = threading.Lock()
    results = {}
    for i in range(NUM_THREADS):
        thread = NmapThread(i, queue, thread_lock, results)
        thread.start()
        threads.append(thread)
    for t in threads:
        t.join()
    return results
