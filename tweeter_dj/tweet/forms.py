from django import forms
from .models import Tweet

# Create a form for the Tweet model

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['content', 'photo']  # Fields to include in the form

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if not content:
            raise forms.ValidationError("Content cannot be empty.")
        if len(content) > 240:
            raise forms.ValidationError("Content cannot exceed 240 characters.")
        return content

    def clean_photo(self):
        photo = self.cleaned_data.get('photo')
        if photo and photo.size > 5 * 1024 * 1024:  # Limit photo size to 5MB
            raise forms.ValidationError("Photo size must be less than 5MB.")
        return photo