def print_subsets(n):
    # Generate all subsets of the natural numbers up to n
    for i in range(1, 2 ** n):
        # Convert the binary representation of i to a set of included natural numbers
        """
        bin(i) convert binary number from integer  and take second index then reverse
        """
        subset = set([j + 1 for j, b in enumerate(bin(i)[2:][::-1]) if int(b)])
        print(subset)


print_subsets(3)