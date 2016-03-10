from datetime import date

from django.forms import TextInput, Form, CharField, PasswordInput, EmailInput, MultiWidget, Select

month_dict_by_name = {"January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6, "July": 7, "August": 8,
                      "September": 9, "October": 10, "November": 11,
                      "December": 12}

month_dict_by_number = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July",
                        8: "August", 9: "September", 10: "October", 11: "November",
                        12: "December"}


class DateSelectorWidget(MultiWidget):
    def __init__(self, attrs=None):
        days = [(day, day) for day in range(1, 32)]
        months = [(month, month) for month in (
            "January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
            "November",
            "December",)]
        _widgets = (
            Select(attrs=attrs, choices=months),
            Select(attrs=attrs, choices=days),
        )
        super(DateSelectorWidget, self).__init__(_widgets, attrs)

    def decompress(self, value):
        if value:
            return [month_dict_by_number[value.month], value.day]
        return [None, None]

    def format_output(self, rendered_widgets):
        return ''.join(rendered_widgets)

    def value_from_datadict(self, data, files, name):
        datelist = [
            widget.value_from_datadict(data, files, name + '_%s' % i)
            for i, widget in enumerate(self.widgets)]
        try:
            D = date(
                day=int(datelist[1]),
                month=month_dict_by_name[datelist[0]],
                year=2000,
            )
        except ValueError:
            print ValueError.message
            return ''
        else:
            return str(D)


class LoginForm(Form):
    username = CharField(label="Username", widget=TextInput(attrs={'required': 'true'}), required=True)
    password = CharField(label="Password", widget=PasswordInput(attrs={'required': 'true'}), required=True)


class RegisterForm(Form):
    username = CharField(label="Username", widget=TextInput(attrs={'required': 'true'}), required=True)
    email = CharField(label="Email", widget=EmailInput(attrs={'required': 'true'}), required=True)
    password = CharField(label="Password", widget=PasswordInput(attrs={'required': 'true'}), required=True)
