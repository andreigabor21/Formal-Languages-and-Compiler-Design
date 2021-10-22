class SymbolClassifier:

    def __init__(self):
        self.separators = []
        self.operators = []
        self.reservedWords = []
        self.classify()

    def classify(self) -> None:
        with open('Token.in', 'r') as f:
            f.readline()
            for i in range(11):
                separator = f.readline().strip()
                if separator == "space":
                    separator = " "
                self.separators.append(separator)
            for i in range(13):
                self.operators.append(f.readline().strip())
            for i in range(13):
                self.reservedWords.append(f.readline().strip())