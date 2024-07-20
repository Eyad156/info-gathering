import requests
import socket
import json
import cowsay
cowsay.daemon("Info-Gathering")
def get_server_headers(domain):
    try:
        
        response = requests.get(f'http://{domain}')
        if response.status_code == 200:
            server = response.headers.get('Server', 'Unknown')
            print(f"Server Info: {server}")
        else:
            print(f"Failed to connect to {domain}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

def get_ip_info(ip):
    try:
        response = requests.get(f'https://ipinfo.io/{ip}/json')
        if response.status_code == 200:
            data = response.json()
            print(f"IP Info: {json.dumps(data, indent=2)}")
        else:
            print("Failed to retrieve IP information")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

def main():
    domain = input("Enter website name (e.g., 'google.com') -> ")
    try:
        ip = socket.gethostbyname(domain)
        print(f"IP Address: {ip}")
        
        get_server_headers(domain)
        get_ip_info(ip)
        
    except socket.gaierror:
        print(f"Could not resolve domain: {domain}")

if __name__ == "__main__":
    main()
