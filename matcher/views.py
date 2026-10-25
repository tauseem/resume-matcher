from django.shortcuts import render, redirect, get_object_or_404
from .forms import AnalysisForm
from .models import Analysis
from .utils import analyze
from .file_utils import extract_text
from django.contrib import messages


def home(request):
    result = None

    if request.method == "POST":
        form = AnalysisForm(request.POST, request.FILES)
        if form.is_valid():
            analysis = form.save(commit=False)
            uploaded = form.cleaned_data.get("resume_file")

            if uploaded:
                try:
                    analysis.resume_text = extract_text(uploaded)
                except Exception:
                    form.add_error("resume_file", "Could not read this file. Try another file or paste the text.")
                else:
                    if not analysis.resume_text.strip():
                        form.add_error("resume_file", "No text found in this file. It may be a scanned image, so paste the text instead.")

            if not form.errors:
                result = analyze(analysis.resume_text, analysis.job_description)
                analysis.score = result["score"]
                analysis.missing_keywords = ", ".join(result["missing"])
                analysis.save()
    else:
        form = AnalysisForm()

    return render(request, "matcher/home.html", {"form": form, "result": result})

def history(request):
    analyses = Analysis.objects.order_by("-created_at")
    return render(request, "matcher/history.html", {"analyses": analyses})


def detail(request, pk):
    analysis = get_object_or_404(Analysis, pk=pk)
    result = analyze(analysis.resume_text, analysis.job_description)
    return render(request, "matcher/detail.html", {"analysis": analysis, "result": result})


def delete_analysis(request, pk):
    analysis = get_object_or_404(Analysis, pk=pk)
    if request.method == "POST":
        analysis.delete()
        messages.success(request, "Check deleted.")
    return redirect("history")