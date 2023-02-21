from django.shortcuts import render, HttpResponse
from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers import PostgresLexer
from sqlparse import format

import random

from .models import Brand

# Create your views here.


def home(request):
    rnd_id = random.randint(1, 1_000_000)
    rnd_name = "brand" + str(rnd_id)
    Brand.objects.create(brand_id=rnd_id, name=rnd_name)
    print("BRAND CREATED", rnd_id, rnd_name)

    x = Brand.objects.all()
    print(x)
    sqlformatted = format(str(x.query), reindent=True)
    print(highlight(sqlformatted, PostgresLexer(), TerminalFormatter()))

    return render(request, "orm/orm.html")
