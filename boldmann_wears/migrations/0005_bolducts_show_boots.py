# Generated by Django 4.0 on 2022-01-18 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boldmann_wears', '0004_alter_bolducts_category_alter_bolducts_label'),
    ]

    operations = [
        migrations.AddField(
            model_name='bolducts',
            name='show_boots',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
