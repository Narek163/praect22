# Generated by Django 4.0.5 on 2022-06-17 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_staysej'),
    ]

    operations = [
        migrations.CreateModel(
            name='staysej3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='stays3 eji anun')),
                ('price', models.IntegerField()),
                ('img', models.ImageField(upload_to='media', verbose_name='stays3 img')),
                ('orer', models.CharField(max_length=20, verbose_name='oreri qanak')),
                ('oreri_koxqin', models.CharField(max_length=20, verbose_name='oreri koxqin')),
            ],
            options={
                'verbose_name': 'stays3',
                'verbose_name_plural': 'stayss3',
            },
        ),
    ]
