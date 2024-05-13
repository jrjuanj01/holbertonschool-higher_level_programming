#!/ustr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for nums in matrix:
        idx = 0
        for num in nums:
            if idx < (len(nums)-1):
                print("{:d}".format(num), end=" ")
                idx += 1
            else:
                print("{:d}".format(num))
