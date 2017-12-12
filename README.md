# Automatic Question Generation

This program will take a text file as an input and generate questions by analyzing each sentences. 


## Usage

**Virtualenv recommended**

`pip install -r requirements.txt`

`python3 quest.py file.txt`

*Use `-v` option to activate verbose*

`python3 quest.py file.txt -v`

*You can also try inputing any text file.*

## How to improve this program.

* This program only generate questions starting with 'What'. We can add rule for generating questions with starting with 'How', 'Where', 'When' etc.

* We can use a dataset of text and questions along with machine learning to ask better questions. 

* Further we can create better semantic rules for creating long and complex questions.

## Reference 

[Alphabetical list of part-of-speech tags used in the Penn Treebank Project](http://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html)

[Automatic Factual Question Generation from Text](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.208.5602&rep=rep1&type=pdf)

[TextBlob: Simplified Text Processing](http://textblob.readthedocs.io/en/dev/index.html)

[Automatic Question Generation from Paragraph](http://www.ijaerd.com/papers/finished_papers/Automatic%20Question%20Generation%20from%20Paragraph-IJAERDV03I1213514.pdf)

[K2Q: Generating Natural Language Questions from Keywords with User Refinements](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/37566.pdf)
