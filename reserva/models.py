from django.db import models

class Reserva(models.Model):
    TAMANHO_OPCOES = (
        (0, 'PEQUENO'),
        (1, 'MÉDIO'),
        (2, 'GRANDE'),
    )
    TURNO_OPCOES = (
        ('manhã', 'Manhã'),
        ('tarde', 'Tarde'),
    )
    nome = models.CharField(verbose_name='Nome', max_length=50)
    email = models.EmailField(verbose_name='E-mail', max_length=75)
    nome_pet = models.CharField(verbose_name='Nome do pet', max_length=50)
    data = models.DateField(verbose_name='Data', help_text='mm/dd/aaaa')
    turno = models.CharField(verbose_name='Turno', max_length=10, choices=TURNO_OPCOES)
    tamanho = models.IntegerField(verbose_name='Tamanho', choices=TAMANHO_OPCOES)
    observacoes = models.TextField(verbose_name='Observações', blank=True)

    def __str__(self):
        return f'{self.nome}: {self.data} - {self.turno}'
    
    class Meta:
        verbose_name = 'Reserva de banho'
        verbose_name_plural = 'Reservas de banho'