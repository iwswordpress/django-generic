
from django.shortcuts import render


from .models import Run


def runs(request):
    runs = Run.objects.filter(['run_id', 'project_id'])
    context = {"runs": runs}
    print(runs)
    # context = {}
    return render(request, "runs/runs.html", context)

def createRunCSV(request):
    context = {}
    return render(request, "runs/run-form.html", context)


def run(request, pk):
    run = Run.objects.get(id=pk)
    context = {'run': run}
    return render(request, 'projects/runs/run-detail.html', context)


