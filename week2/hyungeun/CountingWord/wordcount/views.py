from django.shortcuts import render

def typetext(request):
    return render(request, "typetext.html")

def result(request):
    sentences = request.GET['sentences']
    wordList = sentences.split()
    wordDict = {}

    for word in wordList:
        try:
            wordDict[word] += 1
        except KeyError:
            wordDict[word] = 1

    return render(request, "result.html", {"sentences": sentences, "countWords": len(wordList), "wordDict": wordDict.items})