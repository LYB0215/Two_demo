def clean_text(t):
    if not isinstance(t,str):
        return ""
    return t.strip().replace("\n"," ")