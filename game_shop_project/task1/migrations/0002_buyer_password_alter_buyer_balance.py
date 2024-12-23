# Generated by Django 5.1.3 on 2024-11-28 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyer',
            name='password',
            field=models.CharField(default=12345, max_length=255, verbose_name='Пароль'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='buyer',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Баланс'),
        ),
    ]
