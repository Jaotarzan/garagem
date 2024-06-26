from django.db import models

# Create your models here.
class Marca(models.Model):
    nome = models.CharField(max_length=50)
    nacionalidade = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.nome.upper()
    
class Categoria(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao
    
class Acessório(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao
    
class Cor(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao
    
class Veículo(models.Model):
    modelo = models.CharField(max_length=100)
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT, related_name="veiculo")
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name="veiculo")
    cor = models.ForeignKey(Cor, on_delete=models.PROTECT, related_name="veiculo")
    ano = models.IntegerField(null=True, blank=True, default=0)
    preco = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default=0)

    def __str__(self) -> str:
        return f"{self.marca} {self.modelo} {self.ano} {self.cor}"