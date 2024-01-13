from django.db import models
from django.contrib.auth import get_user_model

class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    category = models.CharField(max_length=35, verbose_name='Категория', choices=[('Dark chocolate', 'Черный'),('Milk chocolate', 'Молочный'), ('White chocolate', 'Белый')])
    description = models.TextField(max_length=200, null=True, blank=True, verbose_name='Описание')
    image = models.ImageField(upload_to='product_images', verbose_name='Картинка', null=True, blank=True)

    def __str__(self):
        return self.name

class Review(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='Автор')
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='Товар')
    text = models.TextField(verbose_name='Текст', max_length=200)
    rating = models.PositiveIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], verbose_name='Оценка')
    moderate = models.BooleanField(default=False, verbose_name='Промодерирован')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return f'{self.author.name} {self.product.name}'
