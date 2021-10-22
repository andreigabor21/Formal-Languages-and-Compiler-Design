from Scanner import Scanner
from SymbolClassifier import SymbolClassifier
from SymbolTable import SymbolTable


def test_SymbolTable():
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

if __name__ == '__main__':
    sc = SymbolClassifier()
    print("separators:", sc.separators)
    print("operators:", sc.operators)
    print("reserved words:", sc.reservedWords)