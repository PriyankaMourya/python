# Generated by Django 3.2.6 on 2021-09-05 19:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('contact_id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(default='', max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('desc', models.CharField(max_length=500)),
                ('phone', models.IntegerField()),
                ('screenshot', models.ImageField(default='https://via.placeholder.com/500x500.png?text=Default', upload_to='contact\\images')),
                ('pub_date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('desc', models.CharField(max_length=500)),
                ('price', models.IntegerField()),
                ('image', models.ImageField(default='https://via.placeholder.com/500x500.png?text=Default', upload_to='course\\images')),
                ('pub_date', models.DateField(default=django.utils.timezone.now)),
                ('category', models.CharField(default='web', max_length=50)),
            ],
        ),
    ]