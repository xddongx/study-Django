from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Photo(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_photos')      # related_name : 연결된 객체에서 하위 객체의 목록을 부를 때 사용
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', default='photos/no_image.png')
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.author.username} {self.created.strftime("%Y-%m-%d %H:%M:%S")}'

    # 상세 페이지의 주소를 반환하는 메서드
    def get_absolute_url(self):
        return reverse('photo:photo_detail', args=[str(self.id)])

    class Meta:
        ordering = ['-updated']
