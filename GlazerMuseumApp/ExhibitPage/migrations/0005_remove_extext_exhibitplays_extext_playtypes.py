# Generated by Django 4.2.9 on 2024-03-25 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ExhibitPage', '0004_remove_play_playset_playtypes_plays'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='extext',
            name='exhibitPlays',
        ),
        migrations.AddField(
            model_name='extext',
            name='playTypes',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ExhibitPage.playtypes'),
        ),
    ]
