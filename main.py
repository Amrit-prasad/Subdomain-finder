import sys
from subdomain_discovery import find_subdomains
from sorting_validation import remove_invalid_subdomains
from live_domain_checking import main_live_domain_checking

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]

    with open(input_file, "r") as f:
        domains = f.read().splitlines()

    for domain in domains:
        subdomains = find_subdomains(domain)
        valid_subdomains = remove_invalid_subdomains(subdomains)
        main_live_domain_checking(domain, valid_subdomains)
        print(f"Processing for {domain} completed.")

