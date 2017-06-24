""" Project Euler Problem 42
========================

The n-th term of the sequence of triangle numbers is given by, t[n] =
1/2n(n+1); so the first ten triangle numbers are:

                 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its
alphabetical position and adding these values we form a word value. For
example, the word value for SKY is 19 + 11 + 25 = 55 = t[10]. If the word
value is a triangle number then we shall call the word a triangle word.

Using words.txt, a 16K text file containing nearly two-thousand common
English words, how many are triangle words?
"""


def word_value(word):
    """word is alrady upper case"""
    a = ord('A')
    return sum([ord(char) - a + 1 for char in word])

# Test
assert word_value('SKY') == 55


def t(n):
    return (n*(n+1))//2

# Tests
assert t(1) == 1
assert t(4) == 10
assert t(10) == 55


def read_words(path='resources/p042_words.txt'):
    words = []
    with open(path) as f:
        content = f.read()
        quoted_words = content.split(',')
        words = [q[1:-1] for q in quoted_words]
    return words


def main():
    words = read_words()
    scores = [word_value(word) for word in words]
    triangle_numbers = [t(n+1) for n in range(int(max(scores)))]
    triangle_word_scores = [s for s in scores if s in triangle_numbers]
    return len(triangle_word_scores)

if __name__ == '__main__':
    print(main())
