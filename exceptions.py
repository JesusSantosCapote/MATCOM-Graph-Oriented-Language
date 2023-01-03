class SemanticException(Exception):
    def __init__(self, line, message) -> None:
        self.line = line
        self.message = message

    def __str__(self) -> str:
        return "In line: " + str(self.line) + " " + self.message  