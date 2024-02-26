**README**

## JIRA Board Data Retrieval In Json Format

This repository contains a Python script for retrieving data from a JIRA board using the 'requests' library.

### Prerequisites

Before running the script, ensure you have the following dependencies installed:

- Python 3.x
- `requests`

You can install the dependencies via pip:

```bash
pip install requests
```

### Configuration

Make sure to update the following information in the script:

- `url`: Your JIRA board URL.
- `auth`: Provide your JIRA login ID and API Key for authentication.

### Usage

1. Clone the repository:

```bash
git clone https://github.com/your-username/jira-board-data-retrieval.git
cd Get_All_Jira_Stories_in_Json
```

2. Update the script `main.py` with your JIRA board URL, login ID, and API Key.

3. Run the Python script `main.py`:

```bash
python main.py
```

### Description

This script sends a GET request to the specified JIRA board URL, authenticating with the provided credentials. It retrieves the data in JSON format and prints it to the console.

### Input

No direct input is required from the user. However, ensure the script is properly configured with the JIRA board URL, login ID, and API Key.

### Output

The script retrieves data from the JIRA board and prints it to the console in JSON format.

### Contributing

Contributions are welcome! If you have suggestions, feature requests, or bug fixes, please feel free to open an issue or create a pull request.

### Acknowledgements

- [requests](https://docs.python-requests.org/en/master/) - HTTP library for Python.
