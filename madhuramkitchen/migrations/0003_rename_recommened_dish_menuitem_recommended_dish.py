# Generated by Django 5.0.7 on 2024-07-17 05:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('madhuramkitchen', '0002_menuitem_recommened_dish'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menuitem',
            old_name='recommened_dish',
            new_name='recommended_dish',
        ),
    ]
