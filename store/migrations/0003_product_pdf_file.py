# Generated by Django 4.1.2 on 2022-10-27 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='pdf_file',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
