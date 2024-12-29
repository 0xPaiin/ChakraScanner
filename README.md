# OpenEye - A Simple Port Scanning Tool

OpenEye is a lightweight and efficient port scanning tool designed for penetration testers, network administrators, and cybersecurity enthusiasts. It helps users identify open TCP ports on specified hosts. This tool is useful for assessing network vulnerabilities and gathering information about accessible services on a target system.

## Features

- **Multi-Host Scanning**: Scan multiple hosts for open ports on a specific port number.
- **TCP-Based Scanning**: Uses TCP (SOCK_STREAM) for accurate results.
- **Error Handling**: Provides meaningful error messages for unreachable hosts.
- **Lightweight and Simple**: Easy to use with minimal setup.

---

## Usage

### Prerequisites

- Python 3.6 or higher.
- Basic understanding of networking (TCP/UDP).

### Installation

1. Clone or download this repository.
2. Ensure Python is installed on your system.
3. Open a terminal or command prompt and navigate to the tool's directory.

### Running the Tool

1. **Launch the Tool**:
   ```bash
   python openeye.py
   ```

2. **Input Hosts**: When prompted, input a list of hostnames or IP addresses separated by commas (e.g., `192.168.1.1, google.com`).

3. **Input Port**: Enter the port number you want to scan (e.g., `80`).

4. **View Results**: The tool will display the status of the port for each host.

---

## Example

```bash
Enter host addresses (comma-separated): 192.168.1.1, google.com, yahoo.com
Enter port number to scan: 80

Results:
- 192.168.1.1: OPEN
- google.com: OPEN
- yahoo.com: CLOSED
```

---

## Limitations

- Only supports TCP scanning (UDP support not implemented yet).
- Results depend on the network's configuration (e.g., firewalls may block scanning).
- Does not perform advanced vulnerability assessment, only port status.

---

## Disclaimer

This tool is intended for educational purposes and authorized network testing only. Unauthorized use against systems you do not own or have explicit permission to test is illegal and unethical.

---

## License

This project is licensed under the MIT License. See `LICENSE` for more details.

---

## Contribution

Feel free to fork this repository and contribute by submitting pull requests. Suggestions and improvements are always welcome!
