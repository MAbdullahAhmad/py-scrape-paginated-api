# Imports

from lib.curl_to_req import curl_json
from lib.html_2_dict import decode_directory
from pathlib import Path
from sys import exit


# Settings

verbose = True


# Read cRUL String

try:
    file_path = Path.joinpath(Path(__file__).parent, 'data/curl_string.txt')
    curl_string = open(file_path, 'r').read()

    if 'page=1' not in curl_string:
        if verbose: print("[ERR]: Please paste accurate url!")
        raise Exception

    if verbose: print("[INFO]: Read cURL string successfully")
except:
    if verbose: print("[ERR]: Read cURL string failed")
    exit(1)


# Test First Contact

total_pages = 0
try:
    response = curl_json(curl_string)
    if bool(response['totalPages']) & bool(response['resultsHtml'].strip()):
        total_pages = response['totalPages']
    if verbose: print("[INFO]: First Contact Successful")
except:
    if verbose: print("[ERR]: First Contact failed")
    exit(1)

print("Total Pages =", total_pages)


# Iterate and scrape directory

scraped_directory = []

for i in range(5):
    if verbose: print("[INFO]: Scraping Page #"+str(i+1))

    response = curl_json(curl_string)
    html_directory = response['resultsHtml']

    scraped_directory += decode_directory(html_directory)


# Print results

print(scraped_directory)

# print()

# response = curl_json(curl_string)

# html_directory = response['resultsHtml']
# directory = decode_directory(html_directory)

# print(directory)