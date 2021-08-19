# Generated by Django 3.2.6 on 2021-08-19 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auther', '0002_user_parent'),
        ('purchase', '0010_product_order_limit'),
    ]

    operations = [
        migrations.AddField(
            model_name='price',
            name='role',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='prices', to='auther.role'),
        ),
    ]