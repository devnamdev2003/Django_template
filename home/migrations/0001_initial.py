# Generated by Django 4.1.7 on 2023-08-07 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('email', models.CharField(max_length=122)),
                ('number', models.CharField(max_length=15)),
                ('mess', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
    ]
