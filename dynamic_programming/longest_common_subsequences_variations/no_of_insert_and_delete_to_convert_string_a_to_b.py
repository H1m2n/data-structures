# Problem:
# we have given 2 strings we need to find out optimal number of insertion and deletion, to convert string a to b


a = "heap"
b = "pea"

# How it is LCS?
# Things that are common that will be as it is but just to make convert a to b we need some deletion from a string
# and some insertion from b string

#     a ------> b
#       \
#   LCS= ea

# from a we have removed h and p and in LCS insert p at starting

# so answer will be --->
# no of deletion = len(a) - LCS
# no of insertion = len(b) - LCS
