# Generated by Django 4.0.4 on 2022-06-14 10:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Vox', '0003_remove_post_post_img_post_postimg_alter_post_caption'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='caption',
        ),
    ]
