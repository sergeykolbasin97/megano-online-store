# Generated by Django 4.2.2 on 2023-10-15 06:24

import django.db.models.deletion
from django.db import migrations, models

import catalog.models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("account", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Banner",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=256, verbose_name="title")),
                ("text", models.TextField(verbose_name="text")),
                ("link", models.CharField(max_length=256, verbose_name="link")),
                ("active", models.BooleanField(default=False, verbose_name="active")),
                (
                    "image",
                    models.ImageField(null=True, upload_to="", verbose_name="image"),
                ),
            ],
            options={
                "verbose_name": "Banner",
                "verbose_name_plural": "Banners",
            },
        ),
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        db_index=True, max_length=200, verbose_name="name"
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to=catalog.models.category_image_directory_path,
                        verbose_name="image",
                    ),
                ),
                (
                    "parent",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="subcategories",
                        to="catalog.category",
                        verbose_name="parent",
                    ),
                ),
            ],
            options={
                "verbose_name": "Категория",
                "verbose_name_plural": "Категории",
            },
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        db_index=True, max_length=128, verbose_name="name"
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True, db_index=True, verbose_name="description"
                    ),
                ),
                (
                    "manufacturer",
                    models.CharField(max_length=200, verbose_name="manufacturer"),
                ),
                ("active", models.BooleanField(default=False, verbose_name="active")),
                (
                    "limited_edition",
                    models.BooleanField(default=False, verbose_name="limited_edition"),
                ),
                (
                    "preview",
                    models.CharField(
                        blank=True, max_length=200, null=True, verbose_name="preview"
                    ),
                ),
                (
                    "characteristics",
                    models.JSONField(
                        blank=True,
                        default=dict,
                        null=True,
                        verbose_name="characteristics",
                    ),
                ),
            ],
            options={
                "verbose_name": "Товар",
                "verbose_name_plural": "Товары",
            },
        ),
        migrations.CreateModel(
            name="ProductImage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        upload_to=catalog.models.product_image_directory_path,
                        verbose_name="image",
                    ),
                ),
                (
                    "alt",
                    models.CharField(blank=True, max_length=200, verbose_name="alt"),
                ),
            ],
            options={
                "verbose_name": "Изображение продукта",
                "verbose_name_plural": "Изображения продуктов",
            },
        ),
        migrations.CreateModel(
            name="Seller",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="name")),
                (
                    "description",
                    models.TextField(blank=True, verbose_name="description"),
                ),
                ("phone", models.CharField(max_length=15, verbose_name="phone")),
                ("address", models.TextField(verbose_name="address")),
                ("email", models.EmailField(max_length=254, verbose_name="e-mail")),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to=catalog.models.seller_image_directory_path,
                        verbose_name="image",
                    ),
                ),
            ],
            options={
                "verbose_name": "Seller",
                "verbose_name_plural": "Sellers",
            },
        ),
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=128, verbose_name="name")),
            ],
            options={
                "verbose_name": "Тэг",
                "verbose_name_plural": "Тэги",
            },
        ),
        migrations.CreateModel(
            name="Stock",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "quantity",
                    models.PositiveIntegerField(default=0, verbose_name="quantity"),
                ),
                (
                    "quantity_sold",
                    models.PositiveIntegerField(
                        default=0, verbose_name="quantity sold"
                    ),
                ),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2, max_digits=16, verbose_name="price"
                    ),
                ),
                (
                    "create_date",
                    models.DateField(
                        auto_now_add=True, null=True, verbose_name="Дата создания"
                    ),
                ),
                (
                    "free_check",
                    models.BooleanField(default=False, verbose_name="preview"),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="product",
                        to="catalog.product",
                        verbose_name="product",
                    ),
                ),
                (
                    "seller",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="seller",
                        to="catalog.seller",
                        verbose_name="seller",
                    ),
                ),
            ],
            options={
                "verbose_name": "Stock",
                "verbose_name_plural": "Stocks",
            },
        ),
        migrations.AddField(
            model_name="seller",
            name="products",
            field=models.ManyToManyField(
                blank=True,
                related_name="sellers",
                through="catalog.Stock",
                to="catalog.product",
                verbose_name="products",
            ),
        ),
        migrations.CreateModel(
            name="Review",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "text",
                    models.TextField(blank=True, db_index=True, verbose_name="text"),
                ),
                ("created_at", models.DateField(auto_now=True)),
                (
                    "rating",
                    models.DecimalField(
                        decimal_places=2, max_digits=3, verbose_name="rating"
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="reviews",
                        to="catalog.product",
                        verbose_name="product",
                    ),
                ),
                (
                    "profile",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="reviews",
                        to="account.profile",
                        verbose_name="rating",
                    ),
                ),
            ],
            options={
                "verbose_name": "Отзыв",
                "verbose_name_plural": "Отзывы",
            },
        ),
        migrations.AddField(
            model_name="product",
            name="avatar",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="product",
                to="catalog.productimage",
                verbose_name="avatar",
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="products",
                to="catalog.category",
                verbose_name="category",
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="image",
            field=models.ManyToManyField(
                blank=True,
                related_name="products",
                to="catalog.productimage",
                verbose_name="image",
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="tag",
            field=models.ManyToManyField(
                blank=True,
                related_name="products",
                to="catalog.tag",
                verbose_name="tag",
            ),
        ),
    ]