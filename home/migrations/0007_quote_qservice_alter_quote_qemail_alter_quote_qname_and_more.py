# Generated by Django 5.1.1 on 2024-09-30 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_quote'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='qservice',
            field=models.CharField(default=12, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='quote',
            name='qemail',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='quote',
            name='qname',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='quote',
            name='qspecialnote',
            field=models.TextField(),
        ),
    ]
