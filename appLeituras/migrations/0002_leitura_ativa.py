# Generated by Django 2.1.2 on 2018-10-21 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appLeituras', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='leitura',
            name='ativa',
            field=models.BooleanField(default=False),
        ),
    ]
