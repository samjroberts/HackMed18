# Generated by Django 2.0.3 on 2018-03-11 01:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('genomesequencecheck', '0004_auto_20180310_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genomeindicator',
            name='bacteria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='genomes', to='genomesequencecheck.Bacteria'),
        ),
    ]
