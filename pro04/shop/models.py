from django.db import models
from django.urls import reverse

class Category(models.Model):
    '''카테고리 모델'''
    name = models.CharField(max_length=200, db_index=True)                                  # 색인 생성
    meta_description = models.TextField(blank=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True, allow_unicode=True) # 영어를 제외한 언어 허용

    class Meta:
        ordering = ['name']
        verbose_name = 'category'               # 단수
        verbose_name_plural = 'categories'      # 복수

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_in_category', args=[self.slug])

class Product(models.Model):
    '''상품 모델'''
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='products')           # 객체 조회할 때 쓸 변수
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True, allow_unicode=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    meta_description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)                # 10진수 decimal_places:보다 같거나 커야함
    stock = models.PositiveIntegerField()                                       # 양의 정수
    available_display = models.BooleanField('Display', default=True)
    available_order = models.BooleanField('Order', default=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created', '-updated']
        index_together = [['id','slug']]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])