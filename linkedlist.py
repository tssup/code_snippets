#! /usr/bin/env python


class Node:
    def __init__(self, initial_data):
        self.data = initial_data
        self.next = None

    def getData(self):
        return self.data

    def setData(self, new_data):
        self.data = new_data

    def getNext(self):
        return self.next

    def setNext(self, next_node):
        self.next = next_node


class UnorderedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def add(self, data):
        new_node = Node(data)
        new_node.setNext(self.head)
        self.head = new_node

    def length(self):
        current = self.head
        while current != None:
            self.count += 1
            current = current.getNext()
        return self.count

    def indexer(self, index):
        current = self.head
        count = 0

        while current != None:
            if count == index:
                return current.getData()
            current = current.getNext()
            count += 1

    def search(self, item):
        current = self.head
        found = False

        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self, item):
        previous = None
        current = self.head
        found = False

        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())


if __name__ == "__main__":
    u_list = UnorderedList()
    u_list.add(1)
    u_list.add(100)
    u_list.add("Hello")
    # u_list.add([1, 2, 3, 441, 90])

    print(u_list.length())
    # print(u_list.showNodes())
    print(u_list.search("Hell"))
    print(u_list.search("Hello"))
    print(u_list.indexer(1))

    # 5 4 3 2 1 0 == count

    # 0 1 2 3 4 5 == index
