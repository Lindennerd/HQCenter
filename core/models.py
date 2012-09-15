#encoding: utf-8
from django.db import models
from django.contrib.auth.models import User

class comic(models.Model):
	name = models.CharField(verbose_name=u'Nome', max_length=200)
	description = models.TextField(verbose_name=u'Descrição', max_length=500, blank=True)
	author = models.CharField(verbose_name=u'Autor', max_length=200)
	year = models.CharField(verbose_name=u'ano', max_length=100)
	post_date = models.DateField(auto_now=True)
	designer = models.CharField(verbose_name=u'Desenhista Principal', max_length=250)
	publisher = models.ForeignKey('publisher', verbose_name=u'Publicadora')
	owner = models.ForeignKey(User, verbose_name=u'Dono')
	exclude = models.BooleanField(default=False)

	class Meta:
		verbose_name=u'Comic'

	def __unicode__(self):
		return '%s de %s' % (self.name, self.author)

class publisher(models.Model):
	name = models.CharField(verbose_name=u'Nome', max_length=200)
	exclude = models.BooleanField(default=False)
	
	class Meta:
		verbose_name=u'Publicadora'

	def __unicode__(self):
		return self.name


class Coment(models.Model):
	user = models.ForeignKey(User, verbose_name=u'Usuário')
	comic = models.ForeignKey(comic, verbose_name=u'Comic')
	Coment = models.TextField(verbose_name=u'Comentário', max_length=500)

	class Meta:
		verbose_name=u'Comentário'

	def __unicode__(self):
		return 'Comentário de %s sobre %s' % (self.user.username, comic.name)

