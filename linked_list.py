class Node:
    def __init__(self, title: str, date: str, summary: str, facts: str) -> None:
        self.title = title
        self.date = date
        self.summary = summary
        self.facts = facts
        self.next = None

    def deleteSummary(self):
        self.summary = ""
        
    def addSummary(self, new_summary: str):
        self.summary += " " + new_summary
        
    def addFacts(self, new_facts: str):
        self.facts += " " + new_facts
        
    def deletefacts(self):
        self.facts = ""

    def deleteTitle(self):
        self.title = ""

    def displayInfo(self):
        print("-"*50)
        print("Title: ", self.title)
        print("Date: ", self.date)
        print("Summary: ", self.summary)
        print("Facts: ", self.facts)


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def addNode(self, node: Node, pos: int = -1) -> None:
        '''Add node in given pos(position). If admin don't pass position so by default new node will add to last of linked list'''
        if not self.head:
            self.head = node
            return
        if pos == -1:
            self.insertAtLast(node)
            return
        t = self.head
        if pos == 0:
            node.next = self.head
            self.head = node
            return
        for x in range(pos-1):
            if not t.next:
                print("Given position is out of range")
                return
            t = t.next
        node.next = t.next
        t.next = node

    def insertAtLast(self, node: Node) -> None:  # helper function
        t = self.head
        while t.next:
            t = t.next
        t.next = node

    def deleteLast(self) -> None:  # helper function
        t = self.head
        while t.next.next:
            t = t.next
        t.next = None

    def display(self) -> None:
        if not self.head:
            print("LinkedList is empty")
            return
        t = self.head
        while t:
            t.displayInfo()
            t = t.next

    def delete(self, pos: int = -1) -> None:
        '''Delete node from given pos(position). If admin don't pass position so by default last node will deleted.'''
        if not self.head:
            print("LinkedList is empty")
            return
        if pos == -1:
            self.deleteLast()
            return
        t = self.head
        for x in range(pos-1):
            if not t.next:
                print("Given position is out of range")
                return
            t = t.next
        t.next = t.next.next if t.next else None

    def reorder(self, node, pos) -> None:
        '''Change position of given node'''
        if not self.head:
            print("LinkedList is empty")
            return
        t = self.head
        if t == node:
            self.head = t.next
            self.addNode(node, pos)
            return
        while t.next != node:
            if not t.next:
                print("Given Node is not found")
                return
            t = t.next
        t.next = t.next.next
        self.addNode(node, pos)


n1 = Node("t1", "d1", "s1", "f1")
n2 = Node("t2", "d2", "s2", "f2")
n3 = Node("t3", "d3", "s3", "f3")
n4 = Node("t4", "d4", "s4", "f4")


#you can add/delete/overwrite without function
n1.summary = ""                 # delete a data
n2.facts = "new facts"          # overwrite data
n3.title += " and new title"     # add data


l1 = LinkedList()
l1.addNode(n1)                  # add in last
l1.addNode(n2, 0)               # add in last
l1.addNode(n3)                  # add in last
l1.addNode(n4, 0)               # add in first position
l1.delete(2)                    # delete third node, Index start with zero
l1.reorder(n4, 2)               # change position of n2 to pos = 3 (third index)
l1.display()
