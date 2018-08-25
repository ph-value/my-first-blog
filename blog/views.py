from django.shortcuts import render

def post_list(request):                                                         # 함수 생성
    return render(request, 'blog/post_list.html', {})
