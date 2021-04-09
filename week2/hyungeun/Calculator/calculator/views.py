from django.shortcuts import render


# Create your views here.


def main(request):
    return render(request, 'calculator/main.html')

def calculator(request):
    expression = request.GET['expression']
    result = eval(expression)
    return render(request, "calculator/calculator.html", {"result":result})
    # GET으로 값을 받고, eval 함수를 사용해 값 계산
    # calculator 페이지 렌더링
