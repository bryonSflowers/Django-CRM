from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record

class SignUpForm(UserCreationForm):
	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
	first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
	last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))


	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'User Name'
		self.fields['username'].label = ''
		self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['placeholder'] = 'Password'
		self.fields['password1'].label = ''
		self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

		self.fields['password2'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
		self.fields['password2'].label = ''
		self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'	




# Create Add Simulation Form
class AddRecordForm(forms.ModelForm):
	simulation_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Simulation Name", "class":"form-control"}), label="")
	weatherfile_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Weather File Name", "class":"form-control"}), label="")
	run_period = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Run Period", "class":"form-control"}), label="")
	total_cooling_energy = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Total Cooling Energy [kWh]", "class":"form-control"}), label="")
	peak_cooling_load = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Peak Cooling Load [kWh]", "class":"form-control"}), label="")
	reporting_interval = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Reporting Interval", "class":"form-control"}), label="")
	cooling_setpoint = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Cooling Setpoint", "class":"form-control"}), label="")
	cooling_schedule_type = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Cooling Schedule Type", "class":"form-control"}), label="")
	system_cop = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"System COP", "class":"form-control"}), label="")
	operation_schedule_type = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Operation Schedule Type", "class":"form-control"}), label="")
	lighting_energy = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Lighting Energy [kWh]", "class":"form-control"}), label="")
	equipment_energy = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Equipment Energy [kWh]", "class":"form-control"}), label="")
	envelope_properties = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Envelope Properties", "class":"form-control"}), label="")
	eui = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "EUI [kWh/m²/Year]", "class":"form-control"}), label="")

	class Meta:
		model = Record
		exclude = ("user",)