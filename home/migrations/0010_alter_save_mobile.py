# Generated by Django 5.1.1 on 2024-10-01 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_quote_qspecialnote_alter_save_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='save',
            name='mobile',
            field=models.CharField(max_length=15),
        ),
    ]
