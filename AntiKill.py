import os
from pymal import Scanner

def scan_directory(directory):
    scanner = Scanner()
    scanner.load_yara_rules("malware_signature.yar")
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            result = scanner.scan_file(filepath)
            if result:
                print("Malware detected: ", filepath)
            else:
                print("File is clean: ", filepath)
                
if __name__ == "__main__":
    scan_directory("/path/to/directory")
