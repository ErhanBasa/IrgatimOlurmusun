# -*- coding: utf-8 -*-

from django.db import models
from datetime import datetime

KIMLER = (
        ('0', u'Irgatım ben'),
        ('1', u'Ağayım ben')
    )

class AtarManager(models.Manager):
    def aktif(self):
        return self.filter(aktif=True).order_by("-tarih")

class Atar(models.Model):
    kimsin_sen = models.CharField(u"Kimsin sen", max_length="15", choices=KIMLER)
    atar_icerigi = models.TextField(u"Ne diyon hacım sen")
    konusan_kisi = models.CharField(u"İsim", max_length=40, blank=True, null=True)
    sirket = models.CharField(u"Köy", max_length=60, blank=True, null=True)
    konusulan_kisi = models.CharField(u"Ağa", max_length=40, blank=True, null=True)
    tarih = models.DateTimeField(default=datetime.now)
    aktif = models.BooleanField(default=False)
    objects = AtarManager()

    def __unicode__(self):
        return u"Atar : %s" % (self.pk)

    class Meta:
        verbose_name=u"Atar"
        verbose_name_plural=u"Atarlar"
        ordering=("-tarih",)