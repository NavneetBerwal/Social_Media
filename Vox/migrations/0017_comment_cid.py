# Generated by Django 4.0.4 on 2022-08-10 09:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Vox', '0016_remove_post_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='cid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Vox.post'),
        ),
    ]