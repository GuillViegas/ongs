# Generated by Django 2.2.1 on 2019-06-18 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20190617_0108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='site',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]