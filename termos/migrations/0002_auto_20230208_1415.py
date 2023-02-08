# Generated by Django 2.2.12 on 2023-02-08 14:15

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('termos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='term1',
            name='id',
        ),
        migrations.RemoveField(
            model_name='term2',
            name='id',
        ),
        migrations.RemoveField(
            model_name='term3',
            name='id',
        ),
        migrations.RemoveField(
            model_name='term4',
            name='id',
        ),
        migrations.AlterField(
            model_name='term1',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='term2',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='term3',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='term4',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]