# Generated by Django 4.2.9 on 2024-03-25 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titleText', models.CharField(max_length=200)),
                ('descText', models.CharField(max_length=200)),
                ('imagePath', models.CharField(max_length=200)),
            ],
        ),
    ]
