# Generated by Django 2.2.12 on 2023-02-08 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('termos', '0002_auto_20230208_1415'),
    ]

    operations = [
        migrations.AddField(
            model_name='term1',
            name='title',
            field=models.CharField(default='Titulo 1', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='term2',
            name='title',
            field=models.CharField(default='Titulo 1 Termo 2', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='term3',
            name='title',
            field=models.CharField(default='Titulo 1 Termo 3', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='term4',
            name='title',
            field=models.CharField(default='Titulo 1 Termo 4', max_length=100),
            preserve_default=False,
        ),
    ]