# About

Go to source: [link](https://www.codewars.com/kata/5962bbea6878a381ed000036/)

You just got done writing a function that calculates the player's final score for your new game, "Flight of the cockatoo". Now all you need is a high score table that can be updated with the player's final scores. With such a feature, the player will be motivated to try to beat his previous scores, and hopefully, never stop playing your game. The high score table will start out empty. A limit to the size of the table will be specified upon creation of the table. Here's an example of the expected behavior of the high score table:

```
highScoreTable = HighScoreTable(3)
highScoreTable.scores == [] # evaluates to True
highScoreTable.update(10)
highScoreTable.scores == [10]
highScoreTable.update(8)
highScoreTable.update(12)
highScoreTable.update(5)
highScoreTable.update(10)
highScoreTable.scores == [12, 10, 10]
highScoreTable.reset()
highScoreTable.scores == []
# And so on...
```

# Test

Run the following on terminal:

```
python3 -m unittest test_main.py
```

If passed, the result should look like the following:

```
.........
----------------------------------------------------------------------
Ran 9 tests in 0.000s

OK
```