# Generated by Django 2.2.5 on 2019-10-20 08:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('petName', models.CharField(max_length=200)),
                ('petBorn_time', models.DateTimeField(verbose_name='date born')),
            ],
        ),
        migrations.CreateModel(
            name='Tp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data1', models.FloatField(default=0)),
                ('data2', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Petdata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data1', models.IntegerField(default=0)),
                ('data2', models.FloatField(default=0)),
                ('IdtoPet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pet.Pet')),
            ],
        ),
    ]
