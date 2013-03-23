from django import forms
from apps.irgat.models import *


class IrgatForm(forms.ModelForm):
	class Meta:
		model = Atar