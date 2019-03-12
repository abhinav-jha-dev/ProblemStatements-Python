import json

baseDirectory = "Arrays/Sources/"
outputDirectory = "Arrays/Output/"
outputArray = []
with open(baseDirectory+"ValueElementsText.txt","r") as f:
    for line in f:
        outputArray.append(line.rstrip("\n\r"))
    
with open(outputDirectory+"Output.txt","w") as outfile:
    json.dump(outputArray, outfile)