import random
import os

word_file = "wordenizer/words.txt"
maw = 100 #maximum_queryable_words

def esc(text):
    chars = '''\<>#%{}|^~[]:;/?@&'"'''
    for c in chars:
        text = text.replace(c, "-")
    return text.strip('-').strip(".") # strip trailing

def get_words(wordcount=1, to_dict=False):
    r = random.SystemRandom()
    words = [ x for x in open(word_file).read().split("\n") ]
    seed = []
    cnt = 0
    for i in range(wordcount):
        rand_j =  r.randrange(len(words))
        word = esc(words[rand_j].lower())
        seed.append(word)
        cnt += 1
    if to_dict: 
        return dict(enumerate(seed))
    else:
        return " ".join(seed)



def gen_passphrase():
    return get_words(25)
    

if __name__ == "__main__":
    print("___ a few example passphrases: ___")
    for i in range(5):
        print(gen_passphrase())
