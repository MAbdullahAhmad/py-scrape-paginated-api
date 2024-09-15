import requests
import re
import json

def curl_decode(curl_command):
    # Extract the URL
    url_match = re.search(r"curl '([^']+)'", curl_command)
    url = url_match.group(1) if url_match else ""

    # Extract headers
    headers = {}
    header_matches = re.findall(r"-H '([^']+)'", curl_command)
    for header in header_matches:
        key, value = header.split(": ", 1)
        headers[key] = value

    # Extract method (POST or GET)
    method = 'get'  # Default to GET
    if '--data' in curl_command or '--data-raw' in curl_command:
        method = 'post'

    # Extract data (for POST requests)
    data_match = re.search(r"--data-raw '([^']+)'", curl_command) or re.search(r"--data '([^']+)'", curl_command)
    data = data_match.group(1) if data_match else ""

    return {
        "method": method,
        "url": url,
        "headers": headers,
        "data": data,
    }


def curl_req(curl_command):
    req = curl_decode(curl_command)

    if req['method'] == 'get':
        return requests.get(req['url'], headers=req['headers'])
    
    return requests.post(req['url'], headers=req['headers'], data=req['data'])

def curl_res(curl_command):
    response = curl_req(curl_command)
    if response.status_code == 200:
        return response.text
    return None

def curl_json(curl_command):
    text = curl_res(curl_command)

    return json.loads(text)