from enum import Enum

TokenType = Enum('TokenType', 'eof num plus minus star div opar cpar id')

class Token():

    def __init__(self, token_type, lexeme, literal, line_number) -> None:
        self.token_type = token_type
        self.lexeme = lexeme
        self.literal = literal
        self.line_number = line_number

    def __str__(self) -> str:
        return f"Token of Type:{self.token_type}, Lexeme:{self.lexeme}, Literal:{self.literal} at {self.line_number}"       