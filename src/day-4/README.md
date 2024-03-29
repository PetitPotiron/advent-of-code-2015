# --- Day 4: The Ideal Stocking Stuffer ---

Santa needs help [mining](https://w.wiki/8E3z) some AdventCoins (very similar to [bitcoins](https://w.wiki/8E43)) to use as gifts for all the economically forward-thinking little girls and boys.

To do this, he needs to find [MD5](https://w.wiki/8E45) hashes which, in hexadecimal, start with at least **five zeroes**. The input to the MD5 hash is some secret key (your puzzle input, given below) followed by a number in decimal. To mine AdventCoins, you must find Santa the lowest positive number (no leading zeroes: `1`, `2`, `3`, ...) that produces such a hash.

For example:
- If your secret key is `abcdef`, the answer is `609043`, because the MD5 hash of `abcdef609043` starts with five zeroes (`000001dbbfa...`), and it is the lowest such number to do so.
- If your secret key is `pqrstuv`, the lowest number it combines with to make an MD5 hash starting with five zeroes is `1048970`; that is, the MD5 hash of `pqrstuv1048970` looks like `000006136ef...`.

Your puzzle answer was `254575`.
## --- Part Two ---

Now find one that starts with **six zeroes**.

Your puzzle answer was `1038736`.

**Both parts of this puzzle are complete! They provide two gold stars: \*\***

Your puzzle input was `bgvyzdsv`.

## How I solved it
### First part
I used a method called brute-force. Brute-forcing is the action of trying each possibility, until one works. HEre, I try each number until one provides me a MD5 hash starting with five zeroes.
### Second part
I use the same strategy for the second part, but I look this time for the first number which provides me a 6-zeroes-starting MD5 hash.
