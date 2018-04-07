# Generated by Django 2.0.2 on 2018-03-18 11:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Horse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('age', models.IntegerField()),
                ('total_prize', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_wins', models.IntegerField()),
                ('total_placed', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='HorseRaceLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=255)),
                ('distance', models.IntegerField()),
                ('draw', models.IntegerField()),
                ('position', models.IntegerField()),
                ('weight_carried', models.IntegerField()),
                ('horse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scrapWebPage.Horse')),
            ],
        ),
        migrations.CreateModel(
            name='Race',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prize', models.DecimalField(decimal_places=2, max_digits=10)),
                ('going', models.CharField(max_length=30)),
                ('date', models.DateTimeField()),
                ('group', models.CharField(max_length=10)),
                ('race_class', models.CharField(max_length=10)),
                ('no_runners', models.IntegerField()),
                ('distance', models.CharField(max_length=15)),
            ],
        ),
        migrations.AddField(
            model_name='horseracelink',
            name='race',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scrapWebPage.Race'),
        ),
    ]