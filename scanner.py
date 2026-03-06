import os

network = input("Enter network (example 192.168.1): ")

print("Scanning network...")

for ip in range(1,255):

    address = f"{network}.{ip}"

    response = os.system(f"ping -c 1 -W 1 {address} > /dev/null")

    if response == 0:
        print(address, "is online")
