from django import forms


class QuadraticForm(forms.Form):
    a = forms.IntegerField(label='коэффициент a')#, widget=forms.TextInput, error_messages={'invalid': 'This field is required'}
    b = forms.IntegerField(label='коэффициент b')
    c = forms.IntegerField(label='коэффициент c')

    def clean_a(self):
        val_a = self.cleaned_data['a']
        if val_a == 0:
            raise forms.ValidationError("коэффициент при первом слагаемом уравнения не может быть равным нулю")
            print(forms.a.error)
          #  self.add_error('val_a', "коэффициент при первом слагаемом уравнения не может быть равным нулю")
        return val_a        

    
