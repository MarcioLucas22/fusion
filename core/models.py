import uuid
from django.db import models
from stdimage.models import StdImageField

def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'

    return filename

class Base(models.Model):
    criado = models.DateField('Criação', auto_now_add=True) # auto_now_add adiciona a data na criação do objeto
    modificado = models.DateField('Modificado', auto_now=True) # auto_now adiciona a data na modificação do objeto
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True

class Servico(Base):
    ICONE_CHOICES = (
        ('lni-cog', 'Engrenagem'),
        ('lni-stats-up', 'Gráfico'),
        ('lni-users', 'Usuários'),
        ('lni-layers', 'Design'),
        ('lni-mobile', 'Mobile'),
        ('lni-rocket', 'Foguete'),
    )
    servico = models.CharField('Serviço', max_length=100)
    descricao = models.TextField('Descrição', max_length=200)
    icone = models.CharField('Ícone', max_length=12, choices=ICONE_CHOICES)

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'
    
    def __str__(self) -> str:
        return self.servico
    
class Cargo(Base):
    cargo = models.CharField('Cargo', max_length=100)

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self) -> str:
        return self.cargo
    
class Funcionario(Base):
    nome = models.CharField('Nome', max_length=100)
    cargo = models.ForeignKey('core.Cargo', verbose_name='Cargo', on_delete=models.CASCADE, max_length=100)
    bio = models.TextField('Bio', max_length=200)
    imagem = StdImageField('Imagem', upload_to=get_file_path, variations={'thumb': {'width': 480, 'height': 480, 'crop': True}}) # Quando colocamos "upload_to" automaticamente é criado uma pasta com o nome definido
    facebook = models.CharField('Facebook', max_length=100, default='#')
    twitter = models.CharField('Twitter', max_length=100, default='#')
    instagram = models.CharField('Instagram', max_length=100, default='#')

    class Meta:
        verbose_name = 'Funcionario'
        verbose_name_plural = 'Funcionarios'

    def __str__(self) -> str:
        return self.nome
    
class Funcionalidade(Base):
    ICONE_CHOICES = (
        ('lni-rocket', 'Foguete'),
        ('lni-laptop-phone', 'Notebook-Celular'),
        ('lni-cog', 'Engrenagem'),
        ('lni-leaf', 'Folha'),
        ('lni-layers', 'Camadas'),
    )
    icone = models.CharField('Ícone', choices=ICONE_CHOICES, max_length=20)
    nome = models.CharField('Nome', max_length=100)
    descricao = models.CharField('Descrição', max_length=100)

    class Meta:
        verbose_name = 'Funcionalidade'
        verbose_name_plural = 'Funcionalidades'

    def __str__(self) -> str:
        return self.nome
