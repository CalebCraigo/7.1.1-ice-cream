# Generated by Django 2.2.6 on 2019-10-07 20:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ice_cream', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='icecreams',
            name='pud_date',
        ),
        migrations.CreateModel(
            name='Choices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choices_text', models.CharField(max_length=255)),
                ('featured', models.IntegerField(default=0)),
                ('options', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ice_cream.Icecreams')),
            ],
        ),
    ]