# Automatic Question Generation

This program will take a text file as an input and generate questions by analyzing each sentences. 

## How does this work?

**The text file passed as argument to the program.**

The text file is read using a Python package called `textblob`.
Each paragraph is further broken down to sentences using function `parse(string):`. 
and each sentence is passed as string to function `genQuestion(line):`

**These are the part-of-speech tags which is used in this demo.**

```
NNS 	Noun, plural
JJ 	Adjective 
NNP 	Proper noun, singular 
VBG 	Verb, gerund or present participle 
VBN 	Verb, past participle 
VBZ 	Verb, 3rd person singular present 
VBD 	Verb, past tense 
IN 		Preposition or subordinating conjunction 
PRP 	Personal pronoun 
NN 	Noun, singular or mass 
```

**Ref:** Alphabetical list of part-of-speech tags used in the Penn Treebank Project.
http://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html

**Then I have created a small list of combinations.**

```
    l1 = ['NNP', 'VBG', 'VBZ', 'IN']
    l2 = ['NNP', 'VBG', 'VBZ']
    l3 = ['PRP', 'VBG', 'VBZ', 'IN']
    l4 = ['PRP', 'VBG', 'VBZ']
    l5 = ['PRP', 'VBG', 'VBD']
    l6 = ['NNP', 'VBG', 'VBD']
    l7 = ['NN', 'VBG', 'VBZ']
    l8 = ['NNP', 'VBZ', 'JJ']
    l9 = ['NNP', 'VBZ', 'NN']
    l10 = ['NNP', 'VBZ']
    l11 = ['PRP', 'VBZ']
    l12 = ['NNP', 'NN', 'IN']
    l13 = ['NN', 'VBZ']
```

Then a dictionary is created called `bucket` and parsed using some English grammar using condition statements.

The sentence which gets parsed successfully generates a question sentence. 
The generated question list is printed.

**This demo only used the grammar to print questions starting with 'what'.**

## Usage

**Virtualenv recommended**

`pip install -r requirements.txt`

`python3 quest.py file.txt`

*Use `-v` option to activate verbose*

`python3 quest.py file.txt -v`

*You can also try inputing any text file.*


# Example

**Sentence:**
-----------INPUT TEXT-------------

```
Bansoori is an Indian classical instrument. Akhil plays Bansoori and Guitar. 
Puliyogare is a South Indian dish made of rice and tamarind. 
Priya writes poems. 

Osmosis is the movement of a solvent across a semipermeable membrane toward a higher concentration of solute. In biological systems, the solvent is typically water, but osmosis can occur in other liquids, supercritical liquids, and even gases.
When a cell is submerged in water, the water molecules pass through the cell membrane from an area of low solute concentration to high solute concentration. For example, if the cell is submerged in saltwater, water molecules move out of the cell. If a cell is submerged in freshwater, water molecules move into the cell.

Raja-Yoga is divided into eight steps, the first is Yama -- non - killing, truthfulness, non - stealing, continence, and non - receiving of any gifts.
Next is Niyama -- cleanliness, contentment, austerity, study, and self - surrender to God. 

-----------INPUT END---------------
```

**Generated questions.**

```
 Question: What is Bansoori?

 Question: What does Akhil play?

 Question: What is Puliyogare?

 Question: What does Priya write?

 Question: What is Osmosis?

 Question: What is solvent?

 Question: What is cell?

 Question: What is example?

 Question: What is cell?

 Question: What is Raja-Yoga?

 Question: What is Niyama?
```

# We can also activate the `verbose` by -v argument to further understand the question generation process.

**Output with verbose option.**

```
 Bansoori is an Indian classical instrument. 

TAGS: [('Bansoori', 'NNP'), ('is', 'VBZ'), ('an', 'DT'), ('Indian', 'JJ'), ('classical', 'JJ'), ('instrument', 'NN')] 

{'NN': 5, 'JJ': 3, 'VBZ': 1, 'DT': 2, 'NNP': 0}

 Question: What is Bansoori?

 --------------------
Akhil plays Bansoori and Guitar. 

TAGS: [('Akhil', 'NNP'), ('plays', 'VBZ'), ('Bansoori', 'NNP'), ('and', 'CC'), ('Guitar', 'NNP')] 

{'CC': 3, 'VBZ': 1, 'NNP': 0}

 Question: What does Akhil play?

 --------------------
Puliyogare is a South Indian dish made of rice and tamarind. 

TAGS: [('Puliyogare', 'NNP'), ('is', 'VBZ'), ('a', 'DT'), ('South', 'JJ'), ('Indian', 'JJ'), ('dish', 'NN'), ('made', 'VBN'), ('of', 'IN'), ('rice', 'NN'), ('and', 'CC'), ('tamarind', 'NN')] 

{'JJ': 3, 'IN': 7, 'NNP': 0, 'DT': 2, 'NN': 5, 'CC': 9, 'VBZ': 1, 'VBN': 6}

 Question: What is Puliyogare?

 --------------------
Priya writes poems. 

TAGS: [('Priya', 'NNP'), ('writes', 'VBZ'), ('poems', 'NNS')] 

{'VBZ': 1, 'NNS': 2, 'NNP': 0}

 Question: What does Priya write?

 --------------------
Osmosis is the movement of a solvent across a semipermeable membrane toward a higher concentration of solute. 

TAGS: [('Osmosis', 'NN'), ('is', 'VBZ'), ('the', 'DT'), ('movement', 'NN'), ('of', 'IN'), ('a', 'DT'), ('solvent', 'JJ'), ('across', 'IN'), ('a', 'DT'), ('semipermeable', 'JJ'), ('membrane', 'NN'), ('toward', 'IN'), ('a', 'DT'), ('higher', 'JJR'), ('concentration', 'NN'), ('of', 'IN'), ('solute', 'NN')] 

{'JJ': 6, 'IN': 4, 'DT': 2, 'NN': 0, 'VBZ': 1, 'JJR': 13}

 Question: What is Osmosis?
```

## How to improve this program.

* This program generates questions starting with 'What'. We can add rule for generating questions containing 'How', 'Where', 'When', 'Which' etc.

* We can use a dataset of text and questions along with machine learning to ask better questions. 

* Further, we can add complex semantic rules for creating long and complex questions.

* We can use pre-tagged bag of words to improve part-of-speech tags.

## Reference 

[Alphabetical list of part-of-speech tags used in the Penn Treebank Project](http://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html)

[Automatic Factual Question Generation from Text](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.208.5602&rep=rep1&type=pdf)

[TextBlob: Simplified Text Processing](http://textblob.readthedocs.io/en/dev/index.html)

[Automatic Question Generation from Paragraph](http://www.ijaerd.com/papers/finished_papers/Automatic%20Question%20Generation%20from%20Paragraph-IJAERDV03I1213514.pdf)

[K2Q: Generating Natural Language Questions from Keywords with User Refinements](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/37566.pdf)
