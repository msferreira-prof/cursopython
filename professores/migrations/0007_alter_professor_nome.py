# Generated by Django 3.2.8 on 2021-12-08 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('professores', '0006_alter_titularidade_codigo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professor',
            name='nome',
            field=models.CharField(max_length=45),
        ),
    ]
