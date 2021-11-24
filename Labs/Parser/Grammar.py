class Grammar:

    def __init__(self) -> None:
        self.N = None
        self.E = None
        self.P = None
        self.S = None

    def read_from_file(self, filename):
        with open(filename) as file:
            self.N = self.parse_line(file.readline())
            self.E = self.parse_line(file.readline())
            self.S = file.readline().split('=')[1].strip()
            self.P = self.parse_productions(self.parse_line(''.join([line for line in file])))

    def parse_line(self, line):
        return [value.strip() for value in line.strip().split('=')[1].strip()[1:-1].strip().split(',')]

    def parse_productions(self, rules):
        # rules = ['S -> A B', 'A -> ( S ) | C', 'B -> + S | E', 'C -> * A | E']
        result = {}
        index = 1

        for rule in rules:
            # print(rule)
            lhs, rhs = rule.split('->')
            lhs = lhs.strip()
            rhs = [value.strip() for value in rhs.split('|')]

            for value in rhs:
                if lhs in result.keys():
                    result[lhs].append((value, index))
                else:
                    result[lhs] = [(value, index)]
                index += 1
        # print(result)
        return result

    def is_CFG(self): #A -> alpha, where alpha in {N U E}*
        if self.S not in self.N:
            return False
        for key in self.P.keys():
            if len(key) > 1:  # add left hand side
                return False #not a CFG
            if key not in self.N:
                return False
            for move in self.P[key]:
                # print(move[0])
                for char in move[0].split(' '):
                    # print(char)
                    if char not in self.N and char not in self.E and char != 'E':
                        print(char)
                        return False
        return True

    def is_non_terminal(self, value):
        return value in self.N

    def is_terminal(self, value):
        return value in self.E

    def get_productions_for(self, non_terminal):
        if not self.is_non_terminal(non_terminal):
            raise Exception('Can only show productions for non-terminals')
        for key in self.P.keys():
            if key == non_terminal:
                return self.P[key]

    def __str__(self):
        return 'N = { ' + ', '.join(self.N) + ' }\n' \
               + 'E = { ' + ', '.join(self.E) + ' }\n' \
               + 'P = ' + str(self.P) + '\n' \
               + 'S = ' + str(self.S) + '\n'
