# Generated by Django 4.1.5 on 2023-03-02 20:54

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Hikaro', '0003_match_flashcard_particle'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='current_round',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='match',
            name='score',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='match',
            name='user_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]