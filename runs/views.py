
from django.shortcuts import render


from .models import Run


def runs(request):
    runs = Run.objects.all()
    context = {"runs": runs}
    return render(request, "runs/runs.html", context)

def createRunCSV(request):
    context = {}
    return render(request, "runs/run-form.html", context)


def run(request, pk):
    print('pk',pk)
    run = Run.objects.get(run_id=pk)
    print(run)
    context = {'run': run}
 
    return render(request, 'runs/run-detail.html', context)


