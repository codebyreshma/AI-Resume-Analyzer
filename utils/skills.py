import re

def extract_skills(result, section_name):
    """
    Extracts skills from the AI response.
    Example sections:
    ## Matching Skills
    Python, SQL, Git

    ## Missing Skills
    Docker, AWS
    """

    pattern = rf"{section_name}.*?\n(.*?)(?:\n##|\Z)"

    match = re.search(
        pattern,
        result,
        re.IGNORECASE | re.DOTALL
    )

    if not match:
        return []

    text = match.group(1)

    skills = []

    for item in text.replace("-", "").split(","):
        item = item.strip()

        if item:
            skills.append(item)

    return skills