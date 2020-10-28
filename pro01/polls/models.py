from django.db import models
from django.utils import timezone
import datetime

# 질문 모델
class Question(models.Model):
    # 질문 제목
    question_text = models.CharField(max_length=200)
    # 시간
    pub_date = models.DateTimeField('date published')

    # 제목 출력
    def __str__(self):
        return self.question_text

    # ??????
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    # 정렬??
    was_published_recently.admin_order_field = 'pub_date'
    # True 설정하면 값 대신 아이콘이 나타남
    was_published_recently.boolean = True
    # 항목의 헤더 이름을 설정
    was_published_recently.short_description = 'Published recently?'

# 질문의 선택 항목
class Choice(models.Model):
    # 외래키로 받는다
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # 항목 이름? 제목?
    choice_text = models.CharField(max_length=200)
    # 선택된 횟수? 투표 수
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
