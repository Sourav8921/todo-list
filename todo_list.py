import json
import os


class TodoList:
    def __init__(self, file_name="todo_list.json"):
        self.file_name = file_name
        self.items = self.load_items()

    def add_item(self, item):
        self.items.append(item)
        self.save_items()
        print(f"Added: {item}")

    def remove_item(self, index):
        try:
            removed = self.items.pop(index)
            print(f"Removed: {removed}")
            self.save_items()
        except IndexError:
            print("Invalid index. Please try again.")

    def view_items(self):
        if not self.items:
            print("Todo list is empty")
        else:
            print("Your to-do list is:")
            for index, item in enumerate(self.items, start=1):
                print(f"{index} - {item}")

    def save_items(self):
        with open(self.file_name, 'w') as file:
            json.dump(self.items, file)

    def load_items(self):
        if os.path.exists(self.file_name):
            with open(self.file_name) as file:
                return json.load(file)
        else:
            return []


my_todo_list = TodoList()

print("To-do list")

while True:
    action = input("\nChoose an action: add, remove, display, or exit: ").lower()

    if action == 'add':
        value = input("Enter the to-do item: ")
        my_todo_list.add_item(value)
    elif action == 'display':
        my_todo_list.view_items()
    elif action == 'remove':
        my_todo_list.view_items()
        number = int(input("Enter the number of the item to remove: ")) - 1
        my_todo_list.remove_item(number)
    elif action == 'exit':
        print("Exiting the to-do list application. Goodbye!")
        break
    else:
        print("Invalid action. Please choose add, remove, display, or exit.")
