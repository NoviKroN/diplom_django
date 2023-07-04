# Generated by Django 4.1 on 2023-07-04 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='free_delivery',
        ),
        migrations.RemoveField(
            model_name='product',
            name='full_description',
        ),
        migrations.AddField(
            model_name='product',
            name='freeDelivery',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='fullDescription',
            field=models.TextField(default=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='rating',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='alt',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='src',
            field=models.ImageField(upload_to='product_images/'),
        ),
        migrations.AlterField(
            model_name='productreview',
            name='author',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='productspecification',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='productspecification',
            name='value',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='producttag',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
