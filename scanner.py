from token_type import TokenType, Token


class Scanner():
    
    def __init__(self, source:str) -> None:
        self.source = source
        self.tokens = []
        self.start = 0
        self.current = 0
        self.line = 1

        self.fixed_tokens = {
        '+'  :   Token( '+'           , TokenType.plus  ),
        '-'  :   Token( '-'           , TokenType.minus ),
        '*'  :   Token( '*'           , TokenType.star  ),
        '/'  :   Token( '/'           , TokenType.div   ),
        '('  :   Token( '('           , TokenType.opar  ),
        ')'  :   Token( ')'           , TokenType.cpar  ),
        'pi' :   Token( 3.14159265359 , TokenType.num   ),
        'e'  :   Token( 2.71828182846 , TokenType.num   ),
        'phi':   Token( 1.61803398875 , TokenType.num   ),
        }

    
    def scan_tokens(self):
        while not self.is_at_end():
            self.start = self.current
            self.scan_token()

        self.tokens.append(Token(TokenType.eof, '', None, self.line))

    
    def is_at_end(self):
        return self.current >= len(self.source)


    def scan_token(self):
        c = advance()

        self.fixed_tokens[c]

    
    def add_token(self, token_type, literal = None):
        text = self.source[self.start, self.current] #TODO check if the index of the slice are fine
        new_token = Token(token_type, text, literal, self.line)
        self.tokens.append(new_token)
    
