import subprocess
import re
import sys

def run_command(command):
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
        result.check_returncode()
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {command}")
        print(e.stderr)
        sys.exit(1)

def find_subdomains(domain):
    subdomains = set()

    # Using subfinder
    subfinder_output = run_command(f"subfinder -d {domain}")
    subdomains.update(subfinder_output.splitlines())

    # Using assetfinder
    assetfinder_output = run_command(f"assetfinder --subs-only {domain}")
    subdomains.update(assetfinder_output.splitlines())

    # Using findomain
    findomain_output = run_command(f"findomain -t {domain}")
    subdomains.update(findomain_output.splitlines())

    # Using crt.sh
    crtsh_output = run_command(f'curl -s "https://crt.sh/?q=%25.{domain}&output=json" | jq -r \'.[].name_value\' | sed \'s/\\*\\.//g\' | sort -u')
    subdomains.update(crtsh_output.splitlines())

    # Using nmap
    nmap_output = run_command(f"nmap --script hostmap-crtsh.nse {domain}")
    subdomain_pattern = r'(?<=\n| )([a-zA-Z0-9.-]+\.{0})'.format(domain)
    subdomains.update(re.findall(subdomain_pattern, nmap_output))

    # Running waybackurls
    waybackurls_output = run_command(f"waybackurls {domain}")
    with open(f"{domain}_waybackurls.txt", "w") as f:
        f.write(waybackurls_output)

    return subdomains

