# Generated by Django 4.2.9 on 2024-04-02 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SPText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titleText', models.CharField(max_length=200)),
                ('descText', models.CharField(max_length=200)),
                ('imagePath', models.CharField(max_length=200)),
            ],
        ),
    ]
