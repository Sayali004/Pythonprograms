
server_ip = ("192", "168", "1", "1")
allowed_ips = ["192.168.1.10", "192.168.1.20"] 

def update_allowed_ips():
    print("\nCurrent allowed IPs:", allowed_ips)
    ip = input("Enter new IP to allow: ")
    if ip not in allowed_ips:
        allowed_ips.append(ip)
        print("IP added to allowed list.")
    else:
        print("IP is already in the allowed list.")

def display_config():
    print("\n--- Server Configuration ---")
    print("Server IP (unchangeable):", ".".join(server_ip))
    print("Allowed IPs:", allowed_ips)

def try_to_change_server_ip():
    try:
        server_ip[0] = "10"
    except TypeError:
        print("\nError: Cannot modify server_ip. It is a tuple and immutable!")

while True:
    print("\nWeb Server Configuration Menu:")
    print("1. Display Configuration")
    print("2. Add Allowed IP")
    print("3. Try to Modify Server IP (Should Fail)")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        display_config()
    elif choice == '2':
        update_allowed_ips()
    elif choice == '3':
        try_to_change_server_ip()
    elif choice == '4':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please enter between 1 and 4.")
