HW_SOURCE_FILE = __file__


def summation(n, term):
    """Return the sum of numbers 1 through n (including n) wíth term applied to each number.
    Implement using recursion!

    >>> summation(5, lambda x: x * x * x) # 1^3 + 2^3 + 3^3 + 4^3 + 5^3
    225
    >>> summation(9, lambda x: x + 1) # 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
    54
    >>> summation(5, lambda x: 2**x) # 2^1 + 2^2 + 2^3 + 2^4 + 2^5
    62
    >>> # Do not use while/for loops!
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'summation',
    ...       ['While', 'For'])
    True
    """
    assert n >= 1
    accumulation = 0 #used to store moving sum
    #the term indexes  will be kept track of throughout the helper() calls as a parameter
    def helper(counter, term):
        nonlocal n, accumulation
        #base case for recursive calls
        if counter > n: #point of trouble: needs to be '>' to avoid terminating recursion early
            return accumulation
        else:
            accumulation += term(counter)
            return helper(counter + 1, term)

    return helper(1,term)



def pascal(row, column):
    """Returns the value of the item in Pascal's Triangle
    whose position is specified by row and column.
    >>> pascal(0, 0)
    1
    >>> pascal(0, 5)	# Empty entry; outside of Pascal's Triangle
    0
    >>> pascal(3, 2)	# Row 3 (1 3 3 1), Column 2
    3
    >>> pascal(4, 2)     # Row 4 (1 4 6 4 1), Column 2
    6
    """
    def make_row (counter):
        if counter == 0:
            return [1]
        else:
            #all rows start with 1
            new_row = [1]
            #recursive call to previous row
            previous_row = make_row(counter - 1)
            #pad previous row with 0 to always get 1 at the end of new row
            old_row = previous_row + [0]
            for i in range(0, len(previous_row)):
                new_row.append(old_row[i]+old_row[(i+1)])
            return new_row

    if column > row: #make sure position selection is valid
        return 0
    else:
        target_row = make_row(row)
        return target_row[column]


def compose1(f, g):
    """"Return a function h, such that h(x) = f(g(x))."""
    def h(x):
        return f(g(x))
    return h


def repeated(f, n):
    """Returns a function that takes in an integer and computes
    the nth application of f on that integer.
    Implement using recursion!

    >>> add_three = repeated(lambda x: x + 1, 3)
    >>> add_three(5)
    8
    >>> square = lambda x: x ** 2
    >>> repeated(square, 2)(5) # square(square(5))
    625
    >>> repeated(square, 4)(5) # square(square(square(square(5))))
    152587890625
    >>> repeated(square, 0)(5)
    5
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'repeated',
    ...       ['For', 'While'])
    True
    """
    if n == 1:
        return f
    elif n == 0:
        return lambda x: x
    else:
        return compose1(f,repeated(f, n-1))
