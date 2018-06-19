# Generated by Django 2.0.6 on 2018-06-19 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InputData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('hight_ug', models.IntegerField()),
                ('temperature', models.IntegerField()),
                ('wind_speed', models.IntegerField()),
                ('wind_vector_direction', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='OutputData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avg_temperature', models.IntegerField()),
                ('avg_wind_speed', models.IntegerField()),
                ('direction_in_space', models.IntegerField()),
            ],
        ),
    ]
