# analyze-domain

A simple tool to automate the process of analyzing any given domain name. Very useful during the recon / enumeration stage.

**_Obviously, do NOT use this tool on any hosts that you are not legally allowed to use. There is minimal risk, but bruteforce style enumeration is still used._**

## What will this tool do?

Right now, this tool does some very simple things.

* First, it will bruteforce subdomains using `amass`
* Then `nslookup` is used to obtain all IP addresses
* `nmap` is then run to check for any open ports on all IPs
* IPs are then correlated back to subdomains to generate the final JSON file

## Prerequisites

You will need to install `amass`, `nslookup` and `nmap`. If you are using something like Kali or Parrot Security, these tools should be preinstalled.

You will need Python 3.

## Running

```bash
# For example: python3 analyze_domain.py junzheng.dev junzheng.dev.result.json
python3 analyze_domain.py <DOMAIN> <OUTPUT_FILE>
```

There is also a nice visualization tool that parses the JSON file and prints out everything in a nice format

```bash
python3 visualize.py <JSON_FILE>
```

## Notes

You probably want to run this tool on some sort of cloud infrastructure. It takes a long time, and residential internet is generally not as stable.
