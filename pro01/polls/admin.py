from django.contrib import admin
from .models import Question, Choice

# Choice 항목 만들기 갯수 3개
# class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

# Question 데이터 셋 꾸미기?
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        # 필드 위 제목
        (None, {'fields':['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]

    # Question 항목 출력
    list_display = ('question_text', 'pub_date', 'was_published_recently')

    # 밑에 choice 항목 생성
    inlines = [ChoiceInline]

    # 옆에 필터 날짜로
    list_filter = ['pub_date']
    # 검색 제목으로
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)