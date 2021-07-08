# psuedo code
#     10
#    /  \
#   6    12
#  /
# 4

# IBH method
def height(root):
    parent_node = root
    if parent_node is None:
        return 0
    left_tree_height = height(parent_node.left)
    right_tree_height = height(parent_node.right)

    # we need to add 1 because from right and left child node we are further calculating height, so we are
    # already down with 1 step, that's why we need to include
    return 1 + max(left_tree_height, right_tree_height)
