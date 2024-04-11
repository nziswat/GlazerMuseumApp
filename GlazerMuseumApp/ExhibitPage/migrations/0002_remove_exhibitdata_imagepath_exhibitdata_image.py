# Generated by Django 4.2.9 on 2024-04-02 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ExhibitPage', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exhibitdata',
            name='imagePath',
        ),
        migrations.AddField(
            model_name='exhibitdata',
            name='image',
            field=models.ImageField(default='blank', upload_to='images/'),
        ),
    ]