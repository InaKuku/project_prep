# Generated by Django 4.0.3 on 2022-04-05 10:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ownedgarment',
            old_name='garment_size',
            new_name='garment',
        ),
    ]
