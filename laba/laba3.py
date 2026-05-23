class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def put(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1
        print(f"Добавлено в конец: {data}")

    def get(self):
        if self.is_empty():
            print("Очередь пуста")
            return None
        data = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self.size -= 1
        print(f"Удалено из начала: {data}")
        return data

    def is_empty(self):
        return self.size == 0

    def get_size(self):
        return self.size

    def peek(self):
        if self.is_empty():
            print("Очередь пуста")
            return None
        return self.front.data

    def show(self):
        if self.is_empty():
            print("Очередь пуста")
            return
        current = self.front
        while current:
            print(current.data, end=" ")
            current = current.next
        print()


class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.size += 1
        print(f"Добавлено наверх: {data}")

    def pop(self):
        if self.is_empty():
            print("Стек пуст")
            return None
        data = self.top.data
        self.top = self.top.next
        self.size -= 1
        print(f"Удалено сверху: {data}")
        return data

    def is_empty(self):
        return self.size == 0

    def get_size(self):
        return self.size

    def peek(self):
        if self.is_empty():
            print("Стек пуст")
            return None
        return self.top.data

    def show(self):
        if self.is_empty():
            print("Стек пуст")
            return
        current = self.top
        while current:
            print(current.data, end=" ")
            current = current.next
        print()


class Deque:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def lput(self, data):
        new_node = Node(data)
        if self.front is None:
            self.front = new_node
            self.rear = new_node
        else:
            new_node.next = self.front
            self.front = new_node
        self.size += 1
        print(f"Добавлено слева: {data}")

    def rput(self, data):
        """Добавление справа (в конец)"""
        new_node = Node(data)
        if self.rear is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1
        print(f"Добавлено справа: {data}")

    def lget(self):
        """Удаление слева (из начала)"""
        if self.is_empty():
            print("Дек пуст")
            return None
        data = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self.size -= 1
        print(f"Удалено слева: {data}")
        return data

    def rget(self):
        if self.is_empty():
            print("Дек пуст")
            return None
        if self.front == self.rear:
            data = self.front.data
            self.front = None
            self.rear = None
            self.size -= 1
            print(f"Удалено справа: {data}")
            return data
        current = self.front
        while current.next != self.rear:
            current = current.next
        data = self.rear.data
        self.rear = current
        self.rear.next = None
        self.size -= 1
        print(f"Удалено справа: {data}")
        return data

    def is_empty(self):
        return self.size == 0

    def get_size(self):
        return self.size

    def peek_left(self):
        if self.is_empty():
            print("Дек пуст")
            return None
        return self.front.data

    def peek_right(self):
        if self.is_empty():
            print("Дек пуст")
            return None
        return self.rear.data

    def show(self):
        if self.is_empty():
            print("Дек пуст")
            return
        current = self.front
        while current:
            print(current.data, end=" ")
            current = current.next
        print()


while True:
    print("выберите структуру данных")
    print("1 - Очередь (Queue) - FIFO")
    print("2 - Стек (Stack) - LIFO")
    print("3 - Дек (Deque) - двусторонний")
    print("4 - Выход")

    choice = input("Выберите: ")

    if choice == "1":
        q = Queue()
        while True:
            print("\n1 - Добавить")
            print("2 - Удалить")
            print("3 - Показать все")
            print("4 - Показать первый")
            print("5 - Размер")
            print("6 - Назад")

            cmd = input("Выберите: ")

            if cmd == "1":
                item = input("Введите элемент: ")
                q.put(item)
            elif cmd == "2":
                q.get()
            elif cmd == "3":
                q.show()
            elif cmd == "4":
                first = q.peek()
                if first:
                    print(f"Первый элемент: {first}")
            elif cmd == "5":
                print(f"Размер: {q.get_size()}")
            elif cmd == "6":
                break
            else:
                print("Неверная команда")

    elif choice == "2":
        s = Stack()
        while True:
            print("\n1 - Добавить")
            print("2 - Удалить")
            print("3 - Показать все")
            print("4 - Показать верхний")
            print("5 - Размер")
            print("6 - Назад")

            cmd = input("Выберите: ")

            if cmd == "1":
                item = input("Введите элемент: ")
                s.push(item)
            elif cmd == "2":
                s.pop()
            elif cmd == "3":
                s.show()
            elif cmd == "4":
                top = s.peek()
                if top:
                    print(f"Верхний элемент: {top}")
            elif cmd == "5":
                print(f"Размер: {s.get_size()}")
            elif cmd == "6":
                break
            else:
                print("Неверная команда")

    elif choice == "3":
        d = Deque()
        while True:
            print("\n1 - Добавить слева")
            print("2 - Добавить справа")
            print("3 - Удалить слева")
            print("4 - Удалить справа")
            print("5 - Показать все")
            print("6 - Показать левый")
            print("7 - Показать правый")
            print("8 - Размер")
            print("9 - Назад")

            cmd = input("Выберите: ")

            if cmd == "1":
                item = input("Введите элемент: ")
                d.lput(item)
            elif cmd == "2":
                item = input("Введите элемент: ")
                d.rput(item)
            elif cmd == "3":
                d.lget()
            elif cmd == "4":
                d.rget()
            elif cmd == "5":
                d.show()
            elif cmd == "6":
                left = d.peek_left()
                if left:
                    print(f"Левый элемент: {left}")
            elif cmd == "7":
                right = d.peek_right()
                if right:
                    print(f"Правый элемент: {right}")
            elif cmd == "8":
                print(f"Размер: {d.get_size()}")
            elif cmd == "9":
                break
            else:
                print("Неверная команда")

    elif choice == "4":
        print("До свидания!")
        break

    else:
        print("Неверный выбор")