# Generated by Django 5.1.1 on 2024-09-27 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=300)),
            ],
        ),
        migrations.DeleteModel(
            name='enqiery',
        ),
    ]