# Generated by Django 5.1.2 on 2024-10-29 12:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dados', '0002_alter_dados_cargo_alter_dados_curso_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dados',
            name='cargo',
        ),
        migrations.RemoveField(
            model_name='dados',
            name='curso',
        ),
        migrations.RemoveField(
            model_name='dados',
            name='descricao_atividades',
        ),
        migrations.RemoveField(
            model_name='dados',
            name='empresa',
        ),
        migrations.RemoveField(
            model_name='dados',
            name='instituicao',
        ),
        migrations.RemoveField(
            model_name='dados',
            name='periodo_experiencia',
        ),
        migrations.RemoveField(
            model_name='dados',
            name='periodo_formacao',
        ),
    ]
