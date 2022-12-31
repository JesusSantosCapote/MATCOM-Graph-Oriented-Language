class ScannerError(Exception):
    def __init__(self, line) -> None:
        self.line = line