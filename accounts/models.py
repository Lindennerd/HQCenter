#encoding: utf-8
from django.db import models
from django.contrib.auth.models import User

class tarefa(models.Model):
	nome = models.CharField(verbose_name=u'nome', max_length=200)
	descricao = models.CharField(verbose_name=u'Descrição', max_length=250)
	data_inicio = models.DateField(verbose_name=u'Data de Inicio', auto_now=False)
	data_fim = models.DateField(verbose_name=u'Data de Finalização', auto_now=False)
	responsavel = models.ForeignKey(User)
	finalizada = models.BooleanField(default=False)
	excluida = models.BooleanField(default=False)

	def __unicode__(self):
		return self.nome

	class Meta:
		verbose_name=u'Tarefa'
		verbose_name_plural=u'Tarefas'