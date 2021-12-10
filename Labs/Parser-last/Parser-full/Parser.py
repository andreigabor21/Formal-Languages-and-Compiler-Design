from Grammar import Grammar
from Node import Node
from ParserOutput import ParserOutput


class ParserRecursiveDescendent:
    def __init__(self, grammar_file, sequence_file, out_file):
        self.grammar = Grammar(grammar_file)
        self.sequence = self.read_sequence(sequence_file)
        self.output_file = out_file
        self.init_output_file()
        print(self.sequence)

        # alpha - working stack, stores the way the parse is build
        self.working_stack = []
        # input stack
        self.input_stack = [self.grammar.get_start_symbol()[0]]  # ['a', 'S', 'b', 'S', 'b', 'S']
        # q - normal state, b - back state, f - final state, e - error state
        self.state = "q"
        # i - position of current symbol in input sequenc
        self.index = 0
        # representation - parsing tree
        self.tree = []

        self.parserOutput = ParserOutput(self)

    # reads the input sequence from the given file
    def read_sequence(self, sequence_file):
        sequence = []
        with open(sequence_file) as file:
            if sequence_file == "PIF.out":
                line = file.readline()
                line = file.readline()
                while line:
                    elems_line = line.split(" ")
                    sequence.append(elems_line[0])
                    line = file.readline()
            else:
                line = file.readline()
                while line:
                    sequence.append(line[0:-1])
                    line = file.readline()
        return sequence

    def write_all_data(self):
        with open(self.output_file, 'a') as file:
            # f.write("--------------\n")
            file.write(str(self.state) + " ")
            file.write(str(self.index) + "\n")
            file.write(str(self.working_stack) + "\n")
            file.write(str(self.input_stack) + "\n")

    def init_output_file(self): #creates the given file
        file = open(self.output_file, 'w')
        file.write("")
        file.close()

    def write_in_output_file(self, message, final=False):
        with open(self.output_file, 'a') as file:
            if final:
                file.write("-------RESULT:-------\n")
            file.write(message + "\n")

    def expand(self):
        # when: head of input stack is a non terminal
        # (q, i, alpha, A beta) ⊢ (q, i, alpha A1, gamma1 beta)
        print("---expand---")
        self.write_in_output_file("---expand---")
        non_terminal = self.input_stack.pop(0) # pop A from beta
        self.working_stack.append((non_terminal, 0)) # alpha -> alpha A1
        new_production = self.grammar.get_productions_for_non_terminal(non_terminal)[0]
        self.input_stack = new_production + self.input_stack

    def advance(self):
        # when: head of input stack is a terminal = current symbol from input
        # (q, i, alpha, a_i beta) ⊢ (q, i+1, alpha a_i, beta)
        print("---advance---")
        self.write_in_output_file("---advance---")
        self.working_stack.append(self.input_stack.pop(0))
        self.index += 1

    def momentary_insuccess(self):
        # when: head of input stack is a terminal != current symbol from input
        print("---momentary insuccess---")
        self.write_in_output_file("---momentary insuccess---")
        self.state = "b"

    def back(self):
        # when: head of working stack is a terminal
        # (b, i, alpha a, beta) ⊢ (b, i-1, alpha, a beta)
        print("---back---")
        self.write_in_output_file("---back---")
        new_thing = self.working_stack.pop()
        self.input_stack = [new_thing] + self.input_stack
        self.index -= 1

    def success(self):
        # print("---success---")
        self.write_in_output_file("---success---")
        self.state = "f"

    def another_try(self):
        # print("---another try---")
        self.write_in_output_file("---another try---")
        last = self.working_stack.pop()  # (last, production_nr)
        if last[1] + 1 < len(self.grammar.get_productions_for_non_terminal(last[0])):
            self.state = "q"
            # put working next production for the symbol
            new_tuple = (last[0], last[1] + 1)
            self.working_stack.append(new_tuple)

            # change production on top input
            length_last_production = len(self.grammar.get_productions_for_non_terminal(last[0])[last[1]])
            # delete last production from input
            self.input_stack = self.input_stack[length_last_production:]

            # put new production in input
            new_production = self.grammar.get_productions_for_non_terminal(last[0])[last[1] + 1]
            self.input_stack = new_production + self.input_stack
        elif self.index == 1 and last[0] == self.grammar.get_start_symbol():
            self.state = "e"
        else:
            # change production on top input
            length_last_production = len(self.grammar.get_productions_for_non_terminal(last[0])[last[1]])
            # delete last production from input
            self.input_stack = self.input_stack[length_last_production:]
            self.input_stack = [last[0]] + self.input_stack

    def print_working(self):
        # prints the working stack to the screen and in the output file
        print(self.working_stack)
        self.write_in_output_file(str(self.working_stack))

    def run(self, w):
        while (self.state != 'f') and (self.state != 'e'):
            self.write_all_data()
            if self.state == 'q':
                if len(self.input_stack) == 0 and self.index == len(w):
                    self.success()
                elif len(self.input_stack) == 0:
                    self.state = 'b'
                    print("No input, still have terminals to parse")
                    break
                else:
                    # WHEN: head of input stack is a non terminal
                    if self.input_stack[0] in self.grammar.get_non_terminals():
                        self.expand()
                    else:
                        # WHEN: head of input stack is a terminal = current symbol from input
                        if self.index < len(w) and self.input_stack[0] == w[self.index]:
                            self.advance()
                        else:
                            # WHEN: head of input stack is a terminal ≠ current symbol from input
                            self.momentary_insuccess()
            else:
                if self.state == 'b':
                    if self.index == 0 and len(self.working_stack) == 0:
                        self.state = 'e'
                        print("no top working to look at in Back!")
                        break
                    if self.working_stack[-1] in self.grammar.get_terminals():
                        self.back()
                    else:
                        self.another_try()
        if self.state == 'e':
            message = "ERROR! @ index: {}".format(self.index)
        else:
            message = "Sequence is accepted!"
            self.print_working()
        print(message)
        self.write_in_output_file(message, True)
        self.create_parsing_tree()
        self.parserOutput.write_parsing_tree()

    def create_parsing_tree(self):
        # creates the parsing tree
        father = -1
        for index in range(0, len(self.working_stack)):
            # iterates in the working stack
            if type(self.working_stack[index]) == tuple:
                self.tree.append(Node(self.working_stack[index][0])) #value
                self.tree[index].production = self.working_stack[index][1]
            else:
                self.tree.append(Node(self.working_stack[index]))

        for index in range(0, len(self.working_stack)):
            if type(self.working_stack[index]) == tuple:
                self.tree[index].father = father # sets the father
                father = index
                # computes the length of the production of a non terminal
                len_prod = len(self.grammar.get_productions()[self.working_stack[index][0]][self.working_stack[index][1]])
                vector_index = []
                for i in range(1, len_prod + 1):
                    vector_index.append(index + i)
                for i in range(0, len_prod):
                    if self.tree[vector_index[i]].production != -1:
                        offset = self.get_length_depth(vector_index[i])
                        for j in range(i + 1, len_prod):
                            vector_index[j] += offset
                for i in range(0, len_prod - 1):
                    self.tree[vector_index[i]].sibling = vector_index[i + 1]
            else:
                self.tree[index].father = father
                father = -1

    def get_length_depth(self, index):
        production = self.grammar.get_productions()[self.working_stack[index][0]][self.working_stack[index][1]]
        length_of_production = len(production)
        sum = length_of_production
        for i in range(1, length_of_production + 1):
            if type(self.working_stack[index + i]) == tuple:
                sum += self.get_length_depth(index + i)
        return sum


if __name__ == '__main__':
    # parser2 = ParserRecursiveDescendent("g2.txt", "PIF.out", "out2.txt")
    parser1 = ParserRecursiveDescendent("g1.txt", "seq.txt", "out1.txt")
    # run the Parser for the sequence
    parser1.run(parser1.sequence)