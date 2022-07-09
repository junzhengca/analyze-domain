import subprocess

def get_all_subdomains(domain):
    result = subprocess.run([
        "amass",
        "enum",
        "-brute",
        "-w",
        './wordlists/subdomains-top1million-5000.txt',
        '-d',
        domain
    ], capture_output=True, encoding='utf-8')

    domains = result.stdout.split('\n')
    while("" in domains): domains.remove("")

    return domains
