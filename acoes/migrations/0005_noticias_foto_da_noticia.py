# Generated by Django 3.2.9 on 2021-11-30 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acoes', '0004_noticias'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticias',
            name='foto_da_noticia',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
