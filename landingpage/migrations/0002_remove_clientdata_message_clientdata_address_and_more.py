# Generated by Django 4.2.6 on 2023-10-15 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landingpage', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientdata',
            name='message',
        ),
        migrations.AddField(
            model_name='clientdata',
            name='address',
            field=models.CharField(default='', max_length=255, verbose_name='Address'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='clientdata',
            name='phone',
            field=models.CharField(default='', max_length=15, verbose_name='Phone Number'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='clientdata',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='clientdata',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Full Name'),
        ),
    ]
