import pytest


class TodoList:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, index):
        try:
            return self.items.pop(index)
        except IndexError:
            print("Invalid index. Please try again.")

    def show_items(self):
        return self.items


# Test cases using pytest
def test_add_item():
    todo = TodoList()
    todo.add_item("Finish homework")
    assert todo.show_items() == ["Finish homework"]

    todo.add_item("Read a book")
    assert todo.show_items() == ["Finish homework", "Read a book"]


def test_remove_item():
    todo = TodoList()
    todo.add_item("Finish homework")
    todo.add_item("Read a book")

    removed_item = todo.remove_item(0)
    assert removed_item == "Finish homework"
    assert todo.show_items() == ["Read a book"]

    removed_item = todo.remove_item(0)
    assert removed_item == "Read a book"
    assert todo.show_items() == []


def test_remove_item_invalid_index(capfd):
    todo = TodoList()
    todo.add_item("Finish homework")

    todo.remove_item(5)
    captured = capfd.readouterr()
    assert "Invalid index. Please try again." in captured.out


def test_show_items():
    todo = TodoList()
    assert todo.show_items() == []

    todo.add_item("Finish homework")
    todo.add_item("Read a book")
    assert todo.show_items() == ["Finish homework", "Read a book"]
