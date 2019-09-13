from django.db import models

# Create your models here.


class Slider(models.Model):
    public = models.BooleanField(default=False, verbose_name='Опубликовать')
    sort = models.IntegerField(default=0, verbose_name='Номер для сортировки')
    title = models.CharField(max_length=255, null=True, verbose_name='Название слайда')
    image = models.ImageField(upload_to='media/', null=True, verbose_name='Изображение слайда')
    description = models.TextField(null=True, verbose_name='Описание')
    link_text = models.CharField(max_length=50, null=True, verbose_name='Текст ссылки')
    link = models.URLField(null=True, max_length=200)

    def __str__(self):
        return '{}'.format(self.title)


class LonggridTag(models.Model):
    name = models.CharField(null=True, unique=True, max_length=50, verbose_name='Тэг франшизы')
    slug = models.SlugField(max_length=50, null=True,
                            db_index=True, unique=True,
                            verbose_name='uri', help_text='Поле задает уникалный адрес объекта в разделе сайта')

    def __str__(self):
        return self.name


class Longgrid(models.Model):
    title = models.CharField(max_length=150, null=True, verbose_name='Название Лонггрида')
    slug = models.SlugField(max_length=100, blank=True, null=True, db_index=True, unique=True, verbose_name='uri')
    public = models.BooleanField(null=True, default=False, verbose_name='Опубликовать')
    date_pub = models.DateTimeField(auto_now_add=False, blank=True, verbose_name='Создан')
    image = models.ImageField(upload_to='media/', null=True, verbose_name='Изображение для превью')
    # short_description = WYSWYG
    detail_image = models.ImageField(upload_to='media/', null=True, verbose_name='Детальное изображение')
    # description =  WYSWYG
    tags = models.ManyToManyField(LonggridTag, blank=True, verbose_name="Теги статьи", related_name="Longgrid")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:longgrids", kwargs={"slug": self.slug})