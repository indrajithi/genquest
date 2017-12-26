import nltk

sentence = "Sam plays cricket at 5AM"
tokens = nltk.word_tokenize(sentence)
tagged = nltk.pos_tag(tokens)
entities = nltk.chunk.ne_chunk(tagged) #generate named entities

ROOT = 'ROOT'
def getNodes(parent):
    for node in parent:
        if type(node) is nltk.Tree:
            if node.label() == ROOT:
                print("======== Sentence =========")
                print("Sentence:", " ".join(node.leaves()))
            else:
                print("Label:", node.label())
                print("Leaves:", node.leaves())

            getNodes(node)
        else:
            print("Word:", node)

getNodes(entities)