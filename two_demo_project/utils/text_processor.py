class TextProcessor:
    def __init__(self,min_len):
        self.min_len = min_len

    def clean_text(self,text):
        cleaned = text.strip().replace("\n","")
        return cleaned
    def is_valid(self,text):
        cleaned = self.clean_text(text)
        return len(cleaned) >= self.min_len