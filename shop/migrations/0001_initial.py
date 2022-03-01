# Generated by Django 4.0.2 on 2022-03-01 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('quantity', models.IntegerField()),
                ('image', models.CharField(max_length=200)),
            ],
        ),
    ]