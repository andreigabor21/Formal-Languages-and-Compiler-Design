from re import *

from SymbolClassifier import SymbolClassifier


class Scanner:

    def __init__(self):
        self.symbol_classifier = SymbolClassifier()

    def is_identifier(self, token) -> bool:
        '''
        Check if the given token is an identifier
        :param token: the given token
        :return: true if it is an identifier, otherwise false
        '''
        return match(r'^[a-z]([a-zA-Z]|[0-9])*$', token) is not None

    def is_constant(self, token) -> bool:
        '''
        Check if the given token is a constant
        :param token: the given token
        :return: true if it is a constant, otherwise false
                '''
        return match(r'^(0|[+-]?[1-9][0-9]*)$|^\'.\'$|^\'.*\'$', token) is not None

    def get_string_token_from_line(self, line, index):
        '''
        Gets a string (text between quotes) from a line input
        '''
        token = ''
        quotes = 0
        while index < len(line) and quotes < 2:
            if line[index] == '\'':
                quotes += 1
            token += line[index]
            index += 1
        return token, index

    def is_part_of_operator(self, char) -> bool:
        '''
        Checks if a character is part of an operator
        '''
        for op in self.symbol_classifier.operators:
            if char in op:
                return True
        return False

    def get_operator_token(self, line, index):
        '''
        Gets an operator from the given line
        '''
        token = ''
        while index < len(line) and self.is_part_of_operator(line[index]):
            token += line[index]
            index += 1
        return token, index

    def get_reserved_words(self):
        return self.symbol_classifier.reservedWords

    def get_operators(self):
        return self.symbol_classifier.separators

    def get_separators(self):
        return self.symbol_classifier.operators

    def get_tokens(self, line):
        token = ''
        index = 0
        tokens = []
        while index < len(line):
            if self.is_part_of_operator(line[index]):
                if token:
                    tokens.append(token)
                token, index = self.get_operator_token(line, index)
                tokens.append(token)
                token = ''  # reset token

            elif line[index] == '\'':
                if token:
                    tokens.append(token)
                token, index = self.get_string_token_from_line(line, index)
                print(token) # is prime')
                tokens.append(token)
                token = ''  # reset token

            elif line[index] in self.symbol_classifier.separators:
                if token:
                    # print(token) println
                    tokens.append(token)
                token = line[index]
                index += 1
                # print(token) ( ) ;
                tokens.append(token)
                token = ''  # reset token

            else:
                token += line[index]
                index += 1
        if token:
            tokens.append(token)
        return tokens
