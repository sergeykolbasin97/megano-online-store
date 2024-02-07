# Generated by Django 4.2.2 on 2023-11-07 16:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("order", "0003_merge_20231103_1446"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="comment",
            field=models.TextField(
                blank=True, default="Нет комментария", verbose_name="Комментарий"
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="delivery_method",
            field=models.TextField(
                choices=[
                    ("DELIVERY", "Доставка"),
                    ("EXPRESS_DELIVERY", "Экспресс доставка"),
                ],
                default="DELIVERY",
                verbose_name="Способ доставки",
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="order_status",
            field=models.TextField(
                choices=[
                    ("NOT_PAID", "Не оплачен"),
                    ("PAID", "Оплачен"),
                    ("IN_DELIVERY", "В доставке"),
                    ("DELIVERED", "Доставлен"),
                ],
                default="NOT_PAID",
                verbose_name="Статус заказа",
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="pay_result",
            field=models.BooleanField(default=False, verbose_name="Статсус оплаты"),
        ),
        migrations.AlterField(
            model_name="order",
            name="payment_method",
            field=models.TextField(
                choices=[
                    ("CARD", "Онлайн картой"),
                    ("SOMEONE_ACCOUNT", "Онлайн с чужого счета"),
                ],
                default="CARD",
                verbose_name="Способ оплаты",
            ),
        ),
    ]