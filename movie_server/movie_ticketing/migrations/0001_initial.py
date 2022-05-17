# Generated by Django 4.0.4 on 2022-05-16 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('image', models.URLField()),
                ('runtime_hrs', models.IntegerField()),
                ('runtime_mins', models.IntegerField()),
                ('rating', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Showing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('ticket_price', models.DecimalField(decimal_places=2, max_digits=100)),
                ('seats_available', models.IntegerField()),
                ('seats_total', models.IntegerField()),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie_ticketing.movie')),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket_code', models.CharField(max_length=50)),
                ('ticket_type', models.CharField(max_length=50)),
                ('ticket_used', models.BooleanField(default=False)),
                ('buyer', models.EmailField(max_length=254)),
                ('showing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie_ticketing.showing')),
            ],
        ),
    ]
