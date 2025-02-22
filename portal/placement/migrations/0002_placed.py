# Generated by Django 5.0.4 on 2024-05-07 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('placement', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Placed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_photo', models.ImageField(blank=True, null=True, upload_to='placed_profile_photos/')),
                ('name', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('company', models.CharField(max_length=100)),
            ],
        ),
    ]
