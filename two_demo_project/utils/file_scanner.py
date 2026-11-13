from pathlib import Path

class FileScanner:
    def __init__(self, root_path):
        self.root = Path(root_path)
    
    def is_valid(self):
        return self.root.exists() and self.root.is_dir()
    def scan(self, pattern="*.txt"):
        return list(self.root.rglob(pattern))
