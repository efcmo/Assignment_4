from django.shortcuts import render
from .forms import InputForm
import math

def calculate(request):
    result, error = None, None
    if request.method == "POST":
        form = InputForm(request.POST)
        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            c = form.cleaned_data['c']

            if a < 1:
                error = "Value A is too small"
            elif c < 0:
                error = "Value C cannot be negative"
            else:
                c3 = c ** 3
                if c3 > 1000:
                    result = math.sqrt(c3) * 10
                else:
                    result = math.sqrt(c3) / a
                result += b
        else:
            error = "Invalid input"
    else:
        form = InputForm()
    return render(request, "calculator/result.html", {"form": form, "result": result, "error": error})
