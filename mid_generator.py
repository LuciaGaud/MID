import re
import tkinter as tk
from tkinter import messagebox, ttk

country_codes = [
    ('AF', 'Afghanistan'), ('AX', 'Aland Islands'), ('AL', 'Albania'), ('DZ', 'Algeria'),
    ('AS', 'American Samoa'), ('AD', 'Andorra'), ('AO', 'Angola'), ('AI', 'Anguilla'),
    ('AQ', 'Antarctica'), ('AG', 'Antigua and Barbuda'), ('AR', 'Argentina'), ('AM', 'Armenia'),
    ('AW', 'Aruba'), ('AU', 'Australia'), ('AT', 'Austria'), ('AZ', 'Azerbaijan'),
    ('BS', 'Bahamas'), ('BH', 'Bahrain'), ('BD', 'Bangladesh'), ('BB', 'Barbados'),
    ('BY', 'Belarus'), ('BE', 'Belgium'), ('BZ', 'Belize'), ('BJ', 'Benin'),
    ('BM', 'Bermuda'), ('BT', 'Bhutan'), ('BO', 'Bolivia'), ('BA', 'Bosnia and Herzegovina'),
    ('BW', 'Botswana'), ('BR', 'Brazil'), ('BN', 'Brunei'), ('BG', 'Bulgaria'),
    ('BF', 'Burkina Faso'), ('BI', 'Burundi'), ('KH', 'Cambodia'), ('CM', 'Cameroon'),
    ('CV', 'Cape Verde'), ('KY', 'Cayman Islands'), ('CF', 'Central African Republic'),
    ('TD', 'Chad'), ('CL', 'Chile'), ('CN', 'China'), ('CO', 'Colombia'),
    ('KM', 'Comoros'), ('CG', 'Congo'), ('CD', 'Congo, Democratic Republic'), ('CR', 'Costa Rica'),
    ('CI', "Cote d'Ivoire"), ('HR', 'Croatia'), ('CU', 'Cuba'), ('CY', 'Cyprus'),
    ('CZ', 'Czech Republic'), ('DK', 'Denmark'), ('DJ', 'Djibouti'), ('DM', 'Dominica'),
    ('DO', 'Dominican Republic'), ('EC', 'Ecuador'), ('EG', 'Egypt'), ('SV', 'El Salvador'),
    ('GQ', 'Equatorial Guinea'), ('ER', 'Eritrea'), ('EE', 'Estonia'), ('ET', 'Ethiopia'),
    ('FJ', 'Fiji'), ('FI', 'Finland'), ('FR', 'France'), ('GA', 'Gabon'),
    ('GM', 'Gambia'), ('GE', 'Georgia'), ('DE', 'Germany'), ('GH', 'Ghana'),
    ('GR', 'Greece'), ('GL', 'Greenland'), ('GD', 'Grenada'), ('GU', 'Guam'),
    ('GT', 'Guatemala'), ('GN', 'Guinea'), ('GW', 'Guinea-Bissau'), ('GY', 'Guyana'),
    ('HT', 'Haiti'), ('HN', 'Honduras'), ('HK', 'Hong Kong'), ('HU', 'Hungary'),
    ('IS', 'Iceland'), ('IN', 'India'), ('ID', 'Indonesia'), ('IR', 'Iran'),
    ('IQ', 'Iraq'), ('IE', 'Ireland'), ('IL', 'Israel'), ('IT', 'Italy'),
    ('JM', 'Jamaica'), ('JP', 'Japan'), ('JO', 'Jordan'), ('KZ', 'Kazakhstan'),
    ('KE', 'Kenya'), ('KI', 'Kiribati'), ('KP', 'Korea, North'), ('KR', 'Korea, South'),
    ('KW', 'Kuwait'), ('KG', 'Kyrgyzstan'), ('LA', 'Laos'), ('LV', 'Latvia'),
    ('LB', 'Lebanon'), ('LS', 'Lesotho'), ('LR', 'Liberia'), ('LY', 'Libya'),
    ('LI', 'Liechtenstein'), ('LT', 'Lithuania'), ('LU', 'Luxembourg'), ('MO', 'Macau'),
    ('MK', 'Macedonia'), ('MG', 'Madagascar'), ('MW', 'Malawi'), ('MY', 'Malaysia'),
    ('MV', 'Maldives'), ('ML', 'Mali'), ('MT', 'Malta'), ('MH', 'Marshall Islands'),
    ('MQ', 'Martinique'), ('MR', 'Mauritania'), ('MU', 'Mauritius'), ('MX', 'Mexico'),
    ('FM', 'Micronesia'), ('MD', 'Moldova'), ('MC', 'Monaco'), ('MN', 'Mongolia'),
    ('ME', 'Montenegro'), ('MS', 'Montserrat'), ('MA', 'Morocco'), ('MZ', 'Mozambique'),
    ('MM', 'Myanmar'), ('NA', 'Namibia'), ('NR', 'Nauru'), ('NP', 'Nepal'),
    ('NL', 'Netherlands'), ('NZ', 'New Zealand'), ('NI', 'Nicaragua'), ('NE', 'Niger'),
    ('NG', 'Nigeria'), ('NO', 'Norway'), ('OM', 'Oman'), ('PK', 'Pakistan'),
    ('PW', 'Palau'), ('PA', 'Panama'), ('PG', 'Papua New Guinea'), ('PY', 'Paraguay'),
    ('PE', 'Peru'), ('PH', 'Philippines'), ('PL', 'Poland'), ('PT', 'Portugal'),
    ('QA', 'Qatar'), ('RO', 'Romania'), ('RU', 'Russia'), ('RW', 'Rwanda'),
    ('WS', 'Samoa'), ('SM', 'San Marino'), ('SA', 'Saudi Arabia'), ('SN', 'Senegal'),
    ('RS', 'Serbia'), ('SC', 'Seychelles'), ('SL', 'Sierra Leone'), ('SG', 'Singapore'),
    ('SK', 'Slovakia'), ('SI', 'Slovenia'), ('SB', 'Solomon Islands'), ('SO', 'Somalia'),
    ('ZA', 'South Africa'), ('ES', 'Spain'), ('LK', 'Sri Lanka'), ('SD', 'Sudan'),
    ('SR', 'Suriname'), ('SZ', 'Swaziland'), ('SE', 'Sweden'), ('CH', 'Switzerland'),
    ('SY', 'Syria'), ('TW', 'Taiwan'), ('TJ', 'Tajikistan'), ('TZ', 'Tanzania'),
    ('TH', 'Thailand'), ('TG', 'Togo'), ('TO', 'Tonga'), ('TT', 'Trinidad and Tobago'),
    ('TN', 'Tunisia'), ('TR', 'Turkey'), ('TM', 'Turkmenistan'), ('UG', 'Uganda'),
    ('UA', 'Ukraine'), ('AE', 'United Arab Emirates'), ('GB', 'United Kingdom'),
    ('US', 'United States'), ('UY', 'Uruguay'), ('UZ', 'Uzbekistan'), ('VU', 'Vanuatu'),
    ('VE', 'Venezuela'), ('VN', 'Vietnam'), ('YE', 'Yemen'), ('ZM', 'Zambia'), ('ZW', 'Zimbabwe'),
    ('XA', 'Alberta'), ('XC', 'British Columbia'), ('XM', 'Manitoba'), ('XB', 'New Brunswick'),
    ('XW', 'Newfoundland and Labrador'), ('XT', 'Northwest Territories'), ('XN', 'Nova Scotia'),
    ('XV', 'Nunavut'), ('XO', 'Ontario'), ('XP', 'Prince Edward Island'), ('XQ', 'Quebec'),
    ('XS', 'Saskatchewan'), ('XY', 'Yukon Territory')
]


# Function to get the ISO code from the country name
def get_country_code(country_name):
    for code, name in country_codes:
        if name.lower() == country_name.lower():  # Case-insensitive comparison
            return code
    return None  # If not found

# Searchable
def update_combobox(event):
    typed = combo_iso.get().lower()
    if typed == '':
        combo_iso['values'] = country_names
    else:
        filtered = [name for name in country_names if typed in name.lower()]
        combo_iso['values'] = filtered


# Clean name function to remove unwanted characters and abbreviate certain words
def remove_punctuation(name):
    return re.sub(r'[^\w\s]', '', name)


def filter_common_words(name):
    return re.sub(r'\b(a|an|and|of|the|companha texil|(new)|COMPANHIA TEXTIL|FABRICA DE ARTIGOS DE VESTUARIO|(SUZHOU)|&|(FACTORY)|(SHENZHEN))\b', '', name, flags=re.IGNORECASE)


def abbreviate_words(words):
    return [word[:3].upper() for word in words if len(word) > 1]


def clean_name(name):
    name = remove_punctuation(name)
    name = filter_common_words(name)
    words = name.split()
    cleaned_words = abbreviate_words(words)
    return ''.join(cleaned_words[:2])


# Function to extract the largest number from the address (first 4 digits)
def extract_number(address):
    # Remove hyphens and periods, and replace commas with spaces
    address = address.replace("-", "").replace(".", "").replace(",", " , ")
    
    # Extract numbers from the cleaned address
    numbers = re.findall(r'\d+', address)
    if numbers:
        largest_number = max(numbers, key=int)
        return largest_number[:4]
    return ''


# Function to generate the MID code based on various inputs
def generate_mid(iso, manufacturer_name, address, city):
    country_code = get_country_code(iso)  # Use only the ISO code as the first part
    name_code = clean_name(manufacturer_name)
    number_code = extract_number(address)
    city_code_result = city_code(city)
    mid = f"{country_code}{name_code}{number_code}{city_code_result}"
    return mid[:15]


# Function to extract city code (first 3 letters of city)
def city_code(city):
    city = re.sub(r'[^a-zA-Z]', '', city)
    return city[:3].upper()


# Display the generated MID code in a new window
def display_mid():
    iso = combo_iso.get()
    manufacturer_name = entry_name.get()
    address = entry_address.get()
    city = entry_city.get()

    # Validate that all fields are filled out
    if not iso or not manufacturer_name or not address or not city:
        messagebox.showerror("Error", "All fields are required!")
        return

    # Validate user inputs (optional step for additional validation)
    if not validate_input(manufacturer_name, "Manufacturer Name") or not validate_input(address, "Address") or not validate_input(city, "City"):
        return

    mid_code = generate_mid(iso, manufacturer_name, address, city)
    result_window = tk.Toplevel(app)
    result_window.title("Generated MID")
    mid_label = tk.Entry(result_window, width=30)
    mid_label.insert(0, mid_code)
    mid_label.pack(pady=10)
    mid_label.config(state='readonly')
    mid_label.select_range(0, 'end')
    result_window.clipboard_clear()
    result_window.clipboard_append(mid_code)
    tk.Label(result_window, text="MID code copied to clipboard.").pack()


# Function to validate input (allowing only alphanumeric characters and spaces)
def validate_input(input_text, field_name):
    if not re.match(r'^[a-zA-Z0-9\s,.-]*$', input_text):  # Alphanumeric, spaces, commas, dots, and hyphens
        messagebox.showerror("Invalid Input", f"Invalid characters in {field_name}")
        return False
    return True


# Create the main application window
app = tk.Tk()
app.title("MID Code Generator - by Lucia Gaudioso")
app.geometry("400x300")
app.configure(bg="#f0f0f0")

# Create a dictionary for the country codes and names
country_dict = {name: code for code, name in country_codes}
country_names = [name for _, name in country_codes]

# Dropdown for selecting the country
tk.Label(app, text="Select Country or Provice for Canada:").pack()
combo_iso = ttk.Combobox(app, values=country_names)
combo_iso.current(0)
combo_iso.pack()

# Bind the key release event to update the combobox
combo_iso.bind('<KeyRelease>', update_combobox)

# Entry fields for manufacturer name, address, and city
entry_name = tk.Entry(app)
entry_address = tk.Entry(app)
entry_city = tk.Entry(app)

# Labels for the entry fields
tk.Label(app, text="Manufacturer Name:").pack()
entry_name.pack()
tk.Label(app, text="Address (without post code):").pack()
entry_address.pack()
tk.Label(app, text="City:").pack()
entry_city.pack()

# Button to generate the MID code
tk.Button(app, text="Generate MID", command=display_mid).pack(pady=10)


# Disclaimer
tk.Label(app, text="Please don't use any special characters.\n This script only supports dots, commas,hyphens, letters and numbers.").pack()

app.mainloop()


country_codes = [
    ('AF', 'Afghanistan'), ('AX', 'Aland Islands'), ('AL', 'Albania'), ('DZ', 'Algeria'),
    ('AS', 'American Samoa'), ('AD', 'Andorra'), ('AO', 'Angola'), ('AI', 'Anguilla'),
    ('AQ', 'Antarctica'), ('AG', 'Antigua and Barbuda'), ('AR', 'Argentina'), ('AM', 'Armenia'),
    ('AW', 'Aruba'), ('AU', 'Australia'), ('AT', 'Austria'), ('AZ', 'Azerbaijan'),
    ('BS', 'Bahamas'), ('BH', 'Bahrain'), ('BD', 'Bangladesh'), ('BB', 'Barbados'),
    ('BY', 'Belarus'), ('BE', 'Belgium'), ('BZ', 'Belize'), ('BJ', 'Benin'),
    ('BM', 'Bermuda'), ('BT', 'Bhutan'), ('BO', 'Bolivia'), ('BA', 'Bosnia and Herzegovina'),
    ('BW', 'Botswana'), ('BR', 'Brazil'), ('BN', 'Brunei'), ('BG', 'Bulgaria'),
    ('BF', 'Burkina Faso'), ('BI', 'Burundi'), ('KH', 'Cambodia'), ('CM', 'Cameroon'),
    ('CA', 'Canada'), ('CV', 'Cape Verde'), ('KY', 'Cayman Islands'), ('CF', 'Central African Republic'),
    ('TD', 'Chad'), ('CL', 'Chile'), ('CN', 'China'), ('CO', 'Colombia'),
    ('KM', 'Comoros'), ('CG', 'Congo'), ('CD', 'Congo, Democratic Republic'), ('CR', 'Costa Rica'),
    ('CI', "Cote d'Ivoire"), ('HR', 'Croatia'), ('CU', 'Cuba'), ('CY', 'Cyprus'),
    ('CZ', 'Czech Republic'), ('DK', 'Denmark'), ('DJ', 'Djibouti'), ('DM', 'Dominica'),
    ('DO', 'Dominican Republic'), ('EC', 'Ecuador'), ('EG', 'Egypt'), ('SV', 'El Salvador'),
    ('GQ', 'Equatorial Guinea'), ('ER', 'Eritrea'), ('EE', 'Estonia'), ('ET', 'Ethiopia'),
    ('FJ', 'Fiji'), ('FI', 'Finland'), ('FR', 'France'), ('GA', 'Gabon'),
    ('GM', 'Gambia'), ('GE', 'Georgia'), ('DE', 'Germany'), ('GH', 'Ghana'),
    ('GR', 'Greece'), ('GL', 'Greenland'), ('GD', 'Grenada'), ('GU', 'Guam'),
    ('GT', 'Guatemala'), ('GN', 'Guinea'), ('GW', 'Guinea-Bissau'), ('GY', 'Guyana'),
    ('HT', 'Haiti'), ('HN', 'Honduras'), ('HK', 'Hong Kong'), ('HU', 'Hungary'),
    ('IS', 'Iceland'), ('IN', 'India'), ('ID', 'Indonesia'), ('IR', 'Iran'),
    ('IQ', 'Iraq'), ('IE', 'Ireland'), ('IL', 'Israel'), ('IT', 'Italy'),
    ('JM', 'Jamaica'), ('JP', 'Japan'), ('JO', 'Jordan'), ('KZ', 'Kazakhstan'),
    ('KE', 'Kenya'), ('KI', 'Kiribati'), ('KP', 'Korea, North'), ('KR', 'Korea, South'),
    ('KW', 'Kuwait'), ('KG', 'Kyrgyzstan'), ('LA', 'Laos'), ('LV', 'Latvia'),
    ('LB', 'Lebanon'), ('LS', 'Lesotho'), ('LR', 'Liberia'), ('LY', 'Libya'),
    ('LI', 'Liechtenstein'), ('LT', 'Lithuania'), ('LU', 'Luxembourg'), ('MO', 'Macau'),
    ('MK', 'Macedonia'), ('MG', 'Madagascar'), ('MW', 'Malawi'), ('MY', 'Malaysia'),
    ('MV', 'Maldives'), ('ML', 'Mali'), ('MT', 'Malta'), ('MH', 'Marshall Islands'),
    ('MQ', 'Martinique'), ('MR', 'Mauritania'), ('MU', 'Mauritius'), ('MX', 'Mexico'),
    ('FM', 'Micronesia'), ('MD', 'Moldova'), ('MC', 'Monaco'), ('MN', 'Mongolia'),
    ('ME', 'Montenegro'), ('MS', 'Montserrat'), ('MA', 'Morocco'), ('MZ', 'Mozambique'),
    ('MM', 'Myanmar'), ('NA', 'Namibia'), ('NR', 'Nauru'), ('NP', 'Nepal'),
    ('NL', 'Netherlands'), ('NZ', 'New Zealand'), ('NI', 'Nicaragua'), ('NE', 'Niger'),
    ('NG', 'Nigeria'), ('NO', 'Norway'), ('OM', 'Oman'), ('PK', 'Pakistan'),
    ('PW', 'Palau'), ('PA', 'Panama'), ('PG', 'Papua New Guinea'), ('PY', 'Paraguay'),
    ('PE', 'Peru'), ('PH', 'Philippines'), ('PL', 'Poland'), ('PT', 'Portugal'),
    ('QA', 'Qatar'), ('RO', 'Romania'), ('RU', 'Russia'), ('RW', 'Rwanda'),
    ('WS', 'Samoa'), ('SM', 'San Marino'), ('SA', 'Saudi Arabia'), ('SN', 'Senegal'),
    ('RS', 'Serbia'), ('SC', 'Seychelles'), ('SL', 'Sierra Leone'), ('SG', 'Singapore'),
    ('SK', 'Slovakia'), ('SI', 'Slovenia'), ('SB', 'Solomon Islands'), ('SO', 'Somalia'),
    ('ZA', 'South Africa'), ('ES', 'Spain'), ('LK', 'Sri Lanka'), ('SD', 'Sudan'),
    ('SR', 'Suriname'), ('SZ', 'Swaziland'), ('SE', 'Sweden'), ('CH', 'Switzerland'),
    ('SY', 'Syria'), ('TW', 'Taiwan'), ('TJ', 'Tajikistan'), ('TZ', 'Tanzania'),
    ('TH', 'Thailand'), ('TG', 'Togo'), ('TO', 'Tonga'), ('TT', 'Trinidad and Tobago'),
    ('TN', 'Tunisia'), ('TR', 'Turkey'), ('TM', 'Turkmenistan'), ('UG', 'Uganda'),
    ('UA', 'Ukraine'), ('AE', 'United Arab Emirates'), ('GB', 'United Kingdom'),
    ('US', 'United States'), ('UY', 'Uruguay'), ('UZ', 'Uzbekistan'), ('VU', 'Vanuatu'),
    ('VE', 'Venezuela'), ('VN', 'Vietnam'), ('YE', 'Yemen'), ('ZM', 'Zambia'), ('ZW', 'Zimbabwe'),
    ('XA', 'Alberta'), ('XC', 'British Columbia'), ('XM', 'Manitoba'), ('XB', 'New Brunswick'),
    ('XW', 'Newfoundland and Labrador'), ('XT', 'Northwest Territories'), ('XN', 'Nova Scotia'),
    ('XV', 'Nunavut'), ('XO', 'Ontario'), ('XP', 'Prince Edward Island'), ('XQ', 'Quebec'),
    ('XS', 'Saskatchewan'), ('XY', 'Yukon Territory')
]

