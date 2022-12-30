from token_type import TokenType, Token
from dsl_name import DSL


class Scanner():
    
    def __init__(self, source:str) -> None:
        self.source = source
        self.tokens = []
        self.start = 0
        self.current = 0
        self.line = 1

        self.fixed_tokens = {
        '+'  :   self.add_token(TokenType.plus),
        '-'  :   self.add_token(TokenType.minus),
        '*'  :   self.add_token(TokenType.star),
        '/'  :   self.add_token(TokenType.div),
        '('  :   self.add_token(TokenType.opar),
        ')'  :   self.add_token(TokenType.cpar),
        }

    
    def scan_tokens(self):
        while not self.is_at_end():
            self.start = self.current
            self.scan_token()

        self.tokens.append(Token(TokenType.eof, '', None, self.line))

    
    def is_at_end(self):
        return self.current >= len(self.source)


    def scan_token(self):
        c = self.advance()

        try:
            self.fixed_tokens[c]
        except KeyError:
            DSL.error(self.line, "Unexpected character") #TODO check if this work

    
    def add_token(self, token_type, literal = None):
        text = self.source[self.start, self.current] #TODO check if the index of the slice are fine
        new_token = Token(token_type, text, literal, self.line)
        self.tokens.append(new_token)


    def advance(self):
        try:
            self.current += 1
            return self.source[self.current - 1]
        except IndexError:
            return None
    
