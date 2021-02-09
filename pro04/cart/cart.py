from decimal import Decimal
from django.conf import settings
from shop.models import Product

class Cart(object):
    '''
    세션으로 사용하는 방식, 세션에 데이터 저장 하고 꺼내오는 방식, 세션에 저장 하려면 키값이 있어야함,
    settings.py에 키 값 설정
    '''
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_ID)
        if not cart:
            cart = self.session[settings.CART_ID] = {}
        self.cart = cart

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)

        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']

            yield item

    def add(self, product, quantity=1, is_update=False):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity':0, 'price':str(product.price)}

        if is_update:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity

        self.save()
    
    '''save, remove는 각각 장바구니에 상품을 담고 삭제할 때 사용, clear 상품 주문 시 장바구니 비우는 용'''
    def save(self):
        self.session[settings.CART_ID] = self.cart
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del(self.cart[product_id])
            self.save()

    def clear(self):
        self.session[settings.CART_ID] = {}
        self.session.modified = True

    '''장바구니에 담긴 상픔의 총 가격'''
    def get_product_total(self):
        return sum(Decimal(item['price'])*item['quantity'] for item in self.cart.values())
