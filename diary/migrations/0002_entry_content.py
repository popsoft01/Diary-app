# Generated by Django 2.2.12 on 2021-09-21 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='content',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]