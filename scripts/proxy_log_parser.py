import json

#load Burp Suite Proxy log (exported as JSON)
with open("burp_proxy_log.json", "r") as f:
    proxy_data = json.load(f)

#extract URLs and parameters
for entry in proxy_data:
    try:
        request = entry["request"]
        url = entry["host"] + entry["path"]
        method = request["method"]
        params = request["parameters"]

        print(f"{method} {url} - Params: {params}")
    except KeyError:
        continue

