# --- Day 3: Perfectly Spherical Houses in a Vacuum ---

Santa is delivering presents to an infinite two-dimensional grid of houses.

He begins by delivering a present to the house at his starting location, and then an elf at the North Pole calls him via radio and tells him where to move next. Moves are always exactly one house to the north (`^`), south (`v`), east (`>`), or west (`<`). After each move, he delivers another present to the house at his new location.

However, the elf back at the north pole has had a little too much eggnog, and so his directions are a little off, and Santa ends up visiting some houses more than once. How many houses receive **at least one present**?

For example:

- `>` delivers presents to `2` houses: one at the starting location, and one to the east.
- `^>v<` delivers presents to `4` houses in a square, including twice to the house at his starting/ending location.
- `^v^v^v^v^v` delivers a bunch of presents to some very lucky children at only `2` houses.

Your puzzle answer was `2081`.
## --- Part Two ---

The next year, to speed up the process, Santa creates a robot version of himself, Robo-Santa, to deliver presents with him.

Santa and **Robo-Santa** start at the same location (delivering two presents to the same starting house), then take turns moving based on instructions from the elf, who is eggnoggedly reading from the same script as the previous year.

This year, how many houses receive **at least one present**?

For example:

- `^v` delivers presents to `3` houses, because Santa goes north, and then Robo-Santa goes south.
- `^>v<` now delivers presents to `3` houses, and Santa and Robo-Santa end up back where they started.
- `^v^v^v^v^v` now delivers presents to `11` houses, with Santa going one direction and Robo-Santa going the other.

Your puzzle answer was `2341`.

**Both parts of this puzzle are complete! They provide two gold stars: ****

At this point, you should return to your Advent calendar and try another puzzle.

If you still want to see it, you can [get your puzzle input](https://github.com/PetitPotiron/advent-of-code-2015/blob/main/src/day-3/input.txt).

## How I solved it
### First part
As santa delivers presents to an infinite grid of houses, we can name each house with coordinates. I choose a house, which I call (x=0, y=0) and then, Santa goes up (y+=1), down (y-=1), right (x+=1) or left (x-=1). I save the list of all visited houses. I transform it into a `set` to avoid duplicates, and I count the number of unique house in the list.
### Second part
The process is quite the same as the first part, only I have to save two lists, one for robo santa and one for santa. I also need a variable which tells me whether it's Santa or Robo Santa's turn to move.
Finally, I count all visited houses, without any duplicates thanks to the `set`.
