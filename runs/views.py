
from django.shortcuts import render


from .models import Run


def runs(request):
    runs = Run.objects.all()
    context = {"runs": runs}
    return render(request, "runs/runs.html", context)

