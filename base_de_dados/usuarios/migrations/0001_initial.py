# Generated by Django 2.2 on 2019-05-02 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('dt_criacao', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cpf', models.CharField(blank=True, max_length=11, null=True)),
                ('dtNascimento', models.DateField(blank=True, null=True, verbose_name='Data de nascimento')),
                ('nrTelCelular', models.CharField(blank=True, max_length=11, null=True, verbose_name='Nº telefone celular')),
                ('data_acesso', models.DateTimeField()),
                ('observacoes', models.TextField(blank=True, null=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.categoria')),
            ],
            options={
                'verbose_name_plural': 'usuarios',
            },
        ),
        migrations.CreateModel(
            name='professor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cpf', models.CharField(blank=True, max_length=11, null=True)),
                ('dtNascimento', models.DateField(blank=True, null=True, verbose_name='Data de nascimento')),
                ('nrTelCelular', models.CharField(blank=True, max_length=11, null=True, verbose_name='Nº telefone celular')),
                ('salario', models.DecimalField(decimal_places=2, max_digits=7)),
                ('data_acesso', models.DateTimeField()),
                ('observacoes', models.TextField(blank=True, null=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.categoria')),
            ],
            options={
                'verbose_name_plural': 'professores',
            },
        ),
        migrations.CreateModel(
            name='aluno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cpf', models.CharField(blank=True, max_length=11, null=True)),
                ('dtNascimento', models.DateField(blank=True, null=True, verbose_name='Data de nascimento')),
                ('nrTelCelular', models.CharField(blank=True, max_length=11, null=True, verbose_name='Nº telefone celular')),
                ('curso', models.CharField(max_length=100)),
                ('mensalidade', models.DecimalField(decimal_places=2, max_digits=7)),
                ('data_acesso', models.DateTimeField()),
                ('observacoes', models.TextField(blank=True, null=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.categoria')),
            ],
            options={
                'verbose_name_plural': 'alunos',
            },
        ),
    ]
