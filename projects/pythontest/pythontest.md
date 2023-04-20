# Python Test
## Overview
The code inside of `strdw-files-stage5.py` is modeled off code by Dr. B's `lotr-files-stage5.py` and code from the (Stardew Valley Text Analysis Project)[https://github.com/gak5275/StardewDIGIT210]. I sampled xml files from this project, as well as used some existing autotagging python code to adapt Dr. B's example.

## Purpose 
The purpose of this python code is to automatically tag xml code based on 'persons' and 'locations' from the collection. Some entities have already been defined from the Stardew Valley Text Analysis Project's `GraydonAutotagging.py`. Others are found through the functions but are more likely to be wrong. The code uses 5 different functions to autotag the xml and produce a text document with all entities found inside the collection. The order of functions is as follows:

[![](https://mermaid.ink/img/pako:eNqNkL9ugzAQh1_F8tRKyQswVKKJmRKGwFApZDjsA6z4T2UOJRHi3WtCJNShUj2dfd9995NHLr1CnvDG-JvsIBA7nCrH4oFzUaan8sK22w-WvmWDk6S9Y9D3aGuDqTE5WOzfn0A9Zj4wBNmxuzWs0Qan2Pg6HlgW635mPldJQFAl3unZWwy7tYuOND123hiU5MNrwxKrjpfcs6MPyH7Z1Tp_C5qw8IFQiVml445legbFP6LiKotMCW2LrxhiEYm_YmRnke8vC8Q33GKwoFX84XF-qzh1aLHiSSwVhGvFKzdFDgbyxcNJnlAYcMOHbwWEew1tAMuTBkyP0w8Ff4l3?type=png)](https://mermaid.live/edit#pako:eNqNkL9ugzAQh1_F8tRKyQswVKKJmRKGwFApZDjsA6z4T2UOJRHi3WtCJNShUj2dfd9995NHLr1CnvDG-JvsIBA7nCrH4oFzUaan8sK22w-WvmWDk6S9Y9D3aGuDqTE5WOzfn0A9Zj4wBNmxuzWs0Qan2Pg6HlgW635mPldJQFAl3unZWwy7tYuOND123hiU5MNrwxKrjpfcs6MPyH7Z1Tp_C5qw8IFQiVml445legbFP6LiKotMCW2LrxhiEYm_YmRnke8vC8Q33GKwoFX84XF-qzh1aLHiSSwVhGvFKzdFDgbyxcNJnlAYcMOHbwWEew1tAMuTBkyP0w8Ff4l3)
**Notes:** 
1. This Flowchart ignores code outside of functions 
2. Entities from *Function entityCollector* is pulled by *Function writeSortedEntities* after all files are read

## Function: assembleAllNames
The function *assembleAllNames* is the first function defined, called, and contains calls to all other functions. It operates as the main function.

It starts finding all files in the collection directory ending with '.xml'. A variable `filepath` is created using the collection's directory name and the file's name. `Filepath` is then sent to the function *readTextFiles*.

**Call function *readTextFiles*, Returned `dictEntities`**

For each file, a `dictEntities` is returned. Each dictionary is added to `AllNames`, another dictionary. The `AllNames` dictionary keys are then made into a list and sorted alphabetically, making `SortedDict`. The function *writeSortedEntries* is called with the argument `SortedDict`.

**Call function *writeSortedEntries***

Another for loop is made finding all files in the collection directory ending with '.xml'. A variable `sourcePath` is made the same as `filepath`. The function *xmlTagger* is called upon with the arguements `sourcePath` and `SortedDict`.

**Call function *xmlTagger***

## Function: readTextFiles
The Function starts by using the Saxonche processor to read the XML through xpath expressions. Line 115 `xpath = xp.evaluate('//dialogue ! normalize-space() => string-join()')` was copied from `GraydonAutotagging.py`. This line selects text in the dialogue elements. Then, all spaces are normalized and each instance is joined into one long saxonche.PyXdmValue node. This node type cannot be used by python, so it is converted back into a string.

This string is then cleaned up using regex expressions in python:
''' python
cleanedUp = regex.sub(r"/|\^", r" ", string)
cleanedUp = regex.sub(r"(\w[!,\?,\.,\*])(\S)", r"\1 \2", cleanedUp)
cleanedUp = regex.sub(r"'([A-Z])]", r" \1", cleanedUp)
cleanedUp = regex.sub(r"(\.) (\.\.)", r"\1\2", cleanedUp)
cleanedUp = regex.sub(r"(\.) ('s)", r"\1\2", cleanedUp)
'''

This removes any metadata characters that might have been left behind, and properly adds spaces where they might have been missed. At this point, the variable `cleanup` has all text formatted and cleaned in one continuous string. Then, the string is converted into `tokens`. `Tokens` is a class usable by the spaCy processor., where it is sent off to the function *entityCollector*. 

**Call function *entityCollector*, Returned `entities`**

After *entityCollector* returns a dict of entities for one file, `dictEntities` takes this dict and is returned to *assembleAllNames*.

**Return `dictEntities`**

## Function: entityCollector
Inside of *Function readTextFiles*, the funciton *entityCollector* is called upon before the function ends. Here, specific entities are found by spaCy and made into a dict class of strings. 

`Entities` is first defined as an empty dict. To be placed in the dict, a few things have to happen. Each instance of an entity in `tokens` has to 

1. have an entity label equal to one of the few specified (i.e., LOC 'location', ORG 'organization', PERSON, etc.)
1. and the text corresponding to that entity cannot be matching the regex expression '''regex
\w*[.,!?;:']\w*
'''

If an entity identified by spaCy passes these two checks, the text corresponding to that entity and its label are added to the dict `entities`. The `entities` dict is then returned back to *readTextFiles*.

**Return entities**

## Function: writeSortedEntries
This is the shortest function at 5 lines. It writes to a file `StillerAutotag.txt` the key and value of each entity in the collection. If `StillerAutotag.txt` is not an existing file, one is created. 

## Function: xmlTagger
The final function, *xmlTagger*, tags the xml and creates a copy in another folder. 

From *assembleAllNames*' for loop, the current filename and target path are taken to get the location for a tagged XML file. This is what forms `targetFile`.

Next, the file from the XML collection is read and converted to a string: `stringFile`. For each of the keys and value in the `SortedDict`, a variable `replacement` places the key and value into a xml structured `name` element with `type` attribute. These changes are applied to `stringFile`. Unwanted changes are then reverted using regex.

```python
cleanedStringFile = regex.sub(r"(<\w+? \w+?=.)<name type=\"\w+?\">(\w+?)</name>(\")", r"\1\2\3", stringFile)
```
The code above was copied from `GraydonAutotagging.py`.

After the xml code in a string is complete, it is made into a xml document using the target path: `targetFile`.

After each file has gone through the function *xmlTagger*, no more funcitons are called and nothing is returned. The python script ends.