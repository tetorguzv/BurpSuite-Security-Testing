import itertools

chars = "abc123!@#"

length = 4

#generating all possible payload combinations
payloads = itertools.product(chars, repeat=length)

#save to a file for Burp Suite Intruder
with open("payloads.txt", "w") as f:
    for payload in payloads:
        f.write("".join(payload) + "\n")

print("[+] Payloads generated: payloads.txt")

