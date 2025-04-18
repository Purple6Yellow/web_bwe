# Generated by Django 5.1.7 on 2025-04-11 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_sbwe', '0004_prog_aanvraag_akkoord_alter_aanvraag_nawnodig'),
    ]

    operations = [
        migrations.AddField(
            model_name='inschrijf',
            name='delen',
            field=models.CharField(choices=[('zelfstandig', 'zelfstandig'), ('delen', 'delen')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='inschrijf',
            name='telefoon',
            field=models.CharField(max_length=30, null=True, verbose_name='telefoon'),
        ),
        migrations.AddField(
            model_name='inschrijf',
            name='vierkantem',
            field=models.CharField(choices=[('30m2', '30m2'), ('50m2', '50m2'), ('100m2', '100m2'), ('150m2', '150m2')], max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='inschrijf',
            name='voorzieing',
            field=models.TextField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='inschrijf',
            name='website',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='inschrijf',
            name='werk',
            field=models.TextField(blank=True, max_length=50, null=True),
        ),
    ]
