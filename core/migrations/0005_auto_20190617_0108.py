# Generated by Django 2.2.1 on 2019-06-17 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20190616_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='logo_path',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]