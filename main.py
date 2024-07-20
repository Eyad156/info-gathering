import requests
import socket
import json
import cowsay
import random
from colorama import Fore, Style, init
init(autoreset=True)
colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]
def random_color():
    return random.choice(colors)

cowsay.daemon("Info-Gathering")

def get_server_headers(domain):
    try:
        response = requests.get(f'http://{domain}')
        if response.status_code == 200:
            server = response.headers.get('Server', 'Unknown')
            print(random_color() + f"Server Info: {server}")
        else:
            print(random_color() + f"Failed to connect to {domain}")
    except requests.exceptions.RequestException as e:
        print(random_color() + f"An error occurred: {e}")

def get_ip_info(ip):
    try:
        response = requests.get(f'https://ipinfo.io/{ip}/json')
        if response.status_code == 200:
            data = response.json()
            print(random_color() + f"IP Info: {json.dumps(data, indent=2)}")
        else:
            print(random_color() + "Failed to retrieve IP information")
    except requests.exceptions.RequestException as e:
        print(random_color() + f"An error occurred: {e}")

def main():
    while True:
        domain = input("Enter website name (e.g., 'google.com') -> ")
        if not domain.strip():
            print("Exiting...")
            break
        try:
            ip = socket.gethostbyname(domain)
            print(random_color() + f"IP Address: {ip}")
            
            get_server_headers(domain)
            get_ip_info(ip)
            
        except socket.gaierror:
            print(random_color() + f"Could not resolve domain: {domain}")
        
        continue_choice = input("Press Enter to exit or any other key to continue: ")
        if not continue_choice.strip():
            print("Exiting...")
            break

if __name__ == "__main__":
    main()
