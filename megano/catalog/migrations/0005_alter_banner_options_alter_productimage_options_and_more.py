# Generated by Django 4.2.2 on 2023-11-02 19:14

import django.db.models.deletion
from django.db import migrations, models

import catalog.models


class Migration(migrations.Migration):
    dependencies = [
        ("account", "0003_alter_profile_options_alter_user_options_and_more"),
        ("catalog", "0004_alter_review_rating"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="banner",
            options={"verbose_name": "Баннер", "verbose_name_plural": "Баннеры"},
        ),
        migrations.AlterModelOptions(
            name="productimage",
            options={
                "verbose_name": "Изображение товара",
                "verbose_name_plural": "Изображения товара",
            },
        ),
        migrations.AlterModelOptions(
            name="seller",
            options={"verbose_name": "Продавец", "verbose_name_plural": "Продавцы"},
        ),
        migrations.AlterModelOptions(
            name="stock",
            options={"verbose_name": "Склад", "verbose_name_plural": "Склады"},
        ),
        migrations.RemoveField(
            model_name="stock",
            name="free_check",
        ),
        migrations.AddField(
            model_name="stock",
            name="free_shipping",
            field=models.BooleanField(
                default=False, verbose_name="Бесплатная доставка"
            ),
        ),
        migrations.AlterField(
            model_name="banner",
            name="active",
            field=models.BooleanField(default=False, verbose_name="Активен"),
        ),
        migrations.AlterField(
            model_name="banner",
            name="image",
            field=models.ImageField(
                null=True, upload_to="", verbose_name="Изображение"
            ),
        ),
        migrations.AlterField(
            model_name="banner",
            name="link",
            field=models.CharField(max_length=256, verbose_name="Ссылка"),
        ),
        migrations.AlterField(
            model_name="banner",
            name="text",
            field=models.TextField(verbose_name="Текст"),
        ),
        migrations.AlterField(
            model_name="banner",
            name="title",
            field=models.CharField(max_length=256, verbose_name="Заголовок"),
        ),
        migrations.AlterField(
            model_name="category",
            name="image",
            field=models.FileField(
                blank=True,
                null=True,
                upload_to=catalog.models.category_image_directory_path,
                verbose_name="Изображение",
            ),
        ),
        migrations.AlterField(
            model_name="category",
            name="parent",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="subcategories",
                to="catalog.category",
                verbose_name="Подкатегория",
            ),
        ),
        migrations.AlterField(
            model_name="category",
            name="title",
            field=models.CharField(
                db_index=True, max_length=200, verbose_name="Заголовок"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="active",
            field=models.BooleanField(default=False, verbose_name="Активен"),
        ),
        migrations.AlterField(
            model_name="product",
            name="avatar",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="product",
                to="catalog.productimage",
                verbose_name="Аватар",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="products",
                to="catalog.category",
                verbose_name="Категория",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="characteristics",
            field=models.JSONField(
                blank=True, default=dict, null=True, verbose_name="Характиристики"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="description",
            field=models.TextField(blank=True, db_index=True, verbose_name="Описание"),
        ),
        migrations.AlterField(
            model_name="product",
            name="image",
            field=models.ManyToManyField(
                blank=True,
                related_name="products",
                to="catalog.productimage",
                verbose_name="Изображения",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="limited_edition",
            field=models.BooleanField(default=False, verbose_name="Лимитированный"),
        ),
        migrations.AlterField(
            model_name="product",
            name="manufacturer",
            field=models.CharField(max_length=200, verbose_name="Производитель"),
        ),
        migrations.AlterField(
            model_name="product",
            name="name",
            field=models.CharField(
                db_index=True, max_length=128, verbose_name="Название"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="preview",
            field=models.CharField(
                blank=True, max_length=200, null=True, verbose_name="Превью"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="tag",
            field=models.ManyToManyField(
                blank=True,
                related_name="products",
                to="catalog.tag",
                verbose_name="Тэги",
            ),
        ),
        migrations.AlterField(
            model_name="productimage",
            name="alt",
            field=models.CharField(blank=True, max_length=200, verbose_name="Описание"),
        ),
        migrations.AlterField(
            model_name="productimage",
            name="image",
            field=models.ImageField(
                upload_to=catalog.models.product_image_directory_path,
                verbose_name="Изображение",
            ),
        ),
        migrations.AlterField(
            model_name="review",
            name="created_at",
            field=models.DateField(auto_now=True, verbose_name="Дата создания"),
        ),
        migrations.AlterField(
            model_name="review",
            name="is_valid",
            field=models.BooleanField(default=False, verbose_name="Валидный"),
        ),
        migrations.AlterField(
            model_name="review",
            name="product",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="reviews",
                to="catalog.product",
                verbose_name="Товар",
            ),
        ),
        migrations.AlterField(
            model_name="review",
            name="profile",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="reviews",
                to="account.profile",
                verbose_name="Пользователь",
            ),
        ),
        migrations.AlterField(
            model_name="review",
            name="rating",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=3,
                null=True,
                verbose_name="Оценка",
            ),
        ),
        migrations.AlterField(
            model_name="review",
            name="text",
            field=models.TextField(blank=True, db_index=True, verbose_name="Текст"),
        ),
        migrations.AlterField(
            model_name="seller",
            name="address",
            field=models.TextField(verbose_name="Адрес"),
        ),
        migrations.AlterField(
            model_name="seller",
            name="description",
            field=models.TextField(blank=True, verbose_name="Описание"),
        ),
        migrations.AlterField(
            model_name="seller",
            name="email",
            field=models.EmailField(max_length=254, verbose_name="E-mail адрес"),
        ),
        migrations.AlterField(
            model_name="seller",
            name="image",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to=catalog.models.seller_image_directory_path,
                verbose_name="Изображение",
            ),
        ),
        migrations.AlterField(
            model_name="seller",
            name="name",
            field=models.CharField(max_length=100, verbose_name="Имя"),
        ),
        migrations.AlterField(
            model_name="seller",
            name="phone",
            field=models.CharField(max_length=15, verbose_name="Телефон"),
        ),
        migrations.AlterField(
            model_name="seller",
            name="products",
            field=models.ManyToManyField(
                blank=True,
                related_name="sellers",
                through="catalog.Stock",
                to="catalog.product",
                verbose_name="Товары",
            ),
        ),
        migrations.AlterField(
            model_name="stock",
            name="price",
            field=models.DecimalField(
                decimal_places=2, max_digits=16, verbose_name="Цена"
            ),
        ),
        migrations.AlterField(
            model_name="stock",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="product",
                to="catalog.product",
                verbose_name="Продукт",
            ),
        ),
        migrations.AlterField(
            model_name="stock",
            name="quantity",
            field=models.PositiveIntegerField(default=0, verbose_name="Количество"),
        ),
        migrations.AlterField(
            model_name="stock",
            name="quantity_sold",
            field=models.PositiveIntegerField(
                default=0, verbose_name="Число проданных"
            ),
        ),
        migrations.AlterField(
            model_name="stock",
            name="seller",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="seller",
                to="catalog.seller",
                verbose_name="Продавец",
            ),
        ),
        migrations.AlterField(
            model_name="tag",
            name="name",
            field=models.CharField(max_length=128, verbose_name="Название"),
        ),
    ]
