# Generated by Django 4.0.5 on 2022-06-15 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_delete_loginimg'),
    ]

    operations = [
        migrations.CreateModel(
            name='Loginimg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='media', verbose_name='login img')),
            ],
            options={
                'verbose_name': 'login',
                'verbose_name_plural': 'logins',
            },
        ),
    ]
