# Generated by Django 3.2.8 on 2021-12-11 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('professores', '0009_remove_professor_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='professor',
            name='foto',
            field=models.ImageField(blank=True, upload_to='fotos/%Y/%m/%d'),
        ),
    ]
