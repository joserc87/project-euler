"""
Project Euler Problem 39
========================

If p is the perimeter of a right angle triangle with integral length
sides, {a,b,c}, there are exactly three solutions for p = 120.

                    {20,48,52}, {24,45,51}, {30,40,50}

For which value of p < 1000, is the number of solutions maximised?
"""

# THOUGHTS:
#
# * p < 1000 => sides < 500
# * for a triangle with sides a, b, c => a*a + b*b = c*c
# * side < 500 => side*side < 250000. We can precalculate the list of squares
# * if a2=a*a, b2=b*b and c2=c*c, we cann pick a2 and b2 from the list of
#   squares and check if a2+b2 is in the list of squares.


def possible_right_triangles(max_perimeter):
    """
    Returns the possible triangles for each perimeter (list of list of tuples)
    """
    triangles = [[] for _ in range(max_perimeter+1)]
    squares = [i*i for i in range(max_perimeter//2 + 1)]
    # Find the triangles (where b>=a)
    for b, b2 in enumerate(squares):
        for a, a2 in enumerate(squares):
            if a > b:
                break
            if a*b != 0:
                c2 = a2 + b2
                if c2 in squares:
                    c = squares.index(c2)
                    perimeter = a + b + c
                    if perimeter <= max_perimeter:
                        triangles[perimeter] += [(a, b, c)]
    return triangles


def perimeter_with_more_triangles(max_perimeter):
    triangles = possible_right_triangles(max_perimeter)
    lens = [len(l) for l in triangles]
    return lens.index(max(lens))

if __name__ == '__main__':
    triangles = possible_right_triangles(1000)
    print(perimeter_with_more_triangles(1000))
