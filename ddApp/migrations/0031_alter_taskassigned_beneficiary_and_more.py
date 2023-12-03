# Generated by Django 4.2.5 on 2023-09-27 01:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ddApp', '0030_alter_beneficiarymodel_mobile_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskassigned',
            name='beneficiary',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ddApp.beneficiarymodel'),
        ),
        migrations.AlterField(
            model_name='taskassigned',
            name='completion',
            field=models.CharField(choices=[('Assigned', 'Assigned'), ('Intransit', 'Intransit'), ('Initiated', 'Initiated'), ('Installation Done!', 'Installation Done!')], default='Initiated', max_length=64),
        ),
    ]
