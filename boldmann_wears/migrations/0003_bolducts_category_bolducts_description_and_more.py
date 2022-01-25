# Generated by Django 4.0 on 2022-01-12 01:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('boldmann_wears', '0002_bolducts_image_bolducts_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='bolducts',
            name='category',
            field=models.CharField(choices=[('S', 'Shirt'), ('SP', 'Sport Wear'), ('OW', 'Out Wear')], default=1, max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bolducts',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bolducts',
            name='discount_price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bolducts',
            name='label',
            field=models.CharField(choices=[('N', 'New'), ('BS', 'Best Seller')], default=1, max_length=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bolducts',
            name='price',
            field=models.FloatField(),
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered', models.BooleanField(default=False)),
                ('quantity', models.IntegerField(default=1)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boldmann_wears.bolducts')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('ordered_date', models.DateTimeField()),
                ('ordered', models.BooleanField(default=False)),
                ('items', models.ManyToManyField(to='boldmann_wears.OrderItem')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
    ]
