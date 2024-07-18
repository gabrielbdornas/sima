# Generated by Django 5.0.6 on 2024-07-16 15:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0002_projetoestrategico'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projeto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('data_atualizacao', models.DateTimeField(auto_now=True)),
                ('data_fim', models.DateTimeField(blank=True, null=True)),
                ('nome', models.CharField(max_length=100)),
                ('fase', models.CharField(choices=[('FORM', 'Formatação'), ('PLAN', 'Planejamento'), ('EXEC', 'Execução'), ('CONC', 'Concluído')], max_length=4)),
                ('oportunidade_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='models.pedidoimersao')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]