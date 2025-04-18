import nmap
import sys

def print_scan_results(scanner):
    overall_found = False
    for host in scanner.all_hosts():
        print("Host:", host, "(", scanner[host].hostname(), ")", "Status:", scanner[host].state())
        host_found = False
        for proto in scanner[host].all_protocols():
            print("Protocol:", proto)
            ports = scanner[host][proto].keys()
            for port in sorted(ports):
                port_data = scanner[host][proto][port]
                if port_data['state'] == 'open':
                    details = ""
                    if "script" in port_data:
                        details = " | ".join([f"{name}: {output}" for name, output in port_data["script"].items()])
                    print("Port:", port, "State:", port_data['state'], "Service:", port_data['name'], details)
                    host_found = True
                    overall_found = True
        if not host_found:
            print("No open ports found on this host.")
    if not overall_found:
        print("No open ports found on any scanned hosts.")

def quick_scan(target):
    print("\nPerforming a quick scan on", target, "(common ports)...")
    scanner = nmap.PortScanner()
    scanner.scan(target, arguments='-F')
    print_scan_results(scanner)

def full_scan(target):
    print("\nPerforming a full scan on", target, "(ports 1-1024)...")
    scanner = nmap.PortScanner()
    scanner.scan(target, '1-1024', arguments='-sV')
    print_scan_results(scanner)

def custom_scan(target):
    port_range = input("Enter port range (e.g., 20-1024): ").strip()
    if '-' not in port_range:
        print("Invalid port range format.")
        return
    print("\nPerforming a custom scan on", target, "(ports", port_range + ")...")
    scanner = nmap.PortScanner()
    scanner.scan(target, port_range, arguments='-sV')
    print_scan_results(scanner)

def vulnerability_scan(target):
    print("\nPerforming a vulnerability scan on", target, "(all ports)...")
    scanner = nmap.PortScanner()
    scanner.scan(target, '1-65535', arguments='-sV --script vuln')
    print_scan_results(scanner)

def cli_menu():
    while True:
        print("\nS2 SCANNER CLI Menu")
        print("1. Quick Scan (common ports)")
        print("2. Full Scan (ports 1-1024)")
        print("3. Custom Scan (user-defined port range)")
        print("4. Vulnerability Scan (all ports)")
        print("5. Exit")
        choice = input("Select an option [1-5]: ").strip()
        
        if choice in ["1", "2", "3", "4"]:
            target = input("Enter target IP address or hostname: ").strip()
            if not target:
                print("No target provided, returning to menu.")
                continue
        
        if choice == "1":
            quick_scan(target)
        elif choice == "2":
            full_scan(target)
        elif choice == "3":
            custom_scan(target)
        elif choice == "4":
            vulnerability_scan(target)
        elif choice == "5":
            print("Exiting S2 SCANNER. Goodbye!")
            sys.exit(0)
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    print("Welcome to S2 SCANNER")
    cli_menu()
