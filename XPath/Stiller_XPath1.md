# XPath Exercise 1

How can XPath tell apart the acts and the scenes?
1. `//div/head`

What XPath would find just the acts?
1. `//body/div/head`

What XPath would find just the scenes?
1. `//div/div/head`
 
What XPath would find just the scenes inside Act II? (The Results window for the previous questions will give you a good clue: look at the numbers inside square brackets.)
1. `//div[2]/div/head`



Write an XPath to find all the stage directions in the document wherever they may be.
1. `//stage`

Write an XPath to reach into Act 3 and find all the stage directions inside that act.
1. `//div[3]//stage

What XPath would find all of the stage directions that are nested inside a metrical line (<l>), that is, between the starting <l> and the ending </l>? How many stage directions are inside lines?
1. `//l/stage`

What XPath would find all of the stage directions that are nested directly inside a speech (<sp>) and outside of the lines within a speech?
1. `//sp/stage`

Run the XPath that finds all the stage directions wherever they are in the whole play again and study the results. Look for stage directions that are not inside a speech (<sp>) or metrical line (<l>). What other element holds stage directions when they are not inside a speech or line?
1. `<div>`

Now, can you write a simple XPath expression that returns all of the stage directions that are not inside a speech or a line? (Check your Results window to make sure none of them are nested inside a speech or line.) How many are there?
1. `//stage[not(parent::l or parent::sp)]`, `22`



Write an XPath to find all the speeches (<sp>) and then step over to isolate their @who attributes. (The Results window shows you just the attribute values.) Record your XPath expression.
1. `//sp/@who`

Often we use attributes in XPath to filter elements, and isolate, say, only the speeches spoken by a particular character. To filter results, we use a predicate expression written inside square brackets. Look for examples of predicates in our XPath tutorial that filter elements based on their attributes. Then write an XPath expression with a predicate to return all of the speeches in the play spoken by Prospero. Record your expression and how many results you get. Try changing the speaker to Miranda: how many speeches are spoken by her?
1. `//sp[@who='Prospero']`, `114`
1. `//sp[@who='Miranda']`, `50`