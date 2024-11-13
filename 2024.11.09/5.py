import ref5

def cnt(dct, letter):
    return (sum([key for key, value in dct.items() if letter in value]))

word = input().upper()
if  "Ё" in word:
    word = word.replace("Ё", "Е")

print(sum([cnt(ref5.scores_letters, word[i]) for i in range(len(word))]))

#синхрофазатрон
#29