def treSum(tree):
    if tree is None:
        return 0
    else:
        left_sum= treSum(tree.left)
        right_sum = treSum(tree.right)
        return tree.val +left_sum +right_sum

#iteration
def Tree_sum(tree):
    stack =[]
    output = [None]
    stack.append(('call', tree, output,[None], [None]))
    while stack:
        action, node, ret, left, right=stack.pop()
        if action == 'call' :
            if node is None:
                ret[0]=0
            else:
                stack.append(('resume', node,ret,left, right))
                stack.append(('call', node.right, left, [None], [None]))
                stack.append(('call', node.left, right, [None], [None]))
        else:
            ret[0]=node.val+left[0]+right[0]
    return output[0]

