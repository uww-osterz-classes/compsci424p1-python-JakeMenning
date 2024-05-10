"""
COMPSCI 424 Program 1
Name: Jake Menning
"""

# I was unable to finish Program 1.






import time
#import collections.abc.MutableSequence

# There are many correct ways to solve this in Python, so I'm giving
# you minimal guidance for your Python code. Any correct solution is
# allowed.

class ListNode:
    def __init__(self, val):
        self.value = val
        self.next = None
    
    


class LinkedList:
    def __init__(self):
        self.head = self.tail = None
        self.size = 0
    
    def insertAtFront(self, value):
        newNode = ListNode(value)
        if (self.size == 0):
            self.head = self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.size = self.size + 1
        return newNode
    
    def insertAtEnd(self, value):
        newNode = ListNode(value)
        if (self.size == 0):
            self.head = self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.size = self.size + 1
        return newNode
    
    def deleteHead(self):
        if(self.size == 0):
            print("Cannot delete from an empty list.")
        elif(self.size == 1):
            self.size = self.size - 1
            self.head = None
        else:
            self.size = self.size - 1
            tmp = self.head
            self.head = self.head.next
            tmp = None

    def getSize(self):
        return self.size
    
    def printList(self):
        if (self.size == 0):
            print("[]")
        else:
            tmp = self.head
            print("[", end="")
            for i in range(0,self.size-1):
                print(tmp.value, " -> ", end="")
                tmp = tmp.next
            print(self.tail.value, "]")
    



"""
class v1:
    def __init__(self):
        self.pcbArray = []

    def create(self, p):
        self #self.pcbArray.append(v1pcb(p))

    def destroy(self, p):
        #for i in 
        self.pcbArray
"""


class v1pcb:
    def __init__(self, p):
        self.p = p
        self.c = LinkedList()    
    
    def getParent(self):
        return self.p
    
    def getChildren(self):
        return self.c



def main():
    # parallel lists to hold pcb objects and the process's pid
    global processList
    processList = []
    global inUse
    inUse = []
    global pid
    pid = 1

    father = v1pcb(-1)
    processList.append(father)
    inUse.append(0)

    varStr = ""
    n = 0
    pairList = []
    command = ""
    print("Please enter commands to continue, N should be an integer value between 0 and 15.\nList of commands:\n\t'create N'\n\t'destroy N'\n\t'end'")

    while (command != "end"):    
        varStr = input("Please enter your command here: ")
        command = (varStr.split())[0].lower()
        # if statement to check if commands were entered and if N is an integer.
        if((command != "create" and command != "destroy" and command != "end")):
            print("\nYou entered the command in the wrong syntax; enter the command in the same syntax as the listed commands below (make sure N is an integer; else, it will error out):\nList of commands:\n\t'create N'\n\t'destroy N'\n\t'end'")
        if(command == "end"):
            break
        n = int((varStr.split())[1])
        if(command == "create" or command == "destroy") and (isinstance(n, int)):
            pair = (command, n)
            pairList.append(pair)
        
    print("Pair List: ", pairList)
    print("pairList var: ", len(pairList))

    for i in range(0, len(pairList)):
        if(pairList[i][0] == "create"):
            v1Create(pairList[i][1])
        elif(pairList[i][0] == "destroy"):
            v1Destroy(pairList[i][1])

    for i in range(0, len(processList)):
        print("ProcessList (", inUse[i], "): ", processList[i], "\n\tChildren: ", end="")
        processList[i].getChildren().printList()




def v1Create(pPID):
    global pid
    processList.append(v1pcb(pPID))
    inUse.append(pid)
    pid = pid + 1
    processList[pPID].getChildren().insertAtEnd(pid)

def v1Destroy(pPID):
    pPID

        
"""
class version1:
    def __init__(self):
        self

class version2:
    def __init__(self):
        self

class pcbv1:
    def __init__(self, parent, children):
        self.parent = parent
        self.childList = LinkedList(self.children[0], self.children[self.children.len()-1], self.children.len())

class pcbv2:
    def __init__(self, parent, firstChild, ys, os):
        self.parent = parent
        self.firstChild = firstChild
        self.ys = ys
        self.os = os
        
class process:
    def __init__(self):
        self

def v1():
    var = 1


def v2():
    var = 1

"""

main()

