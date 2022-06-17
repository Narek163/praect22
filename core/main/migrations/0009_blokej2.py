# Generated by Django 4.0.5 on 2022-06-13 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_aboutuss_delete_kayqimasindetal'),
    ]

    operations = [
        migrations.CreateModel(
            name='blokej2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='blog anun')),
                ('about', models.TextField(verbose_name='blog about ')),
                ('img', models.ImageField(upload_to='media', verbose_name='blog nkar')),
            ],
            options={
                'verbose_name': 'blog',
                'verbose_name_plural': 'blogs',
            },
        ),
    ]