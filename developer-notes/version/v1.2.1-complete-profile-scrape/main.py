# Imports

from pathlib import Path
from sys import exit
from datetime import datetime

from lib.curl_to_req import curl_json, curl_decoded_req, curl_decode
from lib.html_2_dict import decode_directory, decode_info
from lib.save_as_sheet import save_csv
from lib.set_page import set_page

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

for p in range(1, total_pages):
    if verbose: print("[INFO]: Scraping Page #"+str(p))
    curl_string = set_page(curl_string, p)

    response = curl_json(curl_string)
    html_directory = response['resultsHtml']
    directory = decode_directory(html_directory)

    scraped_directory += directory

if verbose: print("[INFO]: Scraped Successfully. Exporting ...")



# Read cRUL String 2

try:
    file_path = Path.joinpath(file_dir, 'data/curl_string_profile.txt')
    curl_string_profile = open(file_path, 'r').read()
    decoded_profile_req = curl_decode(curl_string_profile)

    if verbose: print("[INFO]: Read cURL string successfully")
except:
    if verbose: print("[ERR]: Read cURL string failed")
    exit(1)

# Get more info

total_lawyers = len(scraped_directory)
for i in range(total_lawyers):
    if verbose: print("[INFO]: Detail Scrape #"+str(i+1) + " of " + str(total_lawyers))

    directory = scraped_directory[i]
    decoded_profile_req['url'] = directory['profile_url']

    res = curl_decoded_req(decoded_profile_req)
    info = decode_info(res.text)

    for k in info.keys():
        scraped_directory[i][k] = info[k]


# Export


try:
    filename = f"export_{datetime.now().strftime('%Y_%m_%d__%H_%M_%S_%f')}.csv"
    file_path = Path.joinpath(file_dir, 'output', filename)
    save_csv(scraped_directory, file_path)

    if verbose: print("[INFO]: Exported Successfully to file output/"+str(filename))
except:
    if verbose: print("[ERR]: Export failed!")
    exit(1)


print("Completed")
