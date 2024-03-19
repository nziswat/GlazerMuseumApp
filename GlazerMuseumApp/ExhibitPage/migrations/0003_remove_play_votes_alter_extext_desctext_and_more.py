# Generated by Django 4.2.9 on 2024-03-19 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ExhibitPage', '0002_play_playset_playtypes_setname_alter_extext_desctext_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='play',
            name='votes',
        ),
        migrations.AlterField(
            model_name='extext',
            name='descText',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='extext',
            name='imagePath',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cookie', models.CharField(max_length=256)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('exhibit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ExhibitPage.extext')),
                ('play', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ExhibitPage.play')),
            ],
        ),
    ]