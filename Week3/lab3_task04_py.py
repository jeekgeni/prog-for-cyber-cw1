# character analysis and libraries
import random
from datetime import datetime
import socket

def analyse_code(device_code: str) -> None:
    #check indiviudal characters in a device code 
    #process the string one character at a time
    for character in device_code:
        if character.isdigit():
            print(f"Number found: {character}")
        if character.isupper():
            print(f"Uppercase letter found: {character}")
def create_analysis_details() -> None:

    analysis_id = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print("\n--- Analysis Details ---")
    print(f"Analysis ID: {analysis_id}")
    print(f"Timestamp:{timestamp}")

def main() -> None:
    #run the program.

    device_code = "RTR2048gla"
    analyse_code(device_code)
    create_analysis_details()
    ip_address = get_local_ip()

    print("n--- Network Details ---")
    print(f"Local IP address: {ip_address}")
   

def get_local_ip() -> str:

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))

    ip_address = s.getsockname()[0]
    s.close()
    return ip_address

if __name__ == "__main__":
    main()


