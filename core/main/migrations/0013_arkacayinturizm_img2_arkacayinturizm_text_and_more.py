# Generated by Django 4.0.5 on 2022-06-14 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_hajortvayr'),
    ]

    operations = [
        migrations.AddField(
            model_name='arkacayinturizm',
            name='img2',
            field=models.ImageField(null=True, upload_to='media', verbose_name='ArkacayinTurizm  detal img'),
        ),
        migrations.AddField(
            model_name='arkacayinturizm',
            name='text',
            field=models.TextField(max_length=20, null=True, verbose_name='ArkacayinTurizm text detali hamar'),
        ),
        migrations.AlterField(
            model_name='arkacayinturizm',
            name='about',
            field=models.TextField(null=True, verbose_name='ArkacayinTurizm about'),
        ),
        migrations.AlterField(
            model_name='arkacayinturizm',
            name='img',
            field=models.ImageField(null=True, upload_to='media', verbose_name='ArkacayinTurizm img'),
        ),
        migrations.AlterField(
            model_name='arkacayinturizm',
            name='name',
            field=models.CharField(max_length=20, null=True, verbose_name='ArkacayinTurizm anun'),
        ),
    ]