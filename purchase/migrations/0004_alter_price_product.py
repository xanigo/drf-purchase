# Generated by Django 3.2.5 on 2021-07-29 12:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0003_payment_ref_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='prices', to='purchase.product'),
        ),
    ]