# Generated by Django 4.1 on 2022-08-31 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='esgotado',
            field=models.BooleanField(default=False),
        ),
    ]
