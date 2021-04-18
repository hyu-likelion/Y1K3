from django.shortcuts import render

def home(request):
    return render(request, "home.html")


def result(request):
    sentence = request.GET["sentence"]

    wordDict = {}
    wordList = sentence.split()

    for word in wordList:
        if word in wordDict:
            wordDict[word] += 1
        else:
            wordDict[word] = 1

    return render(
            request, 
            "result.html", 
            {
                "fulltext": sentence,       # 입력한 전체 텍스트
                "count":len(wordList),      # 입력한 텍스트의 단어 개수
                "wordDict":wordDict.items   # 각 단어들의 개수(key, value)
                })



    
