from rb_tree import RedBlackTree

def main():
    ''' test rb tree '''
    rbt = RedBlackTree()

    rbt.add(5)
    rbt.add(10)
    rbt.add(30)
    rbt.add(3)
    rbt.add(13)

    print("PRE ORDER TRAVERSAL")
    print("===================\n")
    i = 0
    for node in rbt:
        if i == 0:
            print("ROOT: " + str(node))
        else:
            print(node)
        i += 1

if __name__ == '__main__':
    main()
