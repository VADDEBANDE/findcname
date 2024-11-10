import dns.resolver
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def get_cname(domain):
    try:
        answers = dns.resolver.resolve(domain, 'CNAME')
        for rdata in answers:
            return rdata.target.to_text()
    except dns.resolver.NoAnswer:
        return "No CNAME record found"
    except dns.resolver.NXDOMAIN:
        return "Domain does not exist"
    except Exception as e:
        return f"Error retrieving CNAME: {e}"

def process_domains(file_path):
    try:
        with open(file_path, 'r') as file:
            domains = file.readlines()
        
        for domain in domains:
            domain = domain.strip()
            cname = get_cname(domain)
            
            # Print CNAME in green if found, else print normally
            if "Error" not in cname and "No CNAME" not in cname and "Domain does not exist" not in cname:
                print(f"Domain: {domain}, CNAME: {Fore.GREEN}{cname}{Style.RESET_ALL}")
            else:
                print(f"Domain: {domain}, CNAME: {cname}")
                
    except FileNotFoundError:
        print(f"File {file_path} not found.")
    except Exception as e:
        print(f"Error processing file: {e}")

if __name__ == "__main__":
    file_path = input("Enter the file path containing the list of domains: ")
    process_domains(file_path)
