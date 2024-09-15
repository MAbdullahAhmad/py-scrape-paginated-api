# Imports

from pathlib import Path
from sys import exit
from datetime import datetime

from lib.curl_to_req import curl_json
from lib.html_2_dict import decode_directory
from lib.save_as_sheet import save_excel

# Settings

verbose = True
file_dir = Path(__file__).parent

# Read cRUL String

try:
    file_path = Path.joinpath(file_dir, 'data/curl_string.txt')
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

for i in range(total_pages):
    if verbose: print("[INFO]: Scraping Page #"+str(i+1))

    response = curl_json(curl_string)
    html_directory = response['resultsHtml']

    scraped_directory += decode_directory(html_directory)

if verbose: print("[INFO]: Scraped Successfully. Exporting ...")


# Export


try:
    filename = f"export_{datetime.now().strftime('%Y_%m_%d__%H_%M_%S_%f')}.xlsx"
    file_path = Path.joinpath(file_dir, 'output', filename)
    save_excel(scraped_directory, file_path)

    if verbose: print("[INFO]: Exported Successfully to file output/"+str(filename))
except:
    if verbose: print("[ERR]: Export failed!")
    exit(1)


print("Completed")
