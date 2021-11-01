
from finite_automata import FiniteAutomata
from utils import Utils


class Console:

    def __init__(self):
        self.finite_automata = Utils.readFromFile('FA.in')

    def showAll(self):
        print(self.finite_automata)

    def showStates(self):
        print(self.finite_automata.Q)

    def showAlphabet(self):
        print(self.finite_automata.E)

    def showTransitions(self):
        print(self.finite_automata.delta)

    def showSetOfFinalStates(self):
        print(self.finite_automata.F)

    def checkDFA(self):
        print(self.finite_automata.isDFA())

    def checkIfAccepted(self):
        sequence = input('Read sequence>>')
        print(self.finite_automata.isAccepted(sequence))

    def __displayMenu(self):
        print("0. Exit")
        print("1.Display everything")
        print("2.Display States")
        print("3.Display Alphabet")
        print("4.Display transitions")
        print("5.Display final states")
        print("6.Check DFA")
        print("7: Check if a sequence is accepted")

    def run(self):
        commands = {'1':self.showAll, '2':self.showStates, '3':self.showAlphabet, '4':self.showTransitions,
                '5':self.showSetOfFinalStates, '6':self.checkDFA, '7': self.checkIfAccepted}
        exit = False
        while not exit:
            self.__displayMenu()
            print(">>")
            command = input()
            if command in commands.keys():
                commands[command]()
            elif command=='0':
                exit = True
            else:
                continue