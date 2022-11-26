from Node import Node


def bfs(root):
    '''
    Traverses level by level from left to right
    '''

    queue = [root]

    while(queue):
        node = queue.pop(0)
        print(node.data)

        if(node.left is not None):
            queue.append(node.left)

        if(node.right is not None):
            queue.append(node.right)


if(__name__ == "__main__"):
    root = Node(1)
    child1 = Node(3)
    child2 = Node(2)
    child3 = Node(4)
    child4 = Node(5)
    child5 = Node(7)

    root.left = child1
    root.right = child2

    child1.left = child3
    child1.right = child4
    child2.right = child5

    bfs(root)
