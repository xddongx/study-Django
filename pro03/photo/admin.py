from django.contrib import admin
from .models import Photo

class PhotoAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'created', 'updated']        # 모록에 보일 필드 설정
    raw_id_fields = ['author']                                  # 검색?
    list_filter = ['created', 'updated', 'author']              # 필터 범위 출력
    search_fields = ['text', 'created']                         # 검색할 필드 ForeinKey 필드는 설정할 수 없음
    ordering = ['-updated', '-created']                         # 관리자 사이트에서 기본으로 사용할 정렬값 설정

admin.site.register(Photo, PhotoAdmin)

