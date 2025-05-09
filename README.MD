# MID Code Generator

## Overview
The **MID Code Generator** is a Python script that generates a Manufacturers Identification Code (MID) for use in U.S. formal customs entries. The MID is an alternative to the full name and address of a manufacturer, shipper, or exporter, and it is a required field on commercial invoices. 

This script allows you to input information about a manufacturer, including the country, manufacturer name, address, and city. It then generates the MID code, which is used for customs documentation.

## What is the MID Code?
The **MID Code** (Manufacturers Identification Code) is a unique code used in U.S. customs entries as an alternative to a full address. The MID code is always required for U.S. formal customs entries and is used to simplify the customs process by uniquely identifying a manufacturer, shipper, or exporter.

### Key Points:
- The MID code must be displayed on the commercial invoice.
- It is used to identify the manufacturer, shipper, or exporter.
- The MID code is always required for U.S. formal customs entries.

## Features
- **Country Selection:** Choose the country from a dropdown of ISO country codes.
- **Manufacturer Name Cleaning:** The script cleans the manufacturer name by removing punctuation and abbreviating common words.
- **Address Parsing:** The address is parsed to extract the largest number (typically the street number) for the MID code.
- **City Abbreviation:** The city is abbreviated to the first three letters.
- **Generated MID Code:** Displays the generated MID code based on user input.

## How to Use
1. **Install Python:** Ensure you have Python installed on your system.
2. **Install Tkinter:** Tkinter is used for the graphical user interface. It is typically bundled with Python, but if it isn't installed, you can install it using:
   ```bash
   pip install tk