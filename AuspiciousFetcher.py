import json

import requests
import re
from pathlib import Path


def get_auspicious(number: int):
    url = f"https://www.ttlingqian.com/zhuge/{number}.html"
    response = requests.get(url=url)
    content = response.content.decode("utf-8")
    pattern = r"<meta name=\"description\" content=\"(.*)\" />"
    auspicious = re.findall(pattern=pattern, string=content)[0]
    file = Path(f"Auspicious/auspicious_{number}.txt")
    with open(file=file, encoding="utf-8", mode="w") as f:
        print(f"第{number}卦:\t{auspicious}")
        f.write(auspicious)
    ...


total = 384
for num in range(total):
    number = num + 1
    get_auspicious(number=number)
    ...

file = Path("Stroke/Unihan_IRGSources.txt")
output = Path("Stroke/unicode2stroke.json")
stroke_dict = dict()
with open(file,mode="r") as f:
    for line in f:
        raw_line = line.strip()
        pattern = r"(U\+.*)\skTotalStrokes.*\s(\d+)"
        result = re.findall(pattern=pattern, string=raw_line)
        if len(result) == 0:
            continue
        unicode_key = result[0][0]
        unicode_stroke = result[0][1]
        print(f"{unicode_key}: {unicode_stroke}")
        stroke_dict[unicode_key] = unicode_stroke

with open(file=output, mode="w", encoding="utf-8") as f:
    json.dump(stroke_dict,f, ensure_ascii=False, indent=4)
