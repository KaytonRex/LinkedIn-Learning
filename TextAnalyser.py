text = """
Wake up to reality! Nothing ever goes as planned in this accursed world. 
The longer you live, the more you realize that the only things that truly exist in this reality are merely pain, suffering and futility. 
Listen, everywhere you look in this world, wherever there is light, there will always be shadows to be found as well. 
As long as there is a concept of victors, the vanquished will also exist. 
The selfish intent of wanting to preserve peace, initiates war and hatred is born in order to protect love. 
There are nexuses causal relationships that cannot be separated.
"""

wordDictionary = {}


for txt in (text.lower().split()):
    wordDictionary.setdefault(txt,0)
    wordDictionary[txt] += 1

print(wordDictionary)

for key, value in enumerate(wordDictionary):
    print(f"{key}: {value}")