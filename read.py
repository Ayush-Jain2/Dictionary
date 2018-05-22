import json
from difflib import get_close_matches
data=json.load(open("076 data.json","r"))

def translate(word):
    if word in data:
        return data[word]
    elif len(get_close_matches(word,data.keys(),cutoff=0.8))>0 :
        match=get_close_matches(word,data.keys(),cutoff=0.8)
        ans=input("Did you mean %s instead ?\nEnter Y for yes and N for no. \n" % match[0])
        if ans=="Y" or ans=="y":
            return translate(match[0])
        elif ans=="N" or ans=="n":
            return "The word dosen't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word dosen't exist. Please double check it."
word  = input("\nEnter a word : ")
word=word.lower()
output=translate(word)
if type(output)==list:
    for item in output:
        print(item)
else:
    print(output)
