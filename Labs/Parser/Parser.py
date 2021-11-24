from Grammar import Grammar

class RecursiveDescentParser:

    def __init__(self, grammar_file_name):
        self.grammar = Grammar()
        self.grammar.read_from_file(grammar_file_name)

        self.state = 'q' #s
        self.index = 1 #i - position of current symbol in input sequence
        self.working_stack = [] #alpha - working stack, stores the way the parse is build
        # beta - input stack, part of the tree to be built
        self.input_stack = [self.grammar.S] # ['S'], ['a', 'S', 'b', 'S', 'b', 'S']
        self.tree = []

    def expand(self):
        # when: head of input stack is a non terminal
        # (q, i, alpha, A beta) ⊢ (q, i, alpha A1, gamma1 beta)
        print("expand")
        non_terminal = self.input_stack.pop(0) # pop A from beta
        self.working_stack.append( (non_terminal, 0) ) # alpha -> alpha A1
        productions = self.grammar.get_productions_for(non_terminal) #[('a B', 1), ('b A', 2)] # gamma1
        current_production = productions[0][0] #('a B', 1) -> ['a B']

        self.concatenate_production_to_stack(current_production)

    def concatenate_production_to_stack(self, current_production):
        to_concatenate = []
        for symbol in current_production:
            to_concatenate += [symbol]
        self.input_stack = to_concatenate + self.input_stack

    def advance(self):
        # when: head of input stack is a terminal = current symbol from input
        # (q, i, alpha, a_i beta) ⊢ (q, i+1, alpha a_i, beta)
        print("advance")
        self.index += 1 # i = i+1
        a_i = self.input_stack.pop(0) #get a_i from beta
        self.working_stack.append(a_i) #append a_i to alpha

    def momentary_insuccess(self):
        # when: head of input stack is a terminal != current symbol from input
        print("momentary insuccess")
        self.state = 'b'

    def back(self):
        # when: head of working stack is a terminal
        # (b, i, alpha a, beta) ⊢ (b, i-1, alpha, a beta)
        print("back")
        self.index -= 1 # i = i-1
        top_of_working_stack = self.working_stack.pop() # a from alpha a
        self.input_stack = [top_of_working_stack] + self.input_stack # beta -> a + beta

    def another_try(self):
        print("another try")
        last = self.working_stack.pop()  # (symbol, production_nr)
        # print(last) #('B', 1)
        current_symbol = last[0]
        current_index = last[1]
        if last[1] + 1 < len(self.grammar.get_productions_for(last[0])): #first case
            self.state = "q"
            # put working next production for the symbol
            new_tuple = (current_symbol, current_index + 1) #('B', 2)
            self.working_stack.append(new_tuple)

            # change production on top input
            len_last_production = len(self.grammar.get_productions_for(current_symbol)[current_index]) #('bS', 7) -> len 2
            # delete last production from input
            self.input_stack = self.input_stack[len_last_production:]  # maybe len -1 -> []
            # put new production in input
            new_production = self.grammar.get_productions_for(current_symbol)[current_index + 1]
            self.concatenate_production_to_stack(new_production[0])
            # self.input_stack = new_production + self.input_stack
        elif self.index == 1 and last[0] == self.grammar.S:
            self.state = "e"
        else:
            # change production on top input
            len_last_production = len(self.grammar.get_productions_for(current_symbol)[current_index])
            # delete last production from input
            self.input = self.input_stack[len_last_production:]
            new_production = [current_symbol]
            # print(new_production)
            self.concatenate_production_to_stack(new_production)
            # self.input = [last[0]] + self.input

    def success(self):
        print("succes")
        self.state = "f"

    def run(self):
        pass

    def __str__(self):
        return "state = " + self.state + "\n" +\
               "index = " + str(self.index) + "\n" \
                "working stack = " + str(self.working_stack) + "\n" \
                "input stack = " + str(self.input_stack) + "\n"


if __name__ == '__main__':
    parser = RecursiveDescentParser("G1.txt")
    print(parser.grammar)
    print(str(parser))

    parser.expand()
    print(str(parser))

    parser.advance()
    print(str(parser))

    parser.expand()
    print(str(parser))

    parser.advance()
    print(str(parser))

    parser.momentary_insuccess()
    print(str(parser))

    parser.back()
    print(str(parser))

    parser.another_try()
    print(str(parser))