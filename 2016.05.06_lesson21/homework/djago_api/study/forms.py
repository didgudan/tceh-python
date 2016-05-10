from django import forms
from django.core.exceptions import ValidationError
import pdb

from study.models import Lesson, Theme


class PlaceholderForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PlaceholderForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields.get(field_name)
            if field:
                if type(field.widget) in (forms.TextInput, ):
                    field.widget.attrs.update(
                        {'placeholder': field.label, 'class': 'span10'}
                    )
                if type(field.widget) in (forms.Select, ):
                    field.widget.attrs.update({'class': 'span10'})
                    field.empty_label = field.label

    def as_p(self):
        return self._html_output(
            normal_row='<p%(html_class_attr)s>%(field)s%(help_text)s</p>',
            error_row='%s',
            row_ender='</p>',
            help_text_html=' <span class="helptext">%s</span>',
            errors_on_separate_row=True
        )


class LessonForm(PlaceholderForm):
    class Meta:
        model = Lesson
        fields = ['number', 'title']

    def clean(self):
        data = self.cleaned_data

        # If we changing already existing lesson
        if self.instance.pk:
            return data

        existing_lessons_id = [lesson.number for lesson in Lesson.objects.all()]

        if data['number'] in existing_lessons_id:
            raise ValidationError('You must enter unique lesson number!',
                                  code='invalid')

        return data


class ThemeForm(PlaceholderForm):
    class Meta:
        model = Theme
        fields = ['name', 'description', 'lesson']
