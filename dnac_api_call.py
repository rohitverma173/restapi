"""
Cisco DNA Center (DNAC) API Integration Module

This module demonstrates how to authenticate with a Cisco DNA Center controller
and retrieve network device information using REST API calls.

Prerequisites:
    - requests library: pip install requests
    - Access to a Cisco DNA Center instance
    - Valid credentials for the DNAC controller

Example:
    This script authenticates to a DNAC controller and retrieves information
    about all Cisco Catalyst 9300 Switch devices, printing their IP addresses
    and MAC addresses.
"""

import requests
from requests.auth import HTTPBasicAuth
import json

# ============================================================================
# STEP 1: AUTHENTICATE WITH DNAC CONTROLLER
# ============================================================================
# URL for DNAC authentication endpoint
# Sandbox: https://sandboxdnac2.cisco.com/dna/system/api/v1/auth/token
# Local/Enterprise: https://172.28.28.74/dna/system/api/v1/auth/token
auth_url = "https://172.28.28.74/dna/system/api/v1/auth/token"

# Authenticate using HTTP Basic Authentication
# Credentials for sandbox: devnetuser / Cisco123!
# Credentials for this instance: admin / Maglev123
auth_response = requests.post(
    auth_url,
    auth=HTTPBasicAuth('admin', 'Maglev123')
)

# Parse the authentication response to extract the token
auth_token_dict = auth_response.json()
auth_token = auth_token_dict['Token']

# ============================================================================
# STEP 2: PREPARE API REQUEST WITH AUTHENTICATION TOKEN
# ============================================================================
# Create headers with the authentication token for subsequent requests
# The x-auth-token header is required for authenticated API calls
headers = {'x-auth-token': auth_token}

# ============================================================================
# STEP 3: QUERY NETWORK DEVICES
# ============================================================================
# URL to retrieve network devices from DNAC
# Sandbox: https://sandboxdnac2.cisco.com/dna/intent/api/v1/network-device
# Local/Enterprise: https://172.28.28.74/dna/system/api/v1/auth/token
device_url = "https://172.28.28.74/dna/system/api/v1/auth/token"

# Filter parameters to search for specific device types
# In this case, we're filtering for Cisco Catalyst 9300 Switch devices
device_filter = {'type': "Cisco Catalyst 9300 Switch"}

# Make GET request with authentication header and filter parameters
device_response = requests.get(
    device_url,
    headers=headers,
    params=device_filter
)

# Parse the API response to JSON dictionary
devices = device_response.json()

# ============================================================================
# STEP 4: EXTRACT AND DISPLAY DEVICE INFORMATION
# ============================================================================
# Iterate through the returned devices and print their IP and MAC addresses
print("Cisco Catalyst 9300 Switch Devices:")
print("-" * 50)

device_count = 0
while device_count < len(devices['response']):
    device = devices['response'][device_count]
    mac_address = device['macAddress']
    management_ip = device['managementIpAddress']

    print(f"IP: {management_ip} | MAC: {mac_address}")
    device_count += 1

print("-" * 50)
print(f"Total devices found: {device_count}")

