import re


def extract_keywords(job_description):

    words = re.findall(r"\b[A-Za-z][A-Za-z0-9+#.-]*\b", job_description)

    stop_words = {
        "the", "and", "for", "with", "this", "that", "you",
        "your", "will", "are", "our", "have", "has", "from",
        "into", "using", "must", "should", "job", "role",
        "years", "experience", "required", "preferred", "work"
    }

    keywords = []

    for word in words:

        word = word.lower()

        if len(word) > 2 and word not in stop_words:
            keywords.append(word)

    return sorted(set(keywords))


def compare_keywords(resume_text, job_description):

    resume = resume_text.lower()

    keywords = extract_keywords(job_description)

    matched = []

    missing = []

    for keyword in keywords:

        if keyword in resume:
            matched.append(keyword)
        else:
            missing.append(keyword)

    return matched, missing