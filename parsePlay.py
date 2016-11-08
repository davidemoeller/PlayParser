import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-f', '--filename')
parser.add_argument('-s', '--search', required=False)

args = parser.parse_args()

list_words = []
word_dict = {}

with open(args.filename, 'r') as f:
    for line in f:
        list_words.append(line.split(" "))

flattened = [val for sublist in list_words for val in sublist]

for words in flattened:
    word_dict[words] = 0

for words in flattened:
    if words in word_dict:
        word_dict[words] += 1

sorted_word_dict = sorted([(value,key) for (key,value) in word_dict.items()])

if (args.search):
    for k,v in word_dict.items():
        if args.search in k:
            print(k, v)

else:
    for element in sorted_word_dict:
        print(element)
