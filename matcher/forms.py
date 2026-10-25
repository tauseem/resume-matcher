from django import forms
from .models import Analysis


class AnalysisForm(forms.ModelForm):
    resume_file = forms.FileField(
        required=False,
        label="Or upload your resume (PDF or DOCX)",
        widget=forms.ClearableFileInput(attrs={"class": "form-control"}),
    )

    class Meta:
        model = Analysis
        fields = ["job_title", "resume_text", "job_description"]
        widgets = {
            "job_title": forms.TextInput(attrs={"class": "form-control"}),
            "resume_text": forms.Textarea(attrs={"class": "form-control", "rows": 8}),
            "job_description": forms.Textarea(attrs={"class": "form-control", "rows": 8}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["resume_text"].required = False

    def clean_resume_file(self):
        file = self.cleaned_data.get("resume_file")
        if file and not file.name.lower().endswith((".pdf", ".docx")):
            raise forms.ValidationError("Please upload a PDF or DOCX file.")
        return file

    def clean(self):
        cleaned = super().clean()
        if not cleaned.get("resume_text") and not cleaned.get("resume_file"):
            raise forms.ValidationError("Paste your resume text or upload a file.")
        return cleaned