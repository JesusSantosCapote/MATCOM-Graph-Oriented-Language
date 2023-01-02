from token_type import Token
import re
from exceptions import ScannerError


class Scanner():
    
    def __init__(self, source:str) -> None:
        self.source = source
        self.tokens = []
        self.current = 0
        self.line = 1

        #Each keyword must have its own regular expression(Token Type)
        self._token_regex = r"""(?xm)
        (?P<string> ".*?"         ) |
        (?P<float>  \d+\.\d+      ) |
        (?P<int>    (\d+)         ) |
        (?P<id>     [a-zA-Z_]+\w* ) |
        (?P<plus>   \+            ) |
        (?P<minus>  \-            ) |
        (?P<star>   \*            ) |
        (?P<div>    /             ) |
        (?P<opar>   \(            ) |
        (?P<cpar>   \)            ) |
        (?P<nline>  \n            ) |
        (?P<equal>  =             ) 
        """
        self.regex = re.compile(self._token_regex)

        self.fixed_literals = {
            'string' : lambda x: str(x),
            'float'  : lambda x: float(x),
            'int'    : lambda x: int(x),
        }

        self.re_ws_skip = re.compile('[^ \t\r\f\v]')
        
    
    def get_tokens(self):
        while not self.is_at_end():
            match = self.re_ws_skip.search(self.source, self.current)
            self.current = match.start()

            match = self.regex.match(self.source, self.current)

            if match:
                if match.lastgroup == 'nline':
                    self.line += 1
                    self.current = match.end()
                else:
                    try:
                        literal = self.fixed_literals[match.lastgroup](match[0])
                    except KeyError:
                        literal = None
                    
                    token = Token(match.lastgroup, match[0], literal, self.line)
                    self.tokens.append(token)
                    self.current = match.end()

            else:
                raise ScannerError(self.line)
            

        self.tokens.append(Token('eof', '', None, self.line))

        return self.tokens

    
    def is_at_end(self):
        return self.current >= len(self.source)


# text = """
# x =    -2   + 4 /    2 -   3.0  + 0.83 
# print(hello2)  
# build_graph(x  *2 )

# name = "chuchi"
# """

# scanner = Scanner(text)

# tokens = scanner.get_tokens()

# for tok in tokens:
#     print(tok)