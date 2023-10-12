# Generated by Django 4.2.2 on 2023-10-09 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExhibitionType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Exhibition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('age_limit', models.IntegerField(default=16)),
                ('place', models.CharField(default='Музей', max_length=40)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('img', models.ImageField(upload_to='exhibition_images')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.exhibitiontype')),
            ],
        ),
    ]
