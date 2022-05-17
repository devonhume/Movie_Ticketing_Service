from django import forms
from .models import Movie, Showing, Ticket


class TicketsForm(forms.Form):
    adult_tickets = forms.IntegerField(label="Adult Tickets (13 and up)")
    child_tickets = forms.IntegerField(label="Child Tickets (12 and under)")


class PurchaseForm(forms.Form):
    first_name = forms.CharField(label="First Name")
    last_name = forms.CharField(label="Last Name")
    email = forms.EmailField(label="Email")
    credit_card = forms.IntegerField(label="Credit Card")
    exp_month = forms.IntegerField(label="Expiration Month")
    exp_year = forms.IntegerField(label="Expiration Year")
    secret_code = forms.IntegerField(label="Secret Code")


# class ConfirmForm():
#     pass

# class TicketsForm(FlaskForm):
#     adult_tickets = IntegerField("Adult Tickets (13 and up)", validators=[DataRequired()])
#     child_tickets = IntegerField("Child Tickets (12 and under)", validators=[DataRequired()])
#     submit = SubmitField("Buy")
#
#
# class PurchaseForm(FlaskForm):
#     first_name = StringField("First Name", validators=[DataRequired()])
#     last_name = StringField("Last Name", validators=[DataRequired()])
#     email = StringField("Email", validators=[Email(), DataRequired()])
#     credit_card = IntegerField("Credit Card", validators=[DataRequired()])
#     exp_month = IntegerField("Expiration Month", validators=[DataRequired()])
#     exp_year = IntegerField("Expiration Year", validators=[DataRequired()])
#     secret_code = IntegerField("Secret Code", validators=[DataRequired()])
#     purchase_submit = SubmitField("Purchase")
#
# class ConfirmForm(FlaskForm):
#     confirm = SubmitField("Close")