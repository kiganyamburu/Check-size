# Python Package Size Checker

A Python script to check the size of a Python package from the Python Package Index (PyPI) before installing it and to determine how much free disk space is available on your machine. This can help you decide whether you have enough space to install the package.

## Features

- Get the approximate size of a Python package from PyPI.
- Check available disk space on your machine.
- Compare package size with your system's free space.

## Requirements

- Python 3.x
- `requests` library

## Installation

1. Clone this repository (or download the script directly):

   ```bash
   git clone https://github.com/kiganyamburu/check-size.git
   cd python-package-check-size
   ```

2. Install the required dependencies:
   ```bash
   pip install requests
   ```

## Usage

1. Run the script using Python:

   ```bash
   python main.py
   ```

2. When prompted, enter the name of the Python package you want to check:

   ```
   Enter the Python package name: numpy
   ```

3. The script will display:
   - The approximate size of the package (in MB).
   - The total, used, and free disk space on your machine (in GB).
   - Whether you have enough space to install the specified package.

### Example Output

## How It Works

- **Package Size Check**: Uses the [PyPI JSON API](https://warehouse.pypa.io/api-reference/json.html) to get the metadata of the specified package and calculate its size.
- **Disk Space Check**: Uses Python's built-in `shutil` module to check the total, used, and available disk space on your system.

## Troubleshooting

- If you encounter any issues related to network connectivity, ensure that you are connected to the internet as the script needs access to PyPI.
- If the script fails to find a package, make sure you have entered the correct package name.

## Contributing

Contributions are welcome! If you have any ideas for improvements or new features, feel free to open an issue or submit a pull request.

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-branch
   ```
3. Make your changes and commit them:
   ```bash
   git commit -m "Add new feature"
   ```
4. Push to your branch:
   ```bash
   git push origin feature-branch
   ```
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgements

- [Python Package Index (PyPI)](https://pypi.org/)
- [requests library](https://docs.python-requests.org/)

## Contact

For any questions or feedback, please reach out:

- Email: mburukiganya@gmail.com
- GitHub: [kiganyamburu](https://github.com/kiganyamburu)
