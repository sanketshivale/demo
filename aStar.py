class Node():
    """A Node class for A* Pathfinding"""
    # Constructor for Node class.
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = self.h = self.f = 0
    # Comparator for Node class
    def __eq__(self, temp):
        return self.position == temp.position

# Boolean function to check if 
# a move is valid or not.
def notValid(nodePosition,n,m):
    return nodePosition[0] > n-1 or nodePosition[0] < 0 \
    or nodePosition[1] > m-1 or nodePosition[1] < 0

# A* algorithm function
def A_Star(board, src, dest):
    """This function returns a list of
    tuples representing the path from the given 
    src node to the given dest node in the given board"""
    # Creating the src and dest node
    # with parent as None.
    srcNode = Node(None, src)
    destNode = Node(None, dest)
    

    # Initializing both openList and 
    # closedList as empty list.
    openList = []
    closedList = []

    # Append srcNode in openList. 
    openList.append(srcNode)

    # Iterate until we reach the 
    # dest Node. 
    while len(openList) > 0:

        # Get the current node
        currentNode = openList[0]
        currentIndex = 0
        # Iterate over the openList to find 
        # node with least 'f'. 
        for index, item in enumerate(openList):
            if item.f < currentNode.f:
                currentNode = item
                currentIndex = index

        # Pop the found node off openList,
        # and add it to the closedList. 
        openList.pop(currentIndex)
        closedList.append(currentNode)

        # If reached the dest.
        if currentNode == destNode:
            # Initializng the 'path' list. 
            path = []
            current = currentNode
            # Adding currentposition in path 
            # and the moving to its parent until 
            # we reach None (parent of src). 
            while current is not None:
                path.append(current.position)
                current = current.parent
            # Returning the reversed path (to make
            # it src -> dest, instead of dest -> src.
            return path[::-1] 

        # Generate children
        children = []
        dirs=((0, -1), (0, 1), (-1, 0), (1, 0),
        (-1, -1), (-1, 1), (1, -1), (1, 1))
        # Iterate over neighouring cells.
        for newPosition in dirs: 

            # Find the position of new Node.
            nodePosition = (currentNode.position[0] + newPosition[0], 
            currentNode.position[1] + newPosition[1])

            # If the new position is not valid (lies outside the board)
            # then do not proceed ahead with this node.
            if(notValid(nodePosition,len(board),
            len(board[len(board)-1]))==True):
                continue
            # Also if the new position contains obstacle, 
            # we can't go ahead.
            if (board[nodePosition[0]][nodePosition[1]] != 0):
                continue
            # Append the node in children list.
            children.append(Node(currentNode, nodePosition))

        # Iterate over children list.
        for child in children:
            
            # If the child is in closedList
            for closedChild in closedList:
                if closedChild == child:
                    continue
            
            # Assign the values of f, g, and h.
            child.g = currentNode.g + 1
            child.h = ((child.position[0] - destNode.position[0]) ** 2) \
            + ((child.position[1] - destNode.position[1]) ** 2)
            child.f = child.g + child.h

            # If the Child is present in OpenList. 
            for openNode in openList:
                if child == openNode and child.g > openNode.g:
                    continue

            # Append the child at the last of open list
            openList.append(child)
        if (len(openList) > len(board)**2*len(board[0])**2): 
            return None

def main():
    board = [
                [0, 0, 0, 1, 0, 0],
                [0, 0, 1, 0, 1, 0],                
                [1, 0, 1, 0, 0, 0]
            ]

    src = (1, 0)
    dest = (2, 5)

    pathSrcToDest = A_Star(board, src, dest)
    print(pathSrcToDest)


if __name__ == '__main__':
    main()
