import json

with open("Stroke/unicode2stroke.json") as f:
    unicode2stroke = json.load(f)


def transfer_to_tradition():
    ...


def get_tradition_character_stroke_count():
    ...


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
    file = f"Auspicious/auspicious_{number}.txt"
    with open(file=file, mode="r", encoding="utf-8") as f:
        auspicious = f.read()
    return auspicious

number = get_number("一","时","欢")
result = get_auspicious(number=number)
print(result)
