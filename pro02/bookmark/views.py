from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from .models import Bookmark

# generic view를 이용한 모델을 리스트 방식으로 불러온다
class BookmarkLV(ListView):
    model = Bookmark
    paginate_by = 6             # 한 페이지에 출력할 갯수

# generic view를 이용한 모델에 데이터 생성
class BookmarkCV(CreateView):
    model = Bookmark                    # 생성할 모델(테이블명)
    fields = ['site_name', 'url']       # 생성할 필드(컬럼)
    success_url = reverse_lazy('list')  # 성공시 이동할 페이지
    template_name_suffix = '_create'    # 사용할 템플릿의 접미사만 변경하는 설정값, bookmark_create라는 이름의 템플릿(html)

# generic view를 이용한 모델 디테일 뷰
class BookmarkDV(DetailView):
    model = Bookmark

# generic view를 이용한 모델 업데이트
class BookmarkUV(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']
    template_name_suffix = '_update'

# generic view를 이용한 모델 삭제
class BookmarkDeleteV(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('list')
