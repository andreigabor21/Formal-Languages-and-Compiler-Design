class FiniteAutomata:

    def __init__(self, Q: list, E: list, q0, F: list, S: dict):
        self.Q = Q
        self.E = E
        self.delta = S
        self.q0 = q0
        self.F = F

    def isDFA(self):
        for elem in self.delta.keys():
            if len(self.delta[elem]) > 1:
                return False
        return True

    def isAccepted(self, sequence):
        if self.isDFA():
            current = self.q0
            for symbol in sequence:
                if (current, symbol) in self.delta.keys():
                    current = self.delta[(current,symbol)][0]
                else:
                    return False
            return current in self.F
        return False

    def __str__(self):
        return "Q = { " + ', '.join(self.Q) + " }\n" \
               "E = { " + ', '.join(self.E) + " }\n" \
               "q0 = { " + self.q0 + " }\n" \
               "S = { " + str(self.delta) + " } " \
               "F = { " + ', '.join(self.F) + " }\n" \
