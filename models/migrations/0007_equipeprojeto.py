# Generated by Django 5.0.6 on 2024-07-23 13:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0006_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='EquipeProjeto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('data_atualizacao', models.DateTimeField(auto_now=True)),
                ('projeto_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='models.projeto')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='models.usuario')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
