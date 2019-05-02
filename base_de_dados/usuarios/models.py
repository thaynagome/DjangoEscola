from django.db import models

class categoria(models.Model):
    nome = models.CharField(max_length=100)
    dt_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

class disciplina(models.Model):
    nome = models.CharField(max_length=100)
    dt_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

class usuario(models.Model):
    nome = models.CharField(max_length=100)
    data_acesso = models.DateTimeField()
    categoria = models.ForeignKey(categoria, on_delete=models.CASCADE)
    observacoes = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "usuarios"

    def __str__(self):
        return self.descricao

class professor(models.Model):
    nome = models.CharField(max_length=100)
    salario = models.DecimalField(max_digits=7, decimal_places=2)
    data_acesso = models.DateTimeField()
    categoria = models.ForeignKey(categoria, on_delete=models.CASCADE)
    observacoes = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "professores"

    def __str__(self):
        return self.descricao

class aluno(models.Model):
    nome = models.CharField(max_length=100)
    curso = models.CharField(max_length=100)
    mensalidade = models.DecimalField(max_digits=7, decimal_places=2)
    data_acesso = models.DateTimeField()
    disciplina = models.ForeignKey(, on_delete=models.CASCADE)
    observacoes = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "alunos"

    def __str__(self):
        return self.descricao