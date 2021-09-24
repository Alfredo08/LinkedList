#from Node import Node
from myPackage.Node import Node

class LinkedList:
    def __init__( self ):
        self.head = None
    
    def insertLast( self, val ):
        newNode = Node( val )
        if self.head == None:
            self.head = newNode
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = newNode
    
    def printList( self ):
        current = self.head
        while current != None:
            print( current.val )
            current = current.next

    def insertFirst( self, val ):
        newNode = Node( val )
        if self.head == None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def findNode( self, val ):
        current = self.head
        while current != None:
            if current.val == val:
                return current
            current = current.next
        return None

    def deleteNode( self, val ):
        if self.head == None:
            return None
        current = self.head
        previous = self.head
        if self.head.val == val:
            self.head = self.head.next
            current.next = None
        else:
            while current != None and current.val != val:
                previous = current
                current = current.next
            if current != None:
                previous.next = current.next
                current.next = None

    def length( self ):
        current = self.head;
        count = 0
        while current != None:
            count += 1
            current = current.next
        return count

    def insertAtPosition( self, index, val ):
        newNode = Node( val )
        if index <= self.length():
            if index == 0:
                self.insertFirst( val )
            else:
                count = 0
                current = self.head
                while count < index - 1:
                    count += 1
                    current = current.next
                newNode.next = current.next
                current.next = newNode
