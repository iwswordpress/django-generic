from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Run


def runs(request):
    runs = Run.objects.all()
    page_number = request.GET.get("page")
    if not page_number:
        page_number = 1

    paginator = Paginator(runs, 5)

    page_obj = paginator.get_page(page_number)
    runs = paginator.page(page_number)
    context = {"runs": runs, "page_obj": page_obj}

    return render(request, "dts/runs.html", context)


def run(request, pk):
    # print("pk", pk)
    run = Run.objects.get(run_id=pk)
    print(run)
    context = {"run": run}

    return render(request, "dts/run-detail.html", context)
