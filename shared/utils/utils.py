
import re

def extract_mentions(text):
    return re.findall(r'@(\w+)', text)
