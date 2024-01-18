# this only works for trees with 3 values (probably maybe) (preorder might work with more than 3 maybe)
tree = {
    0: [1, 2, "A"],
    1: [-1, -1, "B"],
    2: [-1, -1, "C"]
}

output = []

choice = int(input('What traversal would you like to demonstrate?\n1) Pre-order\n2) In-order\n3) Post-order\n'))

def preorder():
    pos = 0
    output.append(tree[pos][2])
    while pos != len(tree) - 1:
        pos += 1
        output.append(tree[pos][2])

def inorder():
    pos = len(tree) // 2
    output.append(tree[pos][2])
    pos -= 1
    output.append(tree[pos][2])
    if pos == 0:
        pos += 2
        output.append(tree[pos][2])

def postorder():
    pos = len(tree) - 1
    output.append(tree[pos][2])
    if pos == 2:
        pos -= 2
        output.append(tree[pos][2])
        pos += 1
        output.append(tree[pos][2])

if choice == 1:
    while len(output) != len(tree):
        preorder()
    print(output)

if choice == 2:
    while len(output) != len(tree):
        inorder()
    print(output)

if choice == 3:
    while len(output) != len(tree):
        postorder()
    print(output)