# Generated by Django 2.0.2 on 2019-01-27 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0008_auto_20190110_1747'),
    ]

    operations = [
        migrations.AddField(
            model_name='corte',
            name='locatarios',
            field=models.PositiveIntegerField(default=0, verbose_name='Locatarios'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='corte',
            name='tolerancias',
            field=models.PositiveIntegerField(default=0, verbose_name='Tolerancias'),
            preserve_default=False,
        ),
    ]