import os

def search_logs_for_ip(ip):
    """Search log files in /var/log for occurrences of a given IP address."""
    
    # Define the directory where log files are located
    log_directory = "/var/log"
    
    # Generate a list of file paths for all files in the log directory, excluding compressed files (.gz)
    files = [os.path.join(dp, f) for dp, dn, filenames in os.walk(log_directory) for f in filenames if not f.endswith('.gz')]

    # Iterate over each file found
    for file in files:
        try:
            # Open the file in read mode with error handling for encoding issues
            with open(file, 'r', errors='ignore') as f:
                # Read the file line by line
                for line in f:
                    # Check if the specified IP address is in the current line
                    if ip in line:
                        # If the IP is found, print the filename and the matching line
                        print(f"[{file}] {line.strip()}")
        except Exception as e:
            # If an error occurs (e.g., file access issues), print an error message with the file name
            print(f"Error reading file {file}: {e}")

if __name__ == "__main__":
    # Prompt the user to input the IP address to search for
    target_ip = input("Input IP Address: ").strip()
    # Check if the user provided an IP address
    if target_ip:
        # Call the function to search logs for the provided IP address
        search_logs_for_ip(target_ip)
    else:
        # Print a message if no IP address was provided
        print("No IP address provided.")
