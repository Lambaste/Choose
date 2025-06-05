# Net Tools

A simple command-line toolkit for network-related tasks. This repository provides three main utilities, all accessible via a unified menu:

- **CIDR Converter**: Expand CIDR notations into lists of IP addresses.
- **IP Lookup**: Resolve hostnames or IPs from a file to their corresponding IP addresses.
- **IP Compare**: Find overlapping IPs between two files.

## Features

- **Interactive Menu**: Select your desired tool from an easy-to-use menu.
- **File-Based Operations**: All tools operate based on file input for batch processing.
- **CSV Output**: Results are saved as CSV files for easy import or sharing.

## Usage

### 1. Clone the Repository

```bash
git clone https://github.com/Lambaste/net-tools.git
cd net-tools
```

### 2. Prepare Your Input Files

- For **CIDR Converter**: Prepare a text file with one CIDR notation per line.
- For **IP Lookup**: Prepare a text file with one hostname or IP per line.
- For **IP Compare**: Prepare two text files, each with one IP per line.

### 3. Launch the Tool

```bash
python choose_tool.py
```

Follow the on-screen prompts to select your desired operation and input files.

---

### Tool Details

#### CIDR Converter

- **Input**: Text file with CIDRs (e.g., `192.168.1.0/24`)
- **Output**: `return.csv` containing all expanded IPs

#### IP Lookup

- **Input**: Text file with hostnames or IPs
- **Output**: `resolved_hosts.csv` with resolved IPs, plus a list of failures (if any)

#### IP Compare

- **Input**: Two text files with IPs (one per line)
- **Output**: `overlap.csv` listing common IPs

---

## Requirements

- Python 3.6+

No external dependencies are required; all modules used are included in the Python standard library.

## File Overview

- `choose_tool.py` – Main menu and entry point
- `cidr_conv.py` – CIDR to IP list conversion
- `ip_lookup.py` – Hostname/IP to IP address resolver
- `ip_diff.py` – Compares lists of IPs for overlaps

## License

This project is licensed under the MIT License.
