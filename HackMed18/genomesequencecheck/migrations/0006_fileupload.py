# Generated by Django 2.0.3 on 2018-03-11 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genomesequencecheck', '0005_auto_20180311_0120'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('encodedFile', models.FileField(upload_to='', verbose_name='Uploaded file')),
            ],
        ),
    ]
