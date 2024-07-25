# Python IP Scanner

This is a simple IP scanner implemented in Python 3, allowing you to scan a subnet to find active IP addresses using ICMP ping requests.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This Python script performs an IP scan on a specified subnet to identify active IP addresses. It sends ICMP echo requests (ping) to each IP in the range and checks for responses to determine which hosts are reachable.

## Features

- Scans a specified subnet for active IP addresses.
- Utilizes Python's `subprocess` module to send ICMP echo requests and check responses.
- Displays the list of active IP addresses found during the scan.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/ALBINJoseph01/ip-scanner.git
   ```

2. Navigate into the directory:
   ```
   cd ip-scanner
   ```

3. Run the script:
   ```
   python ip_scanner.py
   ```

## Usage

1. Enter the subnet you want to scan when prompted 
```
Enter the subnet to scan : ("eg:172.16.1")

```

2. The script will start scanning the IP addresses in the specified subnet 
```
Enter the last number :("enter the subset you want like till 10")
```
3. Active IP addresses (hosts responding to ping) will be displayed as they are found.
```
Host 172.16.1.1 is active.
Host 172.16.1.2 is active.
Host 172.16.1.3 is active.
Host 172.16.1.10 is active.
```

4. Once the scan is complete, the script will show the total scan duration and list all active IP addresses.
```
Scan completed in 0:02:20.202412.

Active IP addresses:
172.16.1.1
172.16.1.2
172.16.1.3
172.16.1.10
```
## Contributing

Contributions are welcome! If you find any bugs, have suggestions, or want to improve the script, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
