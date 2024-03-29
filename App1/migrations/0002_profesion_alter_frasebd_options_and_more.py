# Generated by Django 5.0.2 on 2024-02-11 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profesion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, verbose_name='Nombre')),
            ],
        ),
        migrations.AlterModelOptions(
            name='frasebd',
            options={'verbose_name': 'Frase', 'verbose_name_plural': 'Frases'},
        ),
        migrations.AlterField(
            model_name='autordb',
            name='fecha_fallecimiento',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha Fallecimiento'),
        ),
        migrations.AlterField(
            model_name='autordb',
            name='fecha_nacimiento',
            field=models.DateField(verbose_name='Fecha Nacimiento'),
        ),
        migrations.RemoveField(
            model_name='autordb',
            name='profesion',
        ),
        migrations.AddField(
            model_name='autordb',
            name='profesion',
            field=models.ManyToManyField(to='App1.profesion', verbose_name='Profesion'),
        ),
    ]
