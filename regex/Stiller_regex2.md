# REGEX Exercise 2

1. Find ```&``` Replace ```&amp;```, nothing was found for ```&```, ```<```, or ```>```
1. Normalizing the leading space characters, Find ```^ +``` Replace with nothing
1. Leave the blank newlines in the document
1. Add ```<line>``` to each line that isn't empty, Find ```^.+``` Replace ```<line>\0</line>```
1. Wrap all lines with ```<sonnet>``` and add ```number``` attribute, Find ```^<line>[IVXLC]+</line>$``` Replace ```</sonnet>\n<sonnet number="\1">```
1. Delete first ```</sonnet>``` endtag and add ```</sonnet>``` to end of doc
1. Wrap everything with ```<xml>``` by Ctrl+E