from lib.curl_to_req import curl_json

response = curl_json("""curl 'https://www.eb5investors.com/wp-admin/admin-ajax.php?action=perform_directory_search&state=&language=&title=&type=immigration-attorneys&page=1' \
  -H 'accept: */*' \
  -H 'accept-language: en-US,en;q=0.9' \
  -H 'cookie: cookieyes-consent=consentid:T1RXdG96c0dpMnNRdzVNRmlYYThzQmNQMjQ5RTRMS0I,consent:no,action:,necessary:yes,functional:no,analytics:no,performance:no,advertisement:no,other:no; lhnRefresh=98351486-ad32-4326-8f61-30f6c3644a34; lhnRefresh=98351486-ad32-4326-8f61-30f6c3644a34; lhnJWT=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJ2aXNpdG9yIiwiZG9tYWluIjoiIiwiZXhwIjoxNzI2NTIxNDI3LCJpYXQiOjE3MjY0MzUwMjcsImlzcyI6eyJhcHAiOiJqc19zZGsiLCJjbGllbnQiOjI1NjE1LCJjbGllbnRfbGV2ZWwiOiJlbnRlcnByaXNlIiwibGhueF9mZWF0dXJlcyI6W10sInZpc2l0b3JfdHJhY2tpbmciOnRydWV9LCJqdGkiOiJhNzZjZTVlMC1lYjM4LTQ0ZGQtYjkzMC0zZmU3MWJhMmE3ZGEiLCJyZXNvdXJjZSI6eyJpZCI6ImE3NmNlNWUwLWViMzgtNDRkZC1iOTMwLTNmZTcxYmEyYTdkYS0yNTYxNS02bnN0WTNLIiwidHlwZSI6IkVsaXhpci5MaG5EYi5Nb2RlbC5Db3JlLlZpc2l0b3IifX0.KitNSyz9z-RoakyFk_5-4osvoY3mdDE2WFZcPyjBBSI; lhnJWT=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJ2aXNpdG9yIiwiZG9tYWluIjoiIiwiZXhwIjoxNzI2NTIxNDI3LCJpYXQiOjE3MjY0MzUwMjcsImlzcyI6eyJhcHAiOiJqc19zZGsiLCJjbGllbnQiOjI1NjE1LCJjbGllbnRfbGV2ZWwiOiJlbnRlcnByaXNlIiwibGhueF9mZWF0dXJlcyI6W10sInZpc2l0b3JfdHJhY2tpbmciOnRydWV9LCJqdGkiOiJhNzZjZTVlMC1lYjM4LTQ0ZGQtYjkzMC0zZmU3MWJhMmE3ZGEiLCJyZXNvdXJjZSI6eyJpZCI6ImE3NmNlNWUwLWViMzgtNDRkZC1iOTMwLTNmZTcxYmEyYTdkYS0yNTYxNS02bnN0WTNLIiwidHlwZSI6IkVsaXhpci5MaG5EYi5Nb2RlbC5Db3JlLlZpc2l0b3IifX0.KitNSyz9z-RoakyFk_5-4osvoY3mdDE2WFZcPyjBBSI; lhnContact=a76ce5e0-eb38-44dd-b930-3fe71ba2a7da-25615-6nstY3K; lhnContact=a76ce5e0-eb38-44dd-b930-3fe71ba2a7da-25615-6nstY3K; lhnAutoInviteShown=true; lhnAutoInviteShown=true' \
  -H 'priority: u=1, i' \
  -H 'referer: https://www.eb5investors.com/directories/immigration-attorneys/' \
  -H 'sec-ch-ua: "Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Linux"' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: same-origin' \
  -H 'user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36' \
  -H 'x-requested-with: XMLHttpRequest'
""")

print(response['resultsHtml'])