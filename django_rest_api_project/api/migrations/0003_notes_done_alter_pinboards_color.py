# Generated by Django 4.1 on 2022-08-07 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_notes_pinboards_delete_person_delete_species_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='done',
            field=models.CharField(choices=[('true', 'Yes'), ('false', 'No')], default='false', max_length=5),
        ),
        migrations.AlterField(
            model_name='pinboards',
            name='color',
            field=models.CharField(choices=[('255, 0, 0', 'Red'), ('0, 255, 0', 'Green'), ('0, 0, 255', 'Blue')], default='255, 0, 0', max_length=9),
        ),
    ]
