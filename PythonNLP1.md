# Python NLP Findings
I really wasn't able to spend as much time on this assignment as I wanted to. These are just observations I made.

For this assignment, I've used the Stardew Valley .txt files. XML files had 
more content and files to go through, but results were plagued by words that had been mashed together or had letters added on, making several useless topics. I would not change the number of topics and would keep them at 25.

The text files were interesting to work with. Besides having significantly
fewer errors, only 34 documents were available.

The first visualization made used the top 30 most relevant terms among 25 topics. The first 10 topics were larger than the rest, and all topics were scattered in the middle range moving towards the center after each.
I changed the stop word list to try and prevent topic 1 from taking 44% of all tokens. 
 I could not get a good distribution of topics and sizing. The first topics would increase in size while the rest would shrink. I decided to instead stick with changing the # of terms.

I was curious as to how this would change with a selection of fewer/more
relevant terms. The first change I made was restricting topics to the 10 most relevant terms. The results showed topics being spread out evenly, although sizing remained heavily with the first topic. Topic 1 accounted for 51.6% of tokens, the 2nd took 18.5%.

I moved on to find the results of the 50 most relevant terms. The visualization had provided a less dispersed topic model, but it was still generally acceptable. On the left side a large Ven diagram had been made with the first 3 topics. Each topic was ~25% of all tokens.

Although the text files were better than the xml files, as word relevance decreased more conjoined words would appear. This was an issue for all topics but was most prevalent with smaller topics, as these errors did not repeat often

