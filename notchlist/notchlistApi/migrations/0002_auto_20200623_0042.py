# Generated by Django 3.0.7 on 2020-06-23 00:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notchlistApi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beer',
            name='drink_style',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='drink_style', to='notchlistApi.Drink_Style'),
        ),
    ]