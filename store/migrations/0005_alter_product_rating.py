# Generated by Django 4.2.7 on 2024-04-05 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_wishlist_review_productfaq_notification_coupon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='rating',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]
