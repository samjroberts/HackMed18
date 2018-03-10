# Generated by Django 2.0.3 on 2018-03-10 18:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('genomesequencecheck', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bacteria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='genomeindicator',
            name='name',
        ),
        migrations.AddField(
            model_name='genomeindicator',
            name='bacteria',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='bacteria', to='genomesequencecheck.Bacteria'),
            preserve_default=False,
        ),
    ]
