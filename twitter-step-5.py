import codecs, fnmatch, os

wordcount={}
address={}

for dirpath, dirs, files in os.walk('nlp/step4'):
    for filename in fnmatch.filter(files, '*.txt'):
        with codecs.open(os.path.join(dirpath, filename),'r',encoding="utf-8") as file:
            for word in file.read().split():
                if word not in wordcount:
                    wordcount[word] = 1
                    address[word] = filename+","
                else:
                    wordcount[word] += 1
                    address[word] += filename+","


pdics = [(k, wordcount[k]) for k in sorted(wordcount, key=wordcount.get, reverse=True)]

with codecs.open("nlp/step5/inverted-index.txt", 'a+', encoding="utf-8") as f:
    f.write("data = " + '\r\n')
    for k,v in pdics:
        f.write(k+":"+'\r\n')
        f.write("{"+str(v)+", ["+str(address[k])+"]"+"},"+'\r\n')