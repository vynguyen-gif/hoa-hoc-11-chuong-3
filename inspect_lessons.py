import re
import json

with open("index.html", encoding="utf-8") as f:
    text = f.read()

# Find lessons list
matches = re.findall(r'id:\s*"([^"]+)",\s*title:\s*"([^"]+)"', text)
for m in matches:
    print(m[0], "-->", m[1])
