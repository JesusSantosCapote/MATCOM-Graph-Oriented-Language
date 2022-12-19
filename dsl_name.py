import sys

class DSL:

    had_error = False

    def main(self, file_name = None):
        if file_name != None:
            self.run_file(file_name)

        else:
            self.run_prompt()


    def run_file(self, file_name):
        code = ""
        with open(file_name) as file:
            code = file.read()
        file.close()

        self.run(code)
        
        if self.had_error: print("The code had errors") #TODO: Think a better form to do this


    def run_prompt(self):
        while True:
            try:
                line = input(">>> ")
            except EOFError:
                break
            self.run(line)
            self.had_error = False

    
    def run(source):
        scanner = Scanner(source)
        tokens = scanner.get_tokens()

        #for now only print
        for tok in tokens:
            print(tok)


    def error(self, line_number, message):
        self.report(self, line_number, "", message)


    def report(self, line_number, where, message):
        print("[line " + line_number + "] Error" + where + ": " + message)
        self.had_error = True

