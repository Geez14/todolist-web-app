# Generated by Django 4.2.7 on 2024-02-26 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='description',
            field=models.CharField(default='no-description', max_length=1000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='todo',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
