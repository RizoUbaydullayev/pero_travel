# Generated by Django 4.2.2 on 2023-06-21 21:19

from django.db import migrations, models
import django.db.models.deletion
import mainapp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Tour name')),
                ('description', models.TextField(verbose_name='Tour description')),
                ('seat', models.PositiveSmallIntegerField(verbose_name='Number of seats')),
                ('main_image', models.ImageField(upload_to=mainapp.models.tour_photos_path, verbose_name='Tour main image')),
                ('child_ticket', models.PositiveIntegerField(verbose_name='Child ticket price')),
                ('adult_ticket', models.PositiveIntegerField(verbose_name='Adult ticket price')),
                ('duration', models.DecimalField(decimal_places=1, max_digits=3, verbose_name='Tour duration in hours')),
                ('calendar_image', models.ImageField(upload_to=mainapp.models.tour_photos_path, verbose_name='Image for calendar')),
            ],
        ),
        migrations.CreateModel(
            name='TourType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Tour type name')),
            ],
        ),
        migrations.CreateModel(
            name='TourDate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Tour date')),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.tour')),
            ],
        ),
        migrations.AddField(
            model_name='tour',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.tourtype', verbose_name='Tour type'),
        ),
    ]
