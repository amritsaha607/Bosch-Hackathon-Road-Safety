# Generated by Django 2.1.7 on 2019-03-30 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_no', models.CharField(max_length=100, unique=True)),
                ('lat', models.FloatField(default=0)),
                ('lon', models.FloatField(default=0)),
                ('taken', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Police',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('confirm_password', models.CharField(max_length=50)),
                ('availabality', models.BooleanField(default=True)),
                ('authent', models.BooleanField(default=False)),
                ('captured_image', models.ImageField(blank=True, upload_to='')),
                ('lat', models.FloatField(default=0)),
                ('lon', models.FloatField(default=0)),
                ('detected_car', models.ManyToManyField(blank=True, related_name='choice_set', to='hackathon.Driver')),
            ],
        ),
    ]
