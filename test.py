class Item():  
    def __init__(self, name):
        self.name = name

class TodoList():
    work_list = []
    done_list = []

    def add_to_toDo(self, item):
        if item.name not in self.work_list:
            self.work_list.append(item)
        else:
            return False
        return True

    def add_to_doneList(self, number_item):
        self.done_list.append(self.work_list.pop(number_item))
        

    def show_todo_list(self):
        for num, i in enumerate(self.work_list):
            print("---------------------")
            print("{} {} ".format(num, i.name))
            print("---------------------")

    def show_done_list(self):
        for num, i in enumerate(self.done_list):
            print("---------------------")
            print("{} {} - done".format(num, i.name))
            print("---------------------")
     
    


def main():
    todoList = TodoList()
    print("Welcome to ToDo List ")
    allow_commands = ["add", "done", "history", "show", "exit"]
    while True:
        print("Comands: <add|done|history|show|exit>")
        user_input = input("Input command ").lower()
        if user_input not in allow_commands:
            print("Bad input, try again pls")

        if user_input == 'add':
            name = str(input("Input name "))
            item = Item(name)
            todoList.add_to_toDo(item)
            print("{} is add".format(name))

        if user_input == "done":
            index =  int(input('Input number of item to done '))
            if isinstance(index, int) == False:
                print("Bad input, try again pls <int>")
            else:
                try:
                    todoList.add_to_doneList(index)
                except IndexError:
                    print("This number does not exist!")

        if user_input == "history":
            print("History ")
            todoList.show_done_list()

        if user_input == "show":
            print("You need todo ")
            todoList.show_todo_list()

        if user_input == "exit":
            print("Bye")
            return False


main()
            


    

