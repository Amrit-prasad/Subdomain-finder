def remove_invalid_subdomains(subdomains):
    valid_subdomains = []
    for subdomain in subdomains:
        if '*' not in subdomain and '@' not in subdomain and '🔍' not in subdomain and '=' not in subdomain and '>' not in subdomain:
            valid_subdomains.append(subdomain)
    return valid_subdomains

