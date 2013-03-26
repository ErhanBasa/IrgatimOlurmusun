# -*- coding: utf-8 -*-
from django import forms
from apps.irgat.models import *
<<<<<<< HEAD
=======
from django.utils.encoding import smart_str, smart_unicode
>>>>>>> f6eb45152f75c9d10189ad50fb6306bb13f3340d

class IrgatForm(forms.ModelForm):
    class Meta:
        model = Atar
<<<<<<< HEAD
        exclude = ('tarih',)
=======
>>>>>>> f6eb45152f75c9d10189ad50fb6306bb13f3340d

    def __init__(self, *args, **kwargs):
        super(IrgatForm, self).__init__(*args, **kwargs)
        self.fields['kimsin_sen'].widget = forms.RadioSelect(choices=KIMLER, attrs={'id':'optionsRadios1'})
        self.fields['atar_icerigi'].widget.attrs = {'class':'span5', 'rows':4, 'placeholder':u"Gardaş suç bizde ki.."}
        self.fields['konusan_kisi'].widget.attrs = {'placeholder':u'İsminiz'}
        self.fields['sirket'].widget.attrs = {'placeholder':u'Görüştüğünüz Şirket'}
<<<<<<< HEAD
        self.fields['konusulan_kisi'].widget.attrs = {'placeholder':u'Görüştüğünüz Kişi'}
=======
        self.fields['konusulan_kisi'].widget.attrs = {'placeholder':u'Görüştüğünüz Kişi'}        
>>>>>>> f6eb45152f75c9d10189ad50fb6306bb13f3340d
