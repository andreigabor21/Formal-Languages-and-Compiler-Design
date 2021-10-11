class SymbolTable:
    def __init__(self, size: int) -> None:
        self.__items = [[] for _ in range(size)]
        self.__size = size

    def hash(self, key: str) -> int:
        sum = 0
        for character in key:
            sum += ord(character) - ord('0')
        return sum % self.__size

    def insert(self, key: str) -> None:
        position = self.hash(key)
        self.__items[position].append(key)

    def delete(self, key):
        position = self.hash(key)
        self.__items[position].remove(key)

    def contains(self, key):
        position = self.hash(key)
        return key in self.__items[position]

    def __str__(self) -> str:
        representation = ""
        for i in range(self.__size):
            representation += str(i) + "->" + str(self.__items[i]) + "\n"
        return representation


