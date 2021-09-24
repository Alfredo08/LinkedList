
from myPackage.LinkedList import LinkedList
# At this point the list is empty
listOfNumbers = LinkedList()

# Adding the first node to the list
listOfNumbers.insertLast( 10 )
listOfNumbers.insertLast( 5 )
listOfNumbers.insertLast( 20 )
listOfNumbers.insertLast( 15 )
listOfNumbers.insertLast( 30 )

listOfNumbers.insertAtPosition( 5, 50 )
listOfNumbers.printList()

