from django.shortcuts import render
from django.core.paginator import Paginator


from .models import Run


def runs(request):
    runs = Run.objects.all()

    paginator = Paginator(runs, 5)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    print(page_obj)
    runs = paginator.page(page_number)
    context = {"runs": runs, "page_obj": page_obj}

    return render(request, "runs/runs.html", context)


def createRunCSV(request):
    context = {}
    return render(request, "runs/run-form.html", context)


def run(request, pk):
    print("pk", pk)
    run = Run.objects.get(run_id=pk)
    print(run)
    context = {"run": run}

    return render(request, "runs/run-detail.html", context)
