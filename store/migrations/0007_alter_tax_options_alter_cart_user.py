# Generated by Django 4.2.7 on 2024-04-07 09:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0006_tax'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tax',
            options={'ordering': ['country'], 'verbose_name_plural': 'Taxes'},
        ),
        migrations.AlterField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
