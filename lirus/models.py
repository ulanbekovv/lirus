from django.db import models
from django.conf import settings

class Category(models.Model):
    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категория'

    name = models.CharField('Категории', max_length=128)

    def __str__(self):
        return self.name

class Subcategories(models.Model):
    class Meta:
        verbose_name = 'Подкатигории'
        verbose_name_plural = 'Подкатигория'

    name = models.CharField('Подкатигории', max_length=32)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, verbose_name='Категория')

    def __str__(self):
        return self.name

class Product(models.Model):
    class Meta:
        verbose_name = 'Одежда'
        verbose_name_plural = 'Одежды'
        ordering = ['-id']

    title = models.CharField('Название одежды', max_length =32)
    price = models.PositiveIntegerField('Цена')
    the_size = models.CharField('Размер', max_length=8)
    subcategories = models.ForeignKey('Subcategories', on_delete=models.SET_NULL, null=True, verbose_name='Подкатигория')

    def __str__(self):
        return self.title

class ProductImage(models.Model):
    class Meta:
        verbose_name = 'Фотографии'
        verbose_name_plural = 'Фотография'

    picture = models.FileField('Фотография', upload_to='product/')
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='Товар', null=True, related_name='product_image')

    def __str__(self):
        return self.product

class AboutShop(models.Model):
    class Meta:
        verbose_name_plural = 'О магазине'

    name = models.CharField('Название текста', max_length=512)
    description = models.TextField('Описание')

    def __str__(self):
        return self.name

class ComplaintsAndSuggestions(models.Model):
    class Meta:
        verbose_name = 'Жалоба и предложения'
        verbose_name_plural = 'Жалобы и предложение'

    # fill_out_the_form = models.CharField('Заполните форму', max_length=512)
    # text = models.TextField('Текст')
    name = models.CharField('Имя', max_length=128)
    phone_number = models.CharField('Номер', max_length=12, unique=True)
    message = models.TextField('Сообщение')

    def __str__(self):
        return self.name

class Сontacts(models.Model):
    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
        
    # map = models.
    address = models.CharField('Адрес', max_length=128)
    phone_number = models.CharField('Телефон', max_length=13, unique=True)
    whatsapp = models.CharField('Whatsapp', max_length=13, unique=True)
    email = models.EmailField('E-mail', max_length=128)
    instagram = models.CharField('Instagram', max_length=128) 
    instagram1 = models.CharField('Instagram', max_length=128) 
    instagram2 = models.CharField('Instagram', max_length=128) 

    def __str__(self):
        return self.address

class Feedback(models.Model):
    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратные связи '
        
    name = models.CharField('Имя', max_length=64)
    email = models.EmailField('E-mail', max_length=128)
    phone_number = models.CharField('Телефон', max_length=13, unique=True)
    message = models.TextField('Сообщение')

    def __str__(self):
        return self.name

class Stock(models.Model):
    class Meta:
        verbose_name = 'Акция'
        verbose_name_plural = 'Акции'

    name = models.CharField('Название акции', max_length=512)
    text = models.TextField('Текст')
    publish = models.DateTimeField('Время')

    def __str__(self):
        return self.name

class News(models.Model):
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    name = models.CharField('Название новостей', max_length=512)
    text = models.TextField('Текст')
    publish = models.DateTimeField('Время')

    def __str__(self):
        return self.name

class Offer(models.Model):
    class Meta:
        verbose_name_plural = 'Предложения'

    name = models.CharField('Название предложений', max_length=512)
    text = models.TextField('Текст')
    publish = models.DateTimeField('Время')

    def __str__(self):
        return self.name

class Card(models.Model):
    class Meta:
        verbose_name = 'Карта'
        verbose_name_plural = 'Карты'

    number_card = models.CharField('Номер карты', max_length=20)
    balance = models.BigIntegerField('Баланс', default=0)
    discount = models.PositiveSmallIntegerField('Скидки')

    def __str__(self):
        return self.number_card
    