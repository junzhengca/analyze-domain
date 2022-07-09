# A Python script to automate domain analyze, it runs various pipelines like
# amass, nslookup, etc...
import os

if len(sys.argv) != 2:
    raise ValueError('Usage: python3 analyze-domain.py <DOMAIN> <WORKSPACE>')

domain = sys.argv[0]
workspace_name = sys.argv[1]
workspace_path = os.path.join(RESULTS_PATH, domain + '-analyze-domain-workspace')

