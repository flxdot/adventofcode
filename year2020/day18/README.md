# Advent of Code 2020 - Day 18

Solution for this day: [year2020day18.py](year2020day18.py)

My input for this day: [input.txt](input.txt)

## \--- Day 18: Operation Order ---

As you look out the window and notice a heavily-forested continent slowly
appear over the horizon, you are interrupted by the child sitting next to you.
They're curious if you could help them with their math homework.

Unfortunately, it seems like this "math" [follows different
rules](https://www.youtube.com/watch?v=3QtRK7Y2pPU&t=15) than you remember.

The homework (your puzzle input) consists of a series of expressions that
consist of addition (`+`), multiplication (`*`), and parentheses (`(...)`).
Just like normal math, parentheses indicate that the expression inside must be
evaluated before it can be used by the surrounding expression. Addition still
finds the sum of the numbers on both sides of the operator, and multiplication
still finds the product.

However, the rules of _operator precedence_ have changed. Rather than
evaluating multiplication before addition, the operators have the _same
precedence_ , and are evaluated left-to-right regardless of the order in which
they appear.

For example, the steps to evaluate the expression `1 + 2 * 3 + 4 * 5 + 6` are
as follows:

    
    
    _1 + 2_ * 3 + 4 * 5 + 6
      _3   * 3_ + 4 * 5 + 6
          _9   + 4_ * 5 + 6
             _13   * 5_ + 6
                 _65   + 6_
                     _71_
    

Parentheses can override this order; for example, here is what happens if
parentheses are added to form `1 + (2 * 3) + (4 * (5 + 6))`:

    
    
    1 + _(2 * 3)_ + (4 * (5 + 6))
    _1 +    6_    + (4 * (5 + 6))
         7      + (4 * _(5 + 6)_ )
         7      + _(4 *   11   )_
         _7      +     44_
                _51_
    

Here are a few more examples:

  * `2 * 3 + (4 * 5)` becomes _`26`_.
  * `5 + (8 * 3 + 9 + 3 * 4 * 3)` becomes _`437`_.
  * `5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))` becomes _`12240`_.
  * `((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2` becomes _`13632`_.

Before you can help with the homework, you need to understand it yourself.
_Evaluate the expression on each line of the homework; what is the sum of the
resulting values?_



Source: [https://adventofcode.com/2020/day/18](https://adventofcode.com/2020/day/18)
