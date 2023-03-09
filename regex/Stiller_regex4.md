# REGEX Exercise 4

I want to take a text file for one of the main characters and strip it of code and unnecessary data. I've combined all the files for Emily to create more to work with.

We need to select all the data before and including the line with `content:`. I want to try and do this with regex, although it is short enough to just delete manually if needed.

`xnbData:((.+)|(\n+))+` will select every character or newline starting from `xnbData`, which is the starting point of the stuff we don't want. Just restrict it from deleting what we want by adding something to the end.

Did some more looking and found lookarounds [here](https://www.regular-expressions.info/lookaround.html). They helpfully show that `(?={pattern})` looks ahead in a document and `(?<={pattern})` looks behind. Using both expressions can look for something between the two patters (and maybe the inverse?)

1. Took way too long to come up with this and too many searches. Delete any data not part of the dialogue.
    1. Find `(?=xnb)[\s\S]+?(?<=>)`
    1. Replace `</file>\n<file type="">`
    1. Cleanup `file` element by removing first endtag, adding one at the end, and filling the type attribute
1. Normalize newlines, get rid of indents
    1. Find `\n\n+`
    1. Replace `\n`
    1. Find `^ +`
    1. Replace with nothing
1. Swap and replace `&`. 
    1. Find `&`
    1. Replace `&amp;`,
1. Wrap each dialogue with `quote` element and `type` attribute using the preceeding text
    1. Find `(.+): "(.+)"`
    1. Replace `<quote type="\1">\2</quote>`
1. Cleanup by adding a root element
