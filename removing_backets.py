"""
Let's consider a problem to remove brackets from an algebraic expression
In a mathematics class, Jason the maths teacher asked to solve a book of expressions consisting of characters,
 operators, and brackets.
But Jason wants to give simplified expressions by removing brackets from the expressions.
Write an algorithm to help Jason simplify an expression by removing brackets.

Input: Consists of a string expression, representing an expression
(x + (y - z)) * t
Output: Return a string representing the simplified expression by removing brackets.
x + y - z * t
"""

n = input("Enter an algebraic expression: ")

for i in n:
    if i not in "()":  # checks if the character is not either an opening bracket or closing bracket
        print(i, end=" ")
