# Generated by Django 4.0.5 on 2022-06-15 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_arkacayinturizm_img2_arkacayinturizm_text_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arkacayinturizm',
            name='text',
            field=models.TextField(null=True, verbose_name='ArkacayinTurizm text detali hamar'),
        ),
    ]
