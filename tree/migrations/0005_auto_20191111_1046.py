# Generated by Django 2.2.7 on 2019-11-11 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tree', '0004_auto_20191111_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treeimplementation',
            name='leftId',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='treeimplementation',
            name='rightId',
            field=models.IntegerField(default=None, null=True),
        ),
    ]
