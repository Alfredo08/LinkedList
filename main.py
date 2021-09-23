
from myPackage.LinkedList import LinkedList
# At this point the list is empty
listOfNumbers = LinkedList()

# Adding the first node to the list
listOfNumbers.insertLast( 10 )
listOfNumbers.insertLast( 30 )
listOfNumbers.insertLast( 50 )
listOfNumbers.insertLast( 80 )
listOfNumbers.insertFirst( 100 )

listOfNumbers.printList()
print( "------" )
listOfNumbers.deleteNode( 80 )
listOfNumbers.printList()
