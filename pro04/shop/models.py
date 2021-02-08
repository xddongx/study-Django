from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)          # 카테고리 정보가 저장되는 테이블은 이 이름 열을 인덱스 열로 설정
    meta_description = models.TextField(blank=True)                 # Search Engine Optimization SEO검색엔진??
    slug = models.SlugField(max_length=200, db_index=True, unique=True, allow_unicode=True)         # 상품명으로 url을 만드는 방식, allow_uniucode 영어를 제외한 언어도 허용

    class Meta:
        ordering = ['name']
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        # 관리자 페이지에서 보여지는 객체가 단수일때와 복수일때 표현하는 값 결정

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_in_category', args=[self.slug])

class Product(models.Model):
    # category가 삭제되도 상품은 남아 있어야 하므로 SET_NULL, null=True로 해야 null값 저장
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='products')
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True, allow_unicode=True)

    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    meta_description = models.TextField(blank=True)
    
    # 가격, 재고
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()

    # 상품 노출 여부, 상품 주문 가능 여부
    available_display = models.BooleanField('Display', default=True)        # 주문 불가능한 제품이라도 목록에 노출
    available_order = models.BooleanField('Order', default=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']
        index_together = [['id', 'slug']]           # 멀티 컬럼 검색 id와 slug 필드를 묶어서 색인이 가능하도록 한는 옵션

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])