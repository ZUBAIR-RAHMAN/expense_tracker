# Generated by Django 4.0.2 on 2022-02-03 19:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('expanse_tracker', '0002_expanse_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Type', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='expanse',
            name='Date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='expanse',
            name='Type',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='expanse_type', to='expanse_tracker.type'),
            preserve_default=False,
        ),
    ]
