from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import MovieList, WatchEntry


class JoinForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Email address",
            }
        ),
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

        widgets = {
            "username": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Username",
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["password1"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "Password",
            }
        )

        self.fields["password2"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "Confirm password",
            }
        )


class WatchEntryForm(forms.ModelForm):
    class Meta:
        model = WatchEntry
        fields = ["status", "rating", "review"]

        widgets = {
            "status": forms.Select(
                attrs={"class": "form-select"}
            ),
            "rating": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "min": 1,
                    "max": 10,
                    "placeholder": "1-10",
                }
            ),
            "review": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Write your review...",
                }
            ),
        }

    def clean_rating(self):
        rating = self.cleaned_data.get("rating")

        if rating is not None and (rating < 1 or rating > 10):
            raise forms.ValidationError(
                "Rating must be between 1 and 10."
            )

        return rating


class MovieListForm(forms.ModelForm):
    class Meta:
        model = MovieList
        fields = ["name"]

        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Example: Favorite Movies",
                }
            )
        }