import json

# Read the configuration file
try:
    with open("config.ini", "r") as config_file:
        config_data = config_file.read()
except FileNotFoundError:
    print("Configuration file not found.")
    exit()
except IOError:
    print("Error reading configuration file.")
    exit()

# Parse the configuration file
config_dict = {}
current_section = ""
for line in config_data.splitlines():
    line = line.strip()
    if line.startswith("["):
        current_section = line.strip("[]")
        config_dict[current_section] = {}
    elif "=" in line:
        key, value = line.split("=", 1)
        config_dict[current_section][key.strip()] = value.strip()

# Save the configuration data as JSON in the database
try:
    with open("config.json", "w") as json_file:
        json.dump(config_dict, json_file, indent=4)
except IOError:
    print("Error writing JSON file.")
    exit()

# Create a GET request to fetch the information
# (This part is not provided as it depends on the specific web framework or library being used)

# Sample output
print("Configuration File Parser Results:")
for section, data in config_dict.items():
    print(section)
    for key, value in data.items():
        print(f"- {key}: {value}")