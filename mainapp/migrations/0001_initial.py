# Generated by Django 4.2.2 on 2023-06-23 22:14

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
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.tour', verbose_name='Which tour are the dates for?')),
            ],
        ),
        migrations.AddField(
            model_name='tour',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.tourtype', verbose_name='Tour type'),
        ),
        migrations.CreateModel(
            name='PhotoGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to=mainapp.models.tour_photos_path, verbose_name='Image for gallery')),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.tour', verbose_name='What tour is the photo for?')),
            ],
        ),
        migrations.CreateModel(
            name='ImportantInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=256, verbose_name='Important information when crossing the border')),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.tour', verbose_name='Important information for the tour')),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.TextField(default='No feedback', verbose_name='Feedback')),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.tour', verbose_name='Tour')),
            ],
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Expense name')),
                ('price', models.PositiveIntegerField(blank=True, null=True, verbose_name='Expense price')),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.tour', verbose_name='Additional expense')),
            ],
        ),
        migrations.CreateModel(
            name='Attraction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=256, verbose_name='Attraction description')),
                ('to_choose_from', models.BooleanField(default=False, verbose_name='Is it possible not to visit the attraction?')),
                ('county_name', models.CharField(max_length=50, verbose_name='The name of the county where the attraction is located')),
                ('image', models.ImageField(upload_to=mainapp.models.tour_photos_path, verbose_name='Attraction photo ')),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.tour', verbose_name='Visited attractions included in the tour')),
            ],
        ),
    ]
