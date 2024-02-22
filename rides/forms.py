from django import forms


class RideForm(forms.Form):
  search_origin = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Origin City', 'style': 'width: 300px;', 'class': 'form-control'}), label="",max_length=64, required=False)
  # forms.CharField())
  
  search_destination = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Destination City', 'style': 'width: 300px;', 'class': 'form-control'}), label="",max_length=64, required=False)
  # attrs={'placeholder': 'Name', 'style': 'width: 300px;', 'class': 'form-control

  ## NEW
  searchstate = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'State Abbreviation:', 'style': 'width: 300px;', 'class': 'form-control'}),label="",max_length=2, required=False)
