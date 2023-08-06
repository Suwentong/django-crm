from django import forms
from .models import Customer, Record, Complaint

# Форма для добавления клиентов
class AddCustomerForm(forms.ModelForm):
    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Имя", "class":"form-control"}), label="")
    last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Фамилия", "class":"form-control"}), label="")
    patronymic = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Отчество", "class":"form-control"}), label="")
    personal_account = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Лицевой Счет", "class":"form-control"}), label="")
    phone = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Телефон", "class":"form-control"}), label="")
    address = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Адрес", "class":"form-control"}), label="")
    city = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Город", "class":"form-control"}), label="")

    class Meta:
        model = Customer
        exclude = ("user", )

# Форма для добавления обращений
class AddRecordForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
         self.user = kwargs.pop('user', None)
         super(AddRecordForm, self).__init__(*args, **kwargs)

         if self.user.groups.filter(name='Back Office Specialist').exists():
            self.fields['first_name'] = forms.CharField(required=True, disabled=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Имя", "class":"form-control"}), label="")
            self.fields['last_name'] = forms.CharField(required=True, disabled=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Фамилия", "class":"form-control"}), label="")
            self.fields['patronymic'] = forms.CharField(required=True, disabled=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Отчество", "class":"form-control"}), label="")
            self.fields['personal_account'] = forms.CharField(required=True, disabled=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Лицевой Счет", "class":"form-control"}), label="")
            self.fields['phone'] = forms.CharField(required=True, disabled=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Телефон", "class":"form-control"}), label="")
            self.fields['record'] = forms.CharField(required=True, disabled=True, widget=forms.widgets.Textarea(attrs={"placeholder":"Обращение", "class":"form-control"}), label="")
            self.fields['responsible_person'] = forms.CharField(required=True, disabled=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Ответственный", "class":"form-control"}), label="")
            self.fields['comment'] = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Комментарий Специалиста", "class":"form-control"}), label="")
            self.fields['status'] = forms.CharField(required=True, widget=forms.widgets.RadioSelect(attrs={}, choices=[('1', 'На рассмотрении'), ('2', 'Завершено')]), label="")
         else:
            self.fields.pop('comment')
            self.fields.pop('status')
            self.fields['first_name'] = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Имя", "class":"form-control"}), label="")
            self.fields['last_name'] = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Фамилия", "class":"form-control"}), label="")
            self.fields['patronymic'] = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Отчество", "class":"form-control"}), label="")
            self.fields['personal_account'] = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Лицевой Счет", "class":"form-control"}), label="")
            self.fields['phone'] = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Телефон", "class":"form-control"}), label="")
            self.fields['record'] = forms.CharField(required=True, widget=forms.widgets.Textarea(attrs={"placeholder":"Обращение", "class":"form-control"}), label="")
            self.fields['responsible_person'] = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Ответственный", "class":"form-control"}), label="")
    
    class Meta:
        model = Record
        exclude = ("user", )

# Форма для добавления жалоб
class AddComplaintForm(forms.ModelForm):
   def __init__(self, *args, **kwargs):
         self.user = kwargs.pop('user', None)
         super(AddComplaintForm, self).__init__(*args, **kwargs)

         if self.user.groups.filter(name='Back Office Specialist').exists():
            
            self.fields['first_name'] = forms.CharField(required=True, disabled=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Имя", "class":"form-control"}), label="")
            self.fields['last_name'] = forms.CharField(required=True, disabled=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Фамилия", "class":"form-control"}), label="")
            self.fields['patronymic'] = forms.CharField(required=True, disabled=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Отчество", "class":"form-control"}), label="")
            self.fields['personal_account'] = forms.CharField(required=True, disabled=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Лицевой Счет", "class":"form-control"}), label="")
            self.fields['phone'] = forms.CharField(required=True, disabled=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Телефон", "class":"form-control"}), label="")
            self.fields['complaint'] = forms.CharField(required=True, disabled=True, widget=forms.widgets.Textarea(attrs={"placeholder":"Жалоба", "class":"form-control"}), label="")
            self.fields['responsible_person'] = forms.CharField(required=True, disabled=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Ответственный", "class":"form-control"}), label="")
            self.fields['comment'] = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Комментарий Специалиста", "class":"form-control"}), label="")
            self.fields['status'] = forms.CharField(required=True, widget=forms.widgets.RadioSelect(attrs={}, choices=[('1', 'На рассмотрении'), ('2', 'Завершено')]), label="")
         else:
            self.fields.pop('comment')
            self.fields.pop('status')
            self.fields['first_name'] = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Имя", "class":"form-control"}), label="")
            self.fields['last_name'] = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Фамилия", "class":"form-control"}), label="")
            self.fields['patronymic'] = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Отчество", "class":"form-control"}), label="")
            self.fields['personal_account'] = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Лицевой Счет", "class":"form-control"}), label="")
            self.fields['phone'] = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Телефон", "class":"form-control"}), label="")
            self.fields['complaint'] = forms.CharField(required=True, widget=forms.widgets.Textarea(attrs={"placeholder":"Жалоба", "class":"form-control"}), label="")
            self.fields['responsible_person'] = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Ответственный", "class":"form-control"}), label="")
   
   class Meta:
        model = Complaint
        exclude = ("user", )
