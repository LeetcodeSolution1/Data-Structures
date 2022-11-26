from Node import Node


def inorder(root):
    '''
    Traverses left, root, right
    '''

    if(root):
        inorder(root.left)
        print(root.data)
        inorder(root.right)


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

    inorder(root)
