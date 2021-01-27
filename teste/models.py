from django.db import models

class Pessoa_comum(models.Model):
    """ Classe Abstrata """
    nome = models.CharField(max_length=250)
    telefone = models.CharField(max_length=11)
    endereco = models.CharField(max_length=254)
    email = models.CharField(max_length=254)
    instagram = models.CharField(max_length=50)
    
    class Meta:
        abstract = True


class Terapeuta(Pessoa_comum):
    """ Classe especializada """ 
    hora_entrada = models.TimeField(auto_now=False, auto_now_add=False)
    hora_alm_entrda = models.TimeField(auto_now=False, auto_now_add=False)
    hora_alm_saida = models.TimeField(auto_now=False, auto_now_add=False)
    hora_saida = models.TimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.nome


class Modalidade(models.Model):
    """ docstring """
    MODALIDADES_TUPLA = [
        ('', ''),
        ('Terapia', 'Terapia'),
        ('Tai Chi Chuan', 'Tai Chi Chuan'),
        ('Cone Hindu', 'Cone Hindu'),
        ('Barras de Access', 'Barras de Access'),
    ]
    modalidades = models.CharField(max_length=30, choices=MODALIDADES_TUPLA, default='', unique=True)
    valor = models.FloatField()
    tempo_duracao = models.DurationField()

    def __str__(self):
        return self.modalidades

    # def __repr__(self):
    #     return self.modalidades


class Cadastro(models.Model):
    """ docstring """
    login = models.CharField(max_length=50)
    senha = models.CharField(max_length=50)
    data_entrada = models.DateTimeField(auto_now=True) 
    FK_modalidade = models.OneToOneField(Modalidade, verbose_name=("Atividades"), on_delete=models.CASCADE, related_name='project_modalidade', default=None)

    # def __str__(self):
    #     return self.data_entrada

class Cliente(Pessoa_comum):
    """ Classe especilizada """
    PROFISSAO_CHOICE = (('desempregado', 'Desempregado'), ('empregado', 'Empregado'))
    ESTADO_CIVIL_COICE = (('solteiro(a)','Solteiro(a)'),('casado(a)','Casado(a)'),('divorciado(a)','Divorciado(a)'),('viúvo(a)','Viúvo(a)'))

    nascimento = models.DateField(auto_now=False, auto_now_add=False)
    profissao = models.CharField(max_length=20, choices=PROFISSAO_CHOICE, default='desempregado')
    estado_civil = models.CharField(max_length=20, choices=ESTADO_CIVIL_COICE, default='solterio(a)')
    FK_cadastro = models.OneToOneField(Cadastro, verbose_name=("cadastro"), on_delete=models.CASCADE, related_name='project_cadastro', default=None)

    def __str__(self):
        return self.nome


class Atendimento(models.Model):
    """ docstring """
    horario = models.DateTimeField(auto_now=False, auto_now_add=False)
    cadastro = models.ForeignKey(Cadastro, verbose_name=("Cliente"), on_delete=models.CASCADE, related_name='project_pedido', default=None)
