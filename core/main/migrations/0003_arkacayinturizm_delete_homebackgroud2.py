# Generated by Django 4.0.5 on 2022-06-12 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_homebackgroud2'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArkacayinTurizm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='ArkacayinTurizm anun')),
                ('about', models.TextField(verbose_name='ArkacayinTurizm about')),
                ('img', models.ImageField(upload_to='media', verbose_name='ArkacayinTurizm img')),
            ],
            options={
                'verbose_name': 'ArkacayinTurizm',
                'verbose_name_plural': 'ArkacayinTurizmner',
            },
        ),
        migrations.DeleteModel(
            name='HomeBackGroud2',
        ),
    ]
