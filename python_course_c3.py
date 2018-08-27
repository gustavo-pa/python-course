def read_file(filename):
    infile=open(filename)
    contents=infile.read()
    infile.close()
    return contents

from os import listdir
# infile=open("data/gutenberg/training/austen-sense.txt")
def list_textfiles(directory):
    "Return a list of filenames ending in '.txt' in DIRECTORY."
    textfiles=[]
    for filename in listdir(directory):
        if filename.endswith("txt"):
            textfiles.append(directory  + filename)
    return textfiles

# # out=list_textfiles("data/gutenberg/training/")

# # print(out)
# for filepath in list_textfiles("data/gutenberg/training"):
#     text=read_file(filepath)
#     print(filepath + "has " + str(len(text))+"characteers. ")

# for element in enumerate("Python"):
#     print(element)

def end_of_sentence_marker(charac):
    characteers=[".","?","!"]
    if charac in characteers:
        result=True
    else:
        result=False
    return result
# print(end_of_sentence_marker("a")==True)

def split_sentences(text):
    sentences=[]
    start=0
    for end, character in enumerate(text):
        if end_of_sentence_marker(character):
            sentence=text[start: end+1]
            sentences.append(sentence)
            start=end+1
    return sentences

# print(split_sentences("This is a sentence. Should we seperate it from this one?"))

def tokenize(text):
    sentences=split_sentences(text)
    sentences_clean=[]
    final=[]
    from pyhum.preprocessing import clean_text
    for sent in sentences:
        clean=clean_text(sent)
        sentences_clean.append(clean)
    for sent_clean in sentences_clean:
        final_add=sent_clean.split()
        final.append(final_add)
    return final

print(tokenize("This is a sentence. So, what! comparing.") == 
      [["this", "is", "a", "sentence"], ["so", "what"], ["comparing"]])
##it works##
# 
corpus=[]
read_night=[]
nights_999=list_textfiles("data/arabian_nights/")
for nights in nights_999:
    read_night.append(read_file(nights))
# print(read_night[0])
for cl_night in read_night:
    corpus.append(tokenize(cl_night))
# print(clean_night[0][0])
# print(len(clean_night))
# print(list_textfiles("data/arabian_nights")[:20])
from os.path import splitext
from os.path import basename

def remove_ext(filename):
    file_no_ext=splitext(filename)[0]
    return file_no_ext
# print(remove_ext("data/arabian_nights/1.txt") == "data/arabian_nights/1")
# print(remove_ext("ridiculous_selfie.jpg") == "ridiculous_selfie")
# print(remove_ext("ridiculous_selfie.jpg")[0])

# print(splitext("ridiculous_selfie.jpg"))
def remove_dir(filename):
    file_no_dir=basename(filename)
    return file_no_dir
# print(remove_dir("data/arabian_nights/1.txt") == "1.txt")
# print(remove_dir("/a/kind/of/funny/filepath/to/file.txt") == "file.txt")
def get_filename(filepath):
    clean_file=remove_dir(filepath)
    clean_file=remove_ext(clean_file)
    return clean_file
# print(get_filename("data/arabian_nights/1.txt") == '1')
# x_as_string = "1"
# x_as_int = int(x_as_string)
# print(x_as_int)
def get_night(filepath):
    number_night=int(get_filename(filepath))
    return number_night
# print(get_night("data/arabian_nights/1.txt") == 1)
filenames=list_textfiles('data/arabian_nights')
# filenames.sort(key=get_night)
# filenames[:20]
# filenames.sort(key=get_night)
# print(filenames[:20])  No funcionó

sentences_story=[]

def story_time(text,nwpm):
    count_words=0
    time=0
    sent_story=tokenize(text)
    for w in sent_story:
        sent_counting=w
        for h in sent_counting:
            count_words+=1
    time=count_words/nwpm
    return time

# for time_corpus in corpus:
#     print(story_time(time_corpus,130))

# print(story_time("Probing the time in this program! i hope it works",130))
# for element in enumerate("probando! probando que pasa! probando juemadre"):
#     print(element)
# print(split_sentences("probando! probando que pasa! probando juemadre."))
# print(story_time("probando! probando que pasa! probando juemadre.",130))
def story_time_2(text_split,nwpm):
    count_words=0
    time=0
    for w in text_split:
        sent_counting=w
        for h in sent_counting:
            count_words+=1
    time=count_words/nwpm
    return time

i=0
for alpha in corpus:
    print(i,story_time_2(corpus[i],130))
    i+=1

# print(tokenize("probando! probando que pasa! probando juemadre."))