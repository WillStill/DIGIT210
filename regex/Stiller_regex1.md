# REGEX Exercise 1

1. Find ```&``` Replace ```&amp;```, neither ```<``` or ```>``` were found
1. Surround each line with the movie tag, Find ```^(.+)$``` Replace ```<movie>\1</movie>```
1. Surround titles with title element, Find ```(<movie>)(.+?)\t``` Replace ```\1<title>\2</title>\t```
1. Add date element, Find ```\t(.+?)\t``` Replace ```\t<date>\1</date>\t```
1. Add location element, Find ```\t(".+"?)\t``` Replace ```\t<location>\1</location>\t```
1. Add time element, Find ```\t(\d+\D+)(</movie>)$``` Replace ```\t<time unit="min">\1</time>\2```