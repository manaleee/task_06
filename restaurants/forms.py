from django import forms
from .models import RestaurantForm

class ArticleForm(forms.ModelForm):
    class Meta:
        model = RestaurantForm
        fields=['title','content','author']


<form action={% url 'create-view' %} method="POST">
    {% csrf_token %}
    {{form}}
    <input type="submit" value="create"> 
</form>    