# Generated by Django 4.0.3 on 2022-04-10 18:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bloodbank', '0001_initial'),
        ('vaccine', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VaccineStock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0)),
                ('vaccine_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vaccine.vaccine')),
            ],
        ),
        migrations.CreateModel(
            name='BloodStock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0)),
                ('min_stock', models.IntegerField(default=5)),
                ('blood_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bloodbank.bloodgroup')),
            ],
        ),
    ]