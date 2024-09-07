# DNS Query Script

This script creates and sends a DNS query to a specified DNS server and then forwards the response to a target IP address. It is intended for educational purposes and network diagnostics.

## Features

- Constructs a DNS query for a given domain.
- Sends the DNS query to a specified DNS server.
- Forwards the DNS server's response to a target IP address.
- Validates IP addresses.
- Handles socket timeouts and errors.
- Logs activities and errors to a log file.

## Prerequisites

- Python 3.x

## Usage

1. Clone the repository or download the script.
2. Ensure you have Python 3.x installed on your machine.
3. Modify the [`target_ip`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Ffelipemourao%2FDocuments%2FDeveloper%2Fgilgamesh%2Fmain.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A26%2C%22character%22%3A27%7D%7D%5D%2C%220b27138b-5e02-440d-a50f-cec2acace4dd%22%5D "Go to definition"), [`dns_server`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Ffelipemourao%2FDocuments%2FDeveloper%2Fgilgamesh%2Fmain.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A26%2C%22character%22%3A38%7D%7D%5D%2C%220b27138b-5e02-440d-a50f-cec2acace4dd%22%5D "Go to definition"), and [`domain`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Ffelipemourao%2FDocuments%2FDeveloper%2Fgilgamesh%2Fmain.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A5%2C%22character%22%3A21%7D%7D%5D%2C%220b27138b-5e02-440d-a50f-cec2acace4dd%22%5D "Go to definition") variables in the script as needed.
4. Run the script using the following command:

```bash
python main.py
```

## Code Overview

### [`create_dns_query(domain)`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Ffelipemourao%2FDocuments%2FDeveloper%2Fgilgamesh%2Fmain.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A5%2C%22character%22%3A4%7D%7D%5D%2C%220b27138b-5e02-440d-a50f-cec2acace4dd%22%5D "Go to definition")

This function constructs a DNS query for a given domain.

- **Parameters**:
  - [`domain`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Ffelipemourao%2FDocuments%2FDeveloper%2Fgilgamesh%2Fmain.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A5%2C%22character%22%3A21%7D%7D%5D%2C%220b27138b-5e02-440d-a50f-cec2acace4dd%22%5D "Go to definition") (str): The domain name to query.

- **Returns**:
  - [`bytes`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Ffelipemourao%2FDocuments%2FDeveloper%2Fgilgamesh%2Fmain.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A13%2C%22character%22%3A27%7D%7D%5D%2C%220b27138b-5e02-440d-a50f-cec2acace4dd%22%5D "Go to definition"): The constructed DNS query.

### [`is_valid_ip(ip)`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Ffelipemourao%2FDocuments%2FDeveloper%2Fgilgamesh%2Fmain.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A19%2C%22character%22%3A4%7D%7D%5D%2C%220b27138b-5e02-440d-a50f-cec2acace4dd%22%5D "Go to definition")

This function checks if a given IP address is valid.

- **Parameters**:
  - [`ip`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Ffelipemourao%2FDocuments%2FDeveloper%2Fgilgamesh%2Fmain.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A19%2C%22character%22%3A16%7D%7D%5D%2C%220b27138b-5e02-440d-a50f-cec2acace4dd%22%5D "Go to definition") (str): The IP address to validate.

- **Returns**:
  - `bool`: [`True`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Ffelipemourao%2FDocuments%2FDeveloper%2Fgilgamesh%2Fmain.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A22%2C%22character%22%3A15%7D%7D%5D%2C%220b27138b-5e02-440d-a50f-cec2acace4dd%22%5D "Go to definition") if the IP address is valid, [`False`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Ffelipemourao%2FDocuments%2FDeveloper%2Fgilgamesh%2Fmain.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A24%2C%22character%22%3A15%7D%7D%5D%2C%220b27138b-5e02-440d-a50f-cec2acace4dd%22%5D "Go to definition") otherwise.

### [`send_amplified_request(target_ip, dns_server, domain)`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Ffelipemourao%2FDocuments%2FDeveloper%2Fgilgamesh%2Fmain.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A26%2C%22character%22%3A4%7D%7D%5D%2C%220b27138b-5e02-440d-a50f-cec2acace4dd%22%5D "Go to definition")

This function sends a DNS query to a DNS server and forwards the response to a target IP.

- **Parameters**:
  - [`target_ip`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Ffelipemourao%2FDocuments%2FDeveloper%2Fgilgamesh%2Fmain.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A26%2C%22character%22%3A27%7D%7D%5D%2C%220b27138b-5e02-440d-a50f-cec2acace4dd%22%5D "Go to definition") (str): The IP address of the target.
  - [`dns_server`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Ffelipemourao%2FDocuments%2FDeveloper%2Fgilgamesh%2Fmain.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A26%2C%22character%22%3A38%7D%7D%5D%2C%220b27138b-5e02-440d-a50f-cec2acace4dd%22%5D "Go to definition") (str): The IP address of the DNS server.
  - [`domain`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Ffelipemourao%2FDocuments%2FDeveloper%2Fgilgamesh%2Fmain.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A5%2C%22character%22%3A21%7D%7D%5D%2C%220b27138b-5e02-440d-a50f-cec2acace4dd%22%5D "Go to definition") (str): The domain name to query.

- **Exceptions**:
  - Handles socket timeouts, general socket errors, and other exceptions.

### Example

```python
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, filename='dns.log', filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')

    target_ip = "192.0.2.1"  # IP address of the target
    dns_server = "8.8.8.8"  # Public DNS server (Google DNS)
    domain = "example.com"  # Domain to query

    send_amplified_request(target_ip, dns_server, domain)
```

## Important Notes

- **Ethical Use**: Ensure the code is used for legitimate purposes, such as network diagnostics or educational purposes.
- **Security Concerns**: Be aware that misuse of this script can lead to DNS amplification attacks, which are illegal and unethical.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Contact

For any questions or concerns, please open an issue in the repository.

---

**Disclaimer**: This script is intended for educational purposes only. The author is not responsible for any misuse of this script.
