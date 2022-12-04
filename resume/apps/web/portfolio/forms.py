from django import forms


class GetInTouchForm(forms.Form):
    name = forms.CharField(label='name', widget=forms.TextInput(attrs={"title": "name", "class":"form-control", "placeholder":"Name"}), required=False)
    email = forms.EmailField(label='email', widget=forms.EmailInput(attrs={"title": "email", "class":"form-control", "placeholder":"Email"}), required=False)
    message = forms.CharField(label='message', widget=forms.Textarea(attrs={"title": "message", "class": "form-control", "row": "6", "placeholder": "Message"}), required=False)

    def clean(self):
        cleaned_data = super(GetInTouchForm, self).clean()
        name = cleaned_data.get('name')
        email = cleaned_data.get('email')
        message = cleaned_data.get('message')

        if not name:
            self.add_error('name', "Please put  your name. ")

        if not email:
            self.add_error('email', "Please put your email. ")

        if not message:
            self.add_error('message', "Please put your message. ")

        return cleaned_data