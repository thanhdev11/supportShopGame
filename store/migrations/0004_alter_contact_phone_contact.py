# Generated by Django 3.2.6 on 2021-09-09 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_contact_phone_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone_contact',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]
