from django import forms

from .models import WatchEntry


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