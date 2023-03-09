# REGEX Exercise 2

1. Had to replace `&`, `<`, and `>`. 
    1. Find `&`
    1. Replace `&amp;`,
    1. `<` and `>` were not found
1. Remove the extra blank lines
    1. Find `\n\n+`
    1. Replace `\n`
1. Mark long lines of text with the `p` element
    1. Find `^.+`
    1. Replace `<p>\0</p>`
    1. This covers chapter titles and book info with the `p` element, which can be changed later
1. Find chapter titles and wrap them with `heading` elements
    1. Find `^.+(CHAPTER [IVXCL]+).+$`
    1. Replace `<heading>\1</heading>`
1. Wrap entire chapters in `chapter` elements
    1. Find `^<heading>CHAPTER [IVXCL]+</heading>$`
    1. Replace `</chapter>\n<chapter>\n\0`
    1. Delete first `chapter` endtag and add one at the end of the document
1. Wrap quotes with the `quote` element, swapping it for doublequotes
    1. Find `"(.+?)"`
    1. Replace `<quote>\1</quote>`
1. Cleanup
    1. Fix `title` element
    1. Add root element