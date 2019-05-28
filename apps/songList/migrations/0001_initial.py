# Generated by Django 2.2.1 on 2019-05-28 18:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('playlists', models.ManyToManyField(related_name='users', to='users.User')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='songs', to='users.User')),
            ],
        ),
    ]