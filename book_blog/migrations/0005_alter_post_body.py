# Generated by Django 3.2.9 on 2021-12-20 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_blog', '0004_auto_20211217_2208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.TextField(),
        ),
    ]
