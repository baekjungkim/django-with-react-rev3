# Generated by Django 3.0.8 on 2020-08-04 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0003_post_is_public'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='ip',
            field=models.GenericIPAddressField(null=True),
        ),
    ]
