# /bin/python

def check_post_order(ray):
    if len(ray) < 2:
        return True

    # last element of the ray is the root
    root = ray[-1]

    # find left child (first node to appear to the left that is smaller)
    l = len(ray) - 2
    while l != -1 and ray[l] > root:
        l -= 1

    # find the right child (should be first node on the left)
    r = len(ray) - 2
    while r != -1 and ray[r] < root:
        r -= 1
    if l == -1 or r == -1:
        return check_post_order(ray[:-1])
    elif l > r:
        return False
    else:
        return check_post_order(ray[:l+1]) and check_post_order(ray[l+1:r+1])


ray = [3, 5, 7, 6, 9, 12, 11, 10, 8]
print check_post_order(ray)
ray = [8, 6, 5, 3, 7, 10, 9, 11, 12]
print check_post_order(ray)
ray = [3, 5, 6, 7, 8, 9, 10, 11, 12]
print check_post_order(ray)
