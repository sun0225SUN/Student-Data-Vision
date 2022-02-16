from django import forms

from .models import Student


class StudentForm(forms.ModelForm):
    stu_id = forms.CharField(label='学号', max_length=128)
    name = forms.CharField(label='姓名', max_length=128)
    sex = forms.ChoiceField(label='性别', choices=Student.SEX_ITEMS)
    constellation = forms.ChoiceField(label='星座', choices=Student.STAR_ITEMS)
    birthday = forms.DateField(label='生日', widget=forms.widgets.DateTimeInput(attrs={'type': 'date'}))
    hometown = forms.CharField(label='家庭住址', max_length=128)
    byword = forms.CharField(widget=forms.Textarea, label='人生格言', max_length=128)

    # 学号数字校验
    def clean_stu_id(self):
        cleaned_data = self.cleaned_data['stu_id']
        if not cleaned_data.isdigit():
            raise forms.ValidationError('学号必须是数字！')

        return int(cleaned_data)

    class Meta:
        model = Student
        fields = (
            'stu_id', 'name', 'sex', 'constellation', 'birthday', 'hometown', 'byword'
        )


