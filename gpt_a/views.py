from django.shortcuts import render, redirect
# Create your views here.
import openai
import os
openai.organization = "org-fMwpbP5OlyTkoVg0qaUGYJrg"
openai.api_key = "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"





def gpt(request):
    if request.method == "POST":
        prompt = request.POST.get("prompt")
        model_engine = "text-davinci-003"

        completions = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            max_tokens=3020,
            n=1,
            temperature=0.5,
        )
        oh_ye = 'ohyeeyey'
        message = completions.choices[0].text
        return render(request, "gpt.html", {"message": message,"prompt":prompt,'oh':oh_ye})
    else:
        return render(request, "gpt.html")

def utama(request):
        return render(request, "utama.html")