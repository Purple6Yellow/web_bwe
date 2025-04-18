# Generated by Django 5.1.7 on 2025-04-07 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_sbwe', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inschrijf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voornaam', models.CharField(max_length=50, null=True, verbose_name='voornaam')),
                ('achternaam', models.CharField(max_length=50, null=True, verbose_name='achternaam')),
                ('email', models.EmailField(max_length=254, null=True, unique=True, verbose_name='email')),
                ('bedrijfsnaam', models.CharField(max_length=50, null=True, verbose_name='bedrijfsnaam')),
                ('kvk', models.IntegerField()),
                ('werk', models.TextField(blank=True, max_length=500, null=True)),
                ('website', models.URLField(blank=True, default=False, null=True)),
                ('afbeelding', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
    ]
