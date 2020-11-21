from django.db import models
from django.urls import reverse

# bookmark 테이블
class Bookmark(models.Model):
    # 사이트 이름 필드(컬럼)
    site_name = models.CharField(max_length=100)
    # 사이트 url 필드(컬럼)
    url = models.URLField('site URL')

    # admin page에 bookmark 테이블 이름? 표시
    def __str__(self):
        return f'이름 : {self.site_name}, 주소 : {self.url}'

    # 수정이 완료된 후 이동할 페이지 success_url or 모델에 get_absolute_url
    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])

