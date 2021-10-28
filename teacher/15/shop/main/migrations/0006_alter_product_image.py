# Generated by Django 3.2.8 on 2021-10-07 16:19

from django.db import migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_product_cropping'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=image_cropping.fields.ImageCropField(blank=True, null=True, upload_to='products'),
        ),
    ]