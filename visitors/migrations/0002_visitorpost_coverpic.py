# Generated by Django 3.2.9 on 2021-12-20 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitorpost',
            name='coverpic',
            field=models.URLField(blank=True, null=True),
        ),
    ]
