# Generated by Django 4.1.2 on 2022-10-17 22:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0002_alter_lyrics_song_id_alter_song_artiste_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lyrics',
            name='song_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicapp.song'),
        ),
        migrations.AlterField(
            model_name='song',
            name='artiste_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicapp.artiste'),
        ),
        migrations.AlterField(
            model_name='song',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]