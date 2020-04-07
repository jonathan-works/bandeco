# Generated by Django 3.0.3 on 2020-04-04 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20200403_1323'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cardapioproduto',
            name='cardapio',
        ),
        migrations.AddField(
            model_name='cardapioproduto',
            name='cardapio',
            field=models.ManyToManyField(to='polls.Cardapio'),
        ),
        migrations.RemoveField(
            model_name='cardapioproduto',
            name='produto',
        ),
        migrations.AddField(
            model_name='cardapioproduto',
            name='produto',
            field=models.ManyToManyField(to='polls.Produto'),
        ),
    ]
