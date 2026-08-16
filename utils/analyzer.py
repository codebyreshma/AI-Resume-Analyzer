import re

def extract_score(pattern, text, suffix):
    match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)

    if match:
        return match.group(1) + suffix

    return "N/A"