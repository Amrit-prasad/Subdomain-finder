import subprocess
import shutil
import os
import datetime

def run_command(command):
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
        result.check_returncode()
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {command}")
        print(e.stderr)
        sys.exit(1)

def main_live_domain_checking(domain, valid_subdomains):
    output_folder = f"{domain}_output"  # Use the domain name as the folder name
    os.makedirs(output_folder, exist_ok=True)

    output_file = f"{output_folder}/{domain}_valid_subdomains.txt"
    with open(output_file, "w") as f:
        for subdomain in valid_subdomains:
            f.write(subdomain + "\n")

    os.chdir(output_folder)  # Change current working directory to the domain folder

    run_command(f"httpx -l {domain}_valid_subdomains.txt -o {domain}_live_subdomains.txt -silent -status-code -no-color -threads 50 -screenshot")

    # The output folder from httpx will now be created directly within the domain folder

