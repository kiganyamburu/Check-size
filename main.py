import requests
import shutil
import json

def get_package_size(package_name):
    """Get the approximate size of a Python package from PyPI."""
    try:
        # Get package information from PyPI
        response = requests.get(f"https://pypi.org/pypi/{package_name}/json")
        response.raise_for_status()  # Raise an error for bad responses (like 404)
        package_data = response.json()

        # Get the URL for the latest version of the package
        urls = package_data['urls']
        if not urls:
            print(f"No downloadable files found for {package_name}.")
            return None
        
        # Calculate the total size of all downloadable files
        total_size = sum(file['size'] for file in urls if 'size' in file)
        
        # Convert size to a more readable format (bytes to MB)
        total_size_mb = total_size / (1024 * 1024)
        return total_size_mb

    except requests.exceptions.RequestException as e:
        print(f"Error fetching package information: {e}")
        return None


def check_disk_space():
    """Check the available disk space on the system."""
    total, used, free = shutil.disk_usage("/")
    
    # Convert bytes to GB for a more readable format
    total_gb = total / (1024**3)
    used_gb = used / (1024**3)
    free_gb = free / (1024**3)
    
    return total_gb, used_gb, free_gb


if __name__ == "__main__":
    # Get package name from user
    package_name = input("Enter the Python package name: ")
    
    # Check the size of the package
    package_size = get_package_size(package_name)
    if package_size is not None:
        print(f"\nApproximate size of '{package_name}' package: {package_size:.2f} MB")

    # Check the disk space
    total_gb, used_gb, free_gb = check_disk_space()
    print(f"\nDisk Space Information:")
    print(f"  Total space: {total_gb:.2f} GB")
    print(f"  Used space: {used_gb:.2f} GB")
    print(f"  Free space: {free_gb:.2f} GB")

    # Compare package size with available space (if package size is known)
    if package_size is not None:
        if package_size / 1024 < free_gb:
            print(f"\nYou have enough space to install the '{package_name}' package.")
        else:
            print(f"\nYou do NOT have enough space to install the '{package_name}' package.")
