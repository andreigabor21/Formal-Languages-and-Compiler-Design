class SymbolTable:
    def __init__(self, size: int) -> None:
        self.__items = [[] for _ in range(size)]
        self.__size = size

    def hash(self, key: str) -> int:
        sum = 0
        for character in key:
            sum += ord(character) - ord('0')
        return sum % self.__size

    def get_position(self, key):
        list_position = self.hash(key)
        list_index = 0
        for item in self.__items[list_position]:
            if item != key:
                list_index += 1
            else:
                break
        return (list_position, list_index)

    def insert(self, key: str):
        if self.contains(key):
            return self.get_position(key)
        self.__items[self.hash(key)].append(key)
        return self.get_position(key)

    def delete(self, key) -> None:
        position = self.hash(key)
        self.__items[position].remove(key)

    def contains(self, key) -> bool:
        return key in self.__items[self.hash(key)]

    def __str__(self) -> str:
        representation = ""
        for i in range(self.__size):
            representation += str(i) + "->" + str(self.__items[i]) + "\n"
        return representation


