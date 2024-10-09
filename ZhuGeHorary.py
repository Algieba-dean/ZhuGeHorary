import json
from Config import Config

with open(Config.UNICODE_STROKE_JSON_PATH) as f:
    unicode2stroke = json.load(f)

def get_character_stroke_count(char: str):
    unicode = "U+" + str(hex(ord(char)))[2:].upper()
    return int(unicode2stroke[unicode])


def get_number(first: str, second: str, third: str):
    hundreds = get_character_stroke_count(first) % 10
    tens = get_character_stroke_count(second) % 10
    ones = get_character_stroke_count(third) % 10
    number = (hundreds * 100 + tens * 10 + ones) % 384
    return number

def get_auspicious(number:int):
    file = Config.AUSPICIOUS_PATH_TEMPLATE.substitute(number=number)
    with open(file=file, mode="r", encoding="utf-8") as f:
        auspicious = f.read()
    return auspicious

number = get_number(first="彪",second="虎",third="豹")
result = get_auspicious(number=number)
print(result)
