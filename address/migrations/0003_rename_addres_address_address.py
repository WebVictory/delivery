# Generated by Django 4.0.2 on 2022-02-02 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0002_rename_delivey_delivery'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='addres',
            new_name='address',
        ),
    ]
