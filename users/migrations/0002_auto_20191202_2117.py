# Generated by Django 2.2.6 on 2019-12-02 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='mobile_no',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
