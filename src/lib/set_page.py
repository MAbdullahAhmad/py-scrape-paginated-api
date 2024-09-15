def set_page(curl_string, n):
    return curl_string.replace('&page=1', '&page='+n)