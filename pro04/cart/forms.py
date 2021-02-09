from django import forms

class AddProductForm(forms.Form):
    '''제품을 추가하는 폼'''
    quantity = forms.IntegerField()             # 제품의 수량
    is_update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)