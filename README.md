# Calculator

A work-in-progress calculator that's still not done but functional enough to put up and have at
least a small feeling of accomplishment.


Note: the order of operations is just left to right with no operator having precedence over
another. The left-to-right order is overridden with parentheses. For example:

1 + 2 * 3 ^ 4 is ((1 + 2) * 3) ^ 4 not 1 + (2 * (3 ^ 4))

1 + 2 * (3 ^ 4) is (1 + 2) * (3 ^ 4) not 1 + (2 * (3 ^ 4))

That's jus' how I do! ;)


Possible future updates to Calculator:

1. Custom symbols for the operators. Maybe a whole custom font. Probably using FontStruct. Might
be really difficult with tkinter. So might have to give PyQt a go....

2. Custom symbols for the digits between and including 10 and 64 so that all the bases between
and including 17 and 64 can be added. That's a shit load of buttons though.... Could try to hide
'em when not in use....

3. Maybe make the GUI more tile-like or somethin'.... Purdy it up....
