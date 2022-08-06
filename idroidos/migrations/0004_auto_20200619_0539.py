# Generated by Django 3.0.3 on 2020-06-19 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idroidos', '0003_auto_20200615_0325'),
    ]

    operations = [
        migrations.AddField(
            model_name='comparisoninfo',
            name='phonepic1',
            field=models.ImageField(blank=True, upload_to='comparisons'),
        ),
        migrations.AddField(
            model_name='comparisoninfo',
            name='phonepic2',
            field=models.ImageField(blank=True, upload_to='comparisons'),
        ),
        migrations.AlterField(
            model_name='newsarticle',
            name='article_pic1',
            field=models.ImageField(blank=True, upload_to='newsarticles'),
        ),
        migrations.AlterField(
            model_name='newsarticle',
            name='article_pic2',
            field=models.ImageField(blank=True, upload_to='newsarticles'),
        ),
        migrations.AlterField(
            model_name='smartphonesinfo',
            name='design_pic',
            field=models.ImageField(blank=True, upload_to='smartphones'),
        ),
        migrations.AlterField(
            model_name='smartphonesinfo',
            name='display_pic',
            field=models.ImageField(blank=True, upload_to='smartphones'),
        ),
    ]
