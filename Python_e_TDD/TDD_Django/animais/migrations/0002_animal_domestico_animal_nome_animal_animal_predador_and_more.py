# Generated by Django 4.2.5 on 2023-09-25 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animais', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='domestico',
            field=models.CharField(default='n/a', max_length=4),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='animal',
            name='nome_animal',
            field=models.CharField(default='n/a', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='animal',
            name='predador',
            field=models.CharField(default='n/a', max_length=4),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='animal',
            name='venenoso',
            field=models.CharField(default='n/a', max_length=4),
            preserve_default=False,
        ),
    ]