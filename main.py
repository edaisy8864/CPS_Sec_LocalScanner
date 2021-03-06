from network.network_scanner import NetworkScanner

def nmap_result_callback(hosts):
    print("scan finished")
    for host in hosts:
        print("Found host", host.ip_address, "with MAC address", host.mac_address)
        print("  ports: ")
        for port in host.ports:
            print("    ", port.port_id, port.protocol, port.service)


scanner = NetworkScanner.create()

network_interfaces = scanner.get_network_interfaces()

print("Found network interfaces:", network_interfaces)

nif = network_interfaces[0]

scanner.scan_network_callback(nif, nmap_result_callback, port_scan=False)
print("Network scan started asynchronously")
print(nif.get_nmap_arg())
