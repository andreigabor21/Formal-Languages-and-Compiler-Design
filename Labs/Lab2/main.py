from SymbolTable import *

if __name__ == '__main__':
    table = SymbolTable(5)
    table.insert("a")
    table.insert("b")
    table.insert("c")
    table.insert("qwe")
    table.insert("lk")
    table.insert("kl")

    assert table.contains("a")
    table.delete("a")
    assert not table.contains("a")
    assert table.contains("qwe")
    assert table.contains("kl")

    print(table)