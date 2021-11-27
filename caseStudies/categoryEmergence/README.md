# Case study 1 – Category creation and interaction in online communities

<center><img src='images/picture.jpeg' width=600px /></center>

# Introduction

There are two types of product innovations: innovations that are new to a company and innovations that are new to the world.[1] The latter type of innovation is by far the most challenging to pursue because it requires firms to cope with radically new technologies and to create a new market. iPhone/Pad/Pod, electronic cigarettes, cars or rock music (to go back to early XX century) are iconic examples of category-creating innovations.[2]

<center>
<img src='images/iphone.jpg' width=600px/>

<b> Figure 1: 2007, Apple launches the iPhone </b>
</center>

# Context for the case study

According to the prior literature and empirical evidence category-creating innovations show peculiar characteristics[3]. For example:

- they have a high-risk and high-reward structure
- product positioning poses peculiar marketing challenges
  * lack of familiarity - consumers don't understand the features of the proposed innovation
  * confusion in evaluation - consumers don't have reference points to assess the quality of the proposed innovation
  * competency discount – consumers don't trust the innovator credibly masters the knowledge/technology from distant domains. In 2007: Apple producing phones? Are you kidding me?

Prior studies have started to articulate the role communities of enthusiasts can play in promoting category creating products. However, we have a very limited knowledge of how innovators can leverage upon these communities, possibly, just a few individuals, to sustain the diffusion of their innovations.

# Problem to address

Electric vehicles are widely considered as a category-creating product. Talking about data, there are several data sources that can be used to explore/articulate the role of enthusiasts in facilitation the diffusion of electric vehicles. For example, Reddit is the home of many communities of enthusiasts, including motor-heads such as r/autors, r/cars, r/electricvehicles. Not only, there are several specialized forums wherein people share their passion for cars. Use [this datadump](https://github.com/simoneSantoni/net-analysis-smm638/blob/master/data/c4p.zip) containing on-line interactions among car enthusiasts (companion documents included in the folder), to address the following questions:

- in network terms, what is the main obstacle to the diffusion of positive opinion/sentiment toward electric vehicle?
- is there any node/group of nodes to rely upon in order to facilitate the diffusion of electric vehicles?

# Data

Here is a minimal description of the data included in the dump.

## Source

Data have been crawled from the forum of [Car4play](http://www.car4play.com/forum)

## Data tables

+ `c4p_thread_list.csv`: population of threads
+ `cp4_thread.csv`: messages included in the threads (some minimal cleaning operated within the [Scrapy](https://scrapy.org/) pipeline that crawls the data; overall, the text has some garbage). This file includes the 2-mode network linking authors with threads
+ `c4p_spacy_output.csv`: messages included in threads in lemmatized form (the text corpora has been passed through a [spaCy](https://spacy.io/) NLP pipeline) along with sentiment scores  (computed with the [spaCyTextBlob](https://github.com/SamEdwardes/spaCyTextBlob) library) and subjectivity scores (computed with the [spaCyTextBlob](https://github.com/SamEdwardes/spaCyTextBlob) library)
+ `c4p_ev_threads.csv`: a collection of threads dealing with the topic of electric cars

# Deliverables

No deliverable is exptected. However, students should carefully examine the text of the 
case along with the data before the class.

# References

[1] Hargadon, A.B. and Douglas, Y., 2001. When innovations meet institutions: Edison and the design of the electric light. _Administrative Science Quarterly_, 46(3), pp.476-501.

[2] Hsu, G. and Grodal, S., 2015. Category taken-for-grantedness as a strategic opportunity: The case of light cigarettes, 1964 to 1993. _American Sociological Review_, 80(1), pp.28-62.

[3] Durand, R. and Khaire, M., 2017. Where do market categories come from and how? Distinguishing category creation from category emergence. _Journal of Management_, 43(1), pp.87-110.
