from django import forms

#---------------||My list of tuples for the hours||---------------
TIME_SLOTS = [
    ('9:00', '9:00'),
    ('10:10', '10:10'),
    ('11:20', '11:20'),
    ('13:30', '13:30'),
    ('14:40', '14:40'),
    ('15:50', '15h50'),
]


#---------------||Form to book an appointment||---------------
class FormPickDate(forms.Form):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    time_slot = forms.CharField(widget=forms.Select(choices=TIME_SLOTS))
    subject = forms.CharField(widget=forms.Textarea)


#---------------||Form to edit a note about an appointment||---------------
class EditNoteForm(forms.Form):
    note = forms.CharField(widget=forms.Textarea)

