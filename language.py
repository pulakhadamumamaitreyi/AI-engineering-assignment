from langdetect import detect

def detect_language(text):

    code = detect(text)

    if code == "hi":
        return "Hindi"

    if code == "ta":
        return "Tamil"

    return "English"
