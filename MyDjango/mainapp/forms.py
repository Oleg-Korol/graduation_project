import datetime

from crispy_forms.bootstrap import FieldWithButtons, StrictButton, FormActions
from crispy_forms.layout import Submit, Layout
from crispy_forms.bootstrap import FormActions

from django.core.exceptions import ValidationError
from django.forms import ModelForm

from crispy_forms.helper import FormHelper
from django.urls import reverse

from mainapp.models import Team, Record


class ManagerFormAdmin(ModelForm):

    def clean_team_group(self):
        """"Checks if the manager is in charge of the salon"""

        teams = Team.objects.filter(top_employee=self.instance)

        if len(teams) > 0 and self.cleaned_data['manager_team'] != teams[0]:
            raise ValidationError(
                'Мэнеджер является управляющим другого отдела',
                code='invalid',
                )

        return self.cleaned_data['manager_team']


class RecordForm(ModelForm):
    class Meta:
        model = Record
        fields ='__all__'

    def __init__(self, *args, **kwargs):
            super(RecordForm, self).__init__(*args, **kwargs)

            self.helper = FormHelper(self)
            self.helper.form_method = 'POST'
            self.helper.form_class = "form -horizontal"

            # add form or edite form
            add_form = True if not kwargs['instance'] else False

            # set form tag attribute/add buttons
            if add_form:
                self.helper.form_action = reverse('record_add')
                submit = Submit(
                    'add_button', 'Добавить',
                    css_class='btn btn-primary'
                )
            else:
                self.helper.form_action = reverse(
                    'record_edit',
                    kwargs={'pk': kwargs['instance'].id}
                )
                submit = Submit('save_button',
                                'Сохранить',
                                css_class='btn btn-primary')

            # set form field properties

            self.helper.help_text_inline = True
            self.helper.html5_required = True
            self.helper.label_class = 'col-sm-2 control-label'
            self.helper.field_class = 'col-sm-8'

            self.helper.layout = Layout(
                'first_name ',
                'car_model ',
                'phone_number ',
                'client_email',
                FieldWithButtons('time_servise ',StrictButton(
                    '',
                    css_class="glyphicon glyphicon-calendar"),
                                 ),

                'service ',
                FormActions(
                    submit,
                    Submit(
                        'cancel_button',
                        'Отменить',
                        css_class='btn btn-link',
                    ),
                ),
            )
