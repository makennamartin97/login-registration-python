# Generated by Django 2.2.4 on 2020-05-22 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_reg_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='confirm',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]