# Generated by Django 5.0.3 on 2024-04-23 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_user_canv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='canv',
            field=models.CharField(blank=True, default='', max_length=1000000, null=True),
        ),
    ]