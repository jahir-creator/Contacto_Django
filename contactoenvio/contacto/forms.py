from django import forms

class MiFormulario(forms.Form):
    asunto = forms.CharField(
        max_length=255,
        required=True,
        error_messages={'required': 'El campo Asunto es obligatorio.'}
    )
    mensaje = forms.CharField(
        widget=forms.Textarea,
        required=True,
        error_messages={'required': 'El campo Mensaje es obligatorio.'}
    )
    
    correo = forms.EmailField(
        required=True,
        error_messages={'required': 'El campo Correo es obligatorio.'}
    ) 
   
