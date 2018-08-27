# infile=open("data/austen-emma-excerpt.txt")
# infile2=open("data/austen-emma.txt")
# # print(infile)
# # print(infile.read())
# text=infile.read()
# text2=infile2.read()
# infile.close()
# print(text)

##quiz1##
# number_of_es=0
# for letter in text:
#     if letter == "e":
#         number_of_es=number_of_es+1
# print(number_of_es)
#####################################
#
###quiz2###"
# words=text.split()
# words2=text2.split()
# # # number_of_hits=0
# # item_to_count="in"
# # for letter in words:
# #     if letter == item_to_count:
# #         number_of_hits+=1
# # print(number_of_hits)
# ####################################
def count_in_list(item_to_count, list_to_search):
    number_of_hits=0
    for item in list_to_search:
        if item == item_to_count:
            number_of_hits+=1
    return number_of_hits
# print(count_in_list("an", words))
# ###quiz3###
# print(count_in_list("the",words))
# #
#A more general count
#take1
# counts={}
# for word in words:
#     if word in counts:
#         counts[word] = counts[word]+1
#     else:
#         counts[word] = 1
# print(counts)
# def counter(list_to_search):
#     counts={}
#     for word in list_to_search:
#         if word in counts:
#             counts[word]=counts[word]+1
#         else:
#             counts[word]=1
#     return counts
# print(counter(words))
###quiz3###
#######################################
# emma_count=0
# for letter in words2:
#     if letter == "Emma":
#         emma_count+=1
# print(emma_count)
############A count function (take2)################


# x = ['a', 'a', 'b', 'b', 'c', 'c', 'c']
# unique_x=set(x)
# print(unique_x)

# unique_words=set(words)
# for word in unique_words:
#     print(word, count_in_list(word,words)) 

def counter2(list_to_search):
    unique_words=set(list_to_search)
    for word in unique_words:
        print(word, count_in_list(word,list_to_search))

# counter2(words)
##############Text clean up########################

# x="Emma"
# x_lower=x.lower()
# print(x_lower)

# text_lower=text.lower()
# print(text_lower)

# x = 'Please. remove. all. dots. from. this. sentence.'
# x=x.replace(".","")
# print(x)

# short_text = "Commas, as it turns out, are so much overestimated."
# short_text = short_text.lower()
# short_text = short_text.replace(",","")
# print(short_text)
# short_text = "Commas, as it turns out, are overestimated. Dots, however, even more so!"
def remove_punc(text_in):
    punctuation='!@#$%^&*()_-+={}[]:;"\'|<>,.?/~`'
    for marker in punctuation:
        text_in=text_in.replace(marker,"")
    return text_in
# print(remove_punc(short_text))
#############Writing results to a file##################



# outfile = open("first-output.txt", mode="w")
# outfile.write("My first output.")
# outfile.close()

###final quiz###
outfile=open("data/austes-frequency-distribution.txt", mode="w")
def counter3(list_to_search):
    unique_words=set(list_to_search)
    for word in unique_words:
        number=count_in_list(word, list_to_search)
        outfile.write(word + "; " + ""+ str(number)+" "+" ")
        
        

infile=open("data/austen-emma.txt")
text=infile.read()
infile.close()
text_clean=remove_punc(text)
text_clean=text_clean.lower()
words=text_clean.split()
# outfile1=open("data/austes-frequency-distribution-words.txt", mode="w")
# for letter in words:
#     outfile1.write(letter+"; "+" ")
# print(words)
counter3(words)
# print(text_clean)


