from pathlib import Path
from string import Template
class Config:
    UNICODE_STROKE_JSON_PATH = Path("Stroke/unicode2stroke.json")
    AUSPICIOUS_PATH_TEMPLATE = Template("Auspicious/auspicious_$number.txt")