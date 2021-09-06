from django.forms import ModelForm
from django import forms
from .models import Post
from django.core import validators

#DataFlair #Custom_Validator
def check_size(value):
  if len(value) < 6:
    raise forms.ValidationError("the Password is too short")

# define the class of a form
class PostForm(ModelForm):
	class Meta:
		# write the name of models for which the form is made
		model = Post	

		# Custom fields
		fields =["username", "gender", "text"]

	# this function will be used for the validation
	def clean(self):

		# data from the form is fetched using super function
		super(PostForm, self).clean()
		
		# extract the username and text field from the data
		username = self.cleaned_data.get('username')
		text = self.cleaned_data.get('text')

		# conditions to be met for the username length
		if len(username) < 5:
			self._errors['username'] = self.error_class([
				'Minimum 5 characters required'])
		if len(text) <10:
			self._errors['text'] = self.error_class([
				'Post Should Contain a minimum of 10 characters'])

		# return any errors if found
		return self.cleaned_data

#DataFlair #Form
class SignUp(forms.Form):
    first_name = forms.CharField(initial = 'First Name', )
    last_name = forms.CharField(required = False)
    email = forms.EmailField(help_text = 'write your email', required = False)
    Address = forms.CharField(required = False, )
    Technology = forms.CharField(initial = 'Django', disabled = True)
    age = forms.IntegerField(required = False, )
    #password = forms.CharField(widget = forms.PasswordInput, validators = [validators.MinLengthValidator(6)])
    password = forms.CharField(widget = forms.PasswordInput, validators = [check_size, validators.MinLengthValidator(6)])
    re_password = forms.CharField(widget = forms.PasswordInput, required = False)

    #Validation #DataFlair
    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password) < 4:
            raise forms.ValidationError("password is too short")
        return password


