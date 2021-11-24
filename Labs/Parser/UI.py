
from Grammar import Grammar


class UI:

    def __init__(self) -> None:
        self.grammar = Grammar()
    
    def run(self):
        while True:
            print(">>")
            cmd = input()
            if cmd == "0":
                break
            if cmd == "1":
                self.read_grammar()
            if cmd == "2":
                self.print_production_for_non_terminal()
            if cmd == "3":
                self.print_is_cfg()

    def read_grammar(self):
        self.grammar.read_from_file('G1.txt')
        print(self.grammar)
        # print(self.grammar.P)

    def print_production_for_non_terminal(self):
        print("Give non terminal>>")
        non_terminal = input()
        print(self.grammar.get_productions_for(non_terminal))

    def print_is_cfg(self):
        print(self.grammar.is_CFG())

