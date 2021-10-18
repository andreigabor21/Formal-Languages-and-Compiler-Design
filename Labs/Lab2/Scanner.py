from re import *


class Scanner:
    def __init__(self) -> None:
        self._tokens = ['(', ')', '[', '{', '}', ';', ',', ';', '+', '-', '*', '/', '=', '<', '>', '<=', '>=', '==',
                            '!=', '!', 'fn main', 'and', 'array', 'else', 'for', 'if', 'int', 'or', 'string', 'while',
                            'read', 'println']

    def isIdentifier(self, token) -> bool:
        '''
        Check if the given token is an identifier
        :param token: the given token
        :return: true if it is an identifier, otherwise false
        '''
        return match(r'^[a-z]([a-zA-Z]|[0-9])*$', token) is not None

    def isConstant(self, token) -> bool:
        '''
        Check if the given token is a constant
        :param token: the given token
        :return: true if it is a constant, otherwise false
                '''
        return match(r'^(0|[+-]?[1-9][0-9]*)$|^\'.\'$|^\'.*\'$', token) is not None

    def getStringTokenFromLine(self, line, index):
        '''
        Gets a string (text between quotes) from a line input
        '''
        token = ''
        quotes = 0
        while index < len(line) and quotes < 2:
            if line[index] == '\"':
                quotes += 1
            index += 1
            token += line[index]
        return token, index

    def isPartOfOperator(self, char) -> bool:
        '''
        Checks if a character is part of an operator
        '''
        for op in self._tokens:
            if char in op:
                return True
        return False

    def getOperatorToken(self, line, index):
        '''
        Gets an operator from the given line
        '''
        token = ''
        while index < len(line) and self.isPartOfOperator(line[index]):
            token += line[index]
            index += 1
        return token, index
