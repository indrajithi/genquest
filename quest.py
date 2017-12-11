from textblob import TextBlob
import nltk
from textblob import Word
import sys


def parse(string):
    """
    Parse a paragraph. Devide it into sentences and try to generate quesstions from each sentences.
    """
    try:
        txt = TextBlob(string)
        for sentence in txt.sentences:
            genQuestion(sentence)

    except Exception as e:
        raise e



def genQuestion(line):
    """
    outputs question from the given text
    """
    if type(line) is str:
        line = TextBlob(line)

    bucket = {}


    for i,j in enumerate(line.tags):
        if j[1] not in bucket:
            bucket[j[1]] = i
    
    if verbose:
        print('\n','-'*20)
        print(line ,'\n')        
        print("TAGS:",line.tags, '\n')
        print(bucket)
    
    question = ''

    l1 = ['NNP', 'VBG', 'VBZ', 'IN']
    l2 = ['NNP', 'VBG', 'VBZ']
    

    l3 = ['PRP', 'VBG', 'VBZ', 'IN']
    l4 = ['PRP', 'VBG', 'VBZ']
    l5 = ['PRP', 'VBG', 'VBD']
    l6 = ['NNP', 'VBG', 'VBD']
    l7 = ['NN', 'VBG', 'VBZ']

    l8 = ['NNP', 'VBZ', 'JJ']
    l9 = ['NNP', 'VBZ', 'NN']
    #ll9 = ['PRP', 'VBZ', 'NN']

    l10 = ['NNP', 'VBZ']
    l11 = ['PRP', 'VBZ']
    l12 = ['NNP', 'NN', 'IN']
    l13 = ['NN', 'VBZ']




    if all(key in  bucket for key in l1):
        question = 'What' + ' ' + line.words[bucket['VBZ']] +' '+ line.words[bucket['NNP']]+ ' '+ line.words[bucket['VBG']] + ' ' + line.words[bucket['IN']] + '?1'

    elif all(key in  bucket for key in l2):
        question = 'What' + ' ' + line.words[bucket['VBZ']] +' '+ line.words[bucket['NNP']] +' '+ line.words[bucket['VBG']] + '?2'

    elif all(key in  bucket for key in l3):
        question = 'What' + ' ' + line.words[bucket['VBZ']] +' '+ line.words[bucket['PRP']]+ ' '+ line.words[bucket['VBG']] + ' ' + line.words[bucket['IN']] + '?3'

    elif all(key in  bucket for key in l4):
        question = 'What ' + line.words[bucket['PRP']] +' '+  ' does ' + line.words[bucket['VBG']]+ ' '+  line.words[bucket['VBG']] + '?4'

    #elif all(key in  bucket for key in l5):
    #    question = 'What' + ' ' + line.words[bucket['VBD']] +' '+ line.words[bucket['PRP']] +' '+ line.words[bucket['VBG']] + '?5'
    
    #elif all(key in  bucket for key in l6):
    #    question = 'What' + ' ' + line.words[bucket['VBD']] +' '+ line.words[bucket['NNP']] +' '+ line.words[bucket['VBG']] + '?6'

    elif all(key in  bucket for key in l7):
        question = 'What' + ' ' + line.words[bucket['VBZ']] +' '+ line.words[bucket['NN']] +' '+ line.words[bucket['VBG']] + '?7'

    elif all(key in bucket for key in l8):
        question = 'What' + ' ' + line.words[bucket['VBZ']] + ' ' + line.words[bucket['NNP']] + '?8'

    elif all(key in bucket for key in l9):
        question = 'What' + ' ' + line.words[bucket['VBZ']] + ' ' + line.words[bucket['NNP']] + '?9'

    #elif all(key in bucket for key in ll9):
    #    question = 'What' + ' ' + line.words[bucket['VBZ']] + ' ' + line.words[bucket['PRP']] + '?ll9'

    elif all(key in bucket for key in l11):
        if line.words[bucket['PRP']] in ['she','he']:
            question = 'What' + ' does ' + line.words[bucket['PRP']].lower() + ' ' + line.words[bucket['VBZ']].singularize() + '?10'

    elif all(key in bucket for key in l10):
        question = 'What' + ' does ' + line.words[bucket['NNP']] + ' ' + line.words[bucket['VBZ']].singularize() + '?11'

    elif all(key in bucket for key in l13):
        question = 'What' + ' ' + line.words[bucket['VBZ']] + ' ' + line.words[bucket['NN']] + '?11'



    #elif all(key in bucket for key in l12):
    #    question = 'Who' + line.words[bucket['NNP']] + ' ' + Word(line.words[bucket['NN']]).lemmatize("v") + '?

    if question != '':
        print('\n', 'Question: ' + question )
    #print('-'*20)

def main():  
    """
    Accepts a text file as an argument and generates questions from it.
    """
    global verbose 
    verbose = False

    # Set verbose if -v option is given as argument.
    if len(sys.argv) >= 3: 
        if sys.argv[2] == '-v':
            print('Verbose Mode Activated\n')
            verbose = True


    filehandle = open(sys.argv[1], 'r')
    textinput = filehandle.read()
    print('\n-----------INPUT TEXT-------------\n')
    print(textinput,'\n')
    print('\n-----------INPUT END---------------\n')


    parse(textinput)

if __name__ == "__main__":
    main()

