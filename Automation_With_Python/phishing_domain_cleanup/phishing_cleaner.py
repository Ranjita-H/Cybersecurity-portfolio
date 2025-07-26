"""
Phishing Domain Cleanup Tool
Author: Ranjita Hukkeri
Description:
Removes malicious phishing domains from a trusted domain allow list using threat intel input.
Logs all actions for audit and troubleshooting purposes.
"""

import os
import logging
from datetime import datetime

# === Configuration ===
TRUSTED_FILE = "trusted_domains.txt"
PHISHING_FILE = "phishing_domains.txt"
BACKUP_FILE = "trusted_domains_backup.txt"
LOG_FILE = "phishing_cleanup.log"

# === Logging Setup ===
logging.basicConfig(
    filename=LOG_FILE,
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def read_domains(file_path):
    """Read domains from a text file into a set, skipping empty lines and comments."""
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
        domains = set(
            line.strip() for line in lines
            if line.strip() and not line.strip().startswith("#")
        )
        logging.info(f"Loaded {len(domains)} domains from {file_path}")
        return domains
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        return set()

def write_domains(file_path, domains):
    """Write domains from a set to a text file, sorted alphabetically."""
    try:
        with open(file_path, "w") as file:
            for domain in sorted(domains):
                file.write(f"{domain}\n")
        logging.info(f"Wrote {len(domains)} domains to {file_path}")
    except Exception as e:
        logging.error(f"Error writing to {file_path}: {e}")

def backup_file(original, backup):
    """Create a backup of the trusted domain file."""
    try:
        if os.path.exists(original):
            os.replace(original, backup)
            logging.info(f"Backup created: {backup}")
        else:
            logging.warning(f"No trusted file found to backup: {original}")
    except Exception as e:
        logging.error(f"Backup failed: {e}")

def remove_phishing_domains():
    """Main logic to remove phishing domains from the trusted domain list."""
    logging.info("=== Starting phishing domain cleanup ===")

    # Load domains
    trusted = read_domains(TRUSTED_FILE)
    phishing = read_domains(PHISHING_FILE)

    if not trusted:
        logging.warning("Trusted domain list is empty or missing.")
        return

    # Backup
    backup_file(TRUSTED_FILE, BACKUP_FILE)

    # Clean trusted list
    cleaned = trusted - phishing
    removed = trusted & phishing

    write_domains(TRUSTED_FILE, cleaned)

    if removed:
        logging.info(f"Removed {len(removed)} phishing domains:")
        for domain in sorted(removed):
            logging.info(f" - {domain}")
    else:
        logging.info("No phishing domains were found in the trusted list.")

    logging.info("=== Cleanup completed ===\n")

if __name__ == "__main__":
    remove_phishing_domains()
