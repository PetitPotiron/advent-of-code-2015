# --- Day 1: Not Quite Lisp ---

Santa was hoping for a white Christmas, but his weather machine's "snow" function is powered by stars, and he's fresh out! To save Christmas, he needs you to collect **fifty stars** by December 25th.

Collect stars by helping Santa solve puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants **one star**. Good luck!

Here's an easy puzzle to warm you up.

Santa is trying to deliver presents in a large apartment building, but he can't find the right floor - the directions he got are a little confusing. He starts on the ground floor (floor  `0`) and then follows the instructions one character at a time.

An opening parenthesis, `(`, means he should go up one floor, and a closing parenthesis, `)`, means he should go down one floor.

The apartment building is very tall, and the basement is very deep; he will never find the top or bottom floors.

For example:

- `(())` and `()()` both result in floor `0`.
- `(((` and `(()(()(` both result in floor `3`.
- `))(((((` also results in floor `3`.
- `())` and `))(` both result in floor `-1` (the first basement level).
- `)))` and `)())())` both result in floor `-3`.

To **what floor** do the instructions take Santa?

Your puzzle answer was `138`.

The first half of this puzzle is complete! It provides one gold star: *

## --- Part Two ---
Now, given the same instructions, find the position of the first character that causes him to enter the basement (floor -1). The first character in the instructions has position 1, the second character has position 2, and so on.

For example:

    ) causes him to enter the basement at character position 1.
    ()()) causes him to enter the basement at character position 5.

What is the position of the character that causes Santa to first enter the basement?

Although it hasn't changed, you can still [get your puzzle input](https://github.com/PetitPotiron/advent-of-code-2015/blob/main/src/day-1/second-part/input.txt).

## How I solved it
* Santa begins on floor `0` and then moves. Let's create a `floor = 0` variable to keep track of its level!
* Now, let's read the instructions with the python `open(filename)` and `file.read()` methods.
* As Santa goes through one instruction at a time, let's use a `for loop` to iterate over each instruction. But as we look for the position of the first instruction which causes Santa to enter the basement, we will use the python `enumerate()` function, which provides the element and its position in the instructions (you'll see later it is useful).
* If the instruction is `(`, Santa moves up. I then add `1` to the `floor` variable I created.
* Otherwise, the instruction is obviously `)`. Santa moves then down, so I remove `1` to the `floor` variable.
* Now, let's check if Santa is at floor `-1`, the basement! If so, we print the position of the instruction which caused Santa to enter the basement (we then use the `break` keayword to make sure we don't continue to follow the instructions). Else, we continue to loop until it's the case!
