# Generated by Django 4.0.3 on 2022-04-10 18:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vaccine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='VaccineNeedy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('reg_date', models.DateTimeField(auto_now_add=True)),
                ('age', models.IntegerField()),
                ('place', models.CharField(max_length=50)),
                ('refid', models.BigIntegerField()),
                ('is_mailed', models.BooleanField(default=False)),
                ('needed_vaccine', models.ForeignKey(default='covishield', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='vaccine.vaccine')),
            ],
        ),
    ]
