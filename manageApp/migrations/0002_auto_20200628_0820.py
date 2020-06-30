# Generated by Django 2.2.13 on 2020-06-28 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manageApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='email_id',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='mobile_number',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='persondata',
            name='days_attended',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='persondata',
            name='salary',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='persondata',
            name='name',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
