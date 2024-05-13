#!/ustr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for nums in matrix:
        for idx in range(len(nums)):
            print("{:d}".format(nums[idx]), end="")
            if idx < len(nums) - 1:
                print(" ", end="")
        print()