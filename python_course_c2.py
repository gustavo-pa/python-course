infile=open("data/austen-emma-excerpt.txt")
# print(infile)
# print(infile.read())
text=infile.read()
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
words=text.split()
# number_of_hits=0
# item_to_count="in"
# for letter in words:
#     if letter == item_to_count:
#         number_of_hits+=1
# print(number_of_hits)
####################################
def count_in_list(item_to_count, list_to_search):
    number_of_hits=0
    for item in list_to_search:
        if item == item_to_count:
            number_of_hits+=1
    return number_of_hits
print(count_in_list("an", words))
###quiz3###
print(count_in_list("the",words))
#