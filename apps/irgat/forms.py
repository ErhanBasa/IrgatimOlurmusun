# -*- coding: utf-8 -*-
from django import forms
from apps.irgat.models import *
from django.utils.encoding import smart_str, smart_unicode

class IrgatForm(forms.ModelForm):
    class Meta:
        model = Atar
        exclude = ('tarih',)

    def __init__(self, *args, **kwargs):
        super(IrgatForm, self).__init__(*args, **kwargs)
        self.fields['kimsin_sen'].widget = forms.RadioSelect(choices=KIMLER, attrs={'id':'optionsRadios1'})
        self.fields['atar_icerigi'].widget.attrs = {'class':'span5', 'rows':4, 'placeholder':u"Gardaş suç bizde ki.."}
        self.fields['konusan_kisi'].widget.attrs = {'placeholder':u'İsminiz'}
        self.fields['sirket'].widget.attrs = {'placeholder':u'Görüştüğünüz Şirket'}
        self.fields['konusulan_kisi'].widget.attrs = {'placeholder':u'Görüştüğünüz Kişi'}   