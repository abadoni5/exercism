"""
Approach:
- The provided code defines a function, tree_from_traversals, that constructs a binary tree from its preorder and inorder traversals.
- It first checks for validity conditions such as the lengths of the traversals being equal, containing the same elements, and unique elements.
- Then, it calls the build_tree function which recursively constructs the binary tree.
"""

def build_tree(preorder_traversal, inorder_traversal):
    if len(preorder_traversal) == 0:
        return {}
    root_val = preorder_traversal.pop(0)
    root_index = inorder_traversal.index(root_val)
    inorder_traversal.pop(root_index)
    return {
        'v': root_val, 
        'l': build_tree(preorder_traversal[:root_index], inorder_traversal[:root_index]),
        'r': build_tree(preorder_traversal[root_index:], inorder_traversal[root_index:])}
        
    
def tree_from_traversals(preorder, inorder):
    if len(preorder) != len(inorder):
        raise ValueError("traversals must have the same length")
    if set(preorder) != set(inorder):
        raise ValueError("traversals must have the same elements")
    if len(preorder) != len(set(preorder)):
        raise ValueError("traversals must contain unique items")
    return build_tree(preorder, inorder)
