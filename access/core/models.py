import uuid
from django.db import models


class AccessModel(models.Model):
    DOCS = (
        ('RG', 'RG'),
        ('CPF', 'CPF'),
        ('USP', 'USP'),
        ('USP', 'USP'),
        ('Passaporte', 'Passaporte'),
    )

    ANSWERABLE = (
        ('Aswerable1', 'Answerable1'),
        ('Aswerable2', 'Answerable2'),
    )

    AUTHORIZED = 'Autorizado'
    WAITING = 'Para autorização'
    NOT_AUTHORIZED = 'Não autorizado'

    STATUS = (
        (AUTHORIZED, AUTHORIZED),
        (WAITING, WAITING),
        (NOT_AUTHORIZED, NOT_AUTHORIZED)
    )

    WEEK = (
        (0, 'Segunda'),
        (1, 'Terça'),
        (2, 'Quarta'),
        (3, 'Quinta'),
        (4, 'Sexta'),
        (5, 'Sábado'),
        (6, 'Domingo')
    )

    uuid = models.UUIDField('uuid', default=uuid.uuid4,
                            editable=False, unique=True)
    enabled = models.BooleanField('ativar', default=False)
    weekdays = models.CharField(
        'weekdays', max_length=20, null=True, choices=WEEK)
    period_to = models.DateField('data de término')
    period_from = models.DateField('data de início')
    time_to = models.TimeField('hora de termino')
    time_from = models.TimeField('hora de início')
    institution = models.CharField('instituição', max_length=128)
    name = models.CharField('nome', max_length=128)
    job = models.CharField('cargo', max_length=128)
    email = models.EmailField('email')
    phone = models.CharField('telefone', max_length=20)
    doc_type = models.CharField('tipo documento', choices=DOCS, max_length=128)
    doc_number = models.CharField('numero do documento', max_length=128)
    answerable = models.CharField(
        'responsável', choices=ANSWERABLE, max_length=128)
    observation = models.CharField('observação', max_length=1024)
    status = models.CharField('status', choices=STATUS, max_length=128,
                              default='Para autorização', null=True,
                              blank=True)
    created_at = models.DateTimeField('data de criação', auto_now_add=True)
    updated_at = models.DateTimeField('data de criação', auto_now=True)
    created_by = models.CharField('created by', max_length=10)
