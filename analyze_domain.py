# A Python script to automate domain analyze, it runs various pipelines like
# amass, nslookup, etc...
import os
import sys
from subdomains import get_all_subdomains
from bulk_nslookup import bulk_nslookup

if len(sys.argv) != 3:
    raise ValueError('Usage: python3 analyze_domain.py <DOMAIN> <WORKSPACE>')

domain = sys.argv[1]
workspace_name = sys.argv[2]
workspace_path = os.path.join('.', domain + '-analyze-domain-workspace')

subdomains = get_all_subdomains(domain)
ip_map = bulk_nslookup(subdomains)