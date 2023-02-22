from django.shortcuts import render
from .models import Product
import json
from django.http import JsonResponse
from django.core.serializers import serialize
from django.db import connection, reset_queries
from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers import PostgresLexer
from sqlparse import format


def home(request):
    qs = Product.objects.all()

    serialized_data = serialize("json", qs)
    serialized_data = json.loads(serialized_data)

    print(qs)
    print("============")
    print("")
    print("CONNECTION QUERIES", connection.queries)
    print("")
    print("============")
    sqlformatted = format(str(qs.query), reindent=True)
    print(highlight(sqlformatted, PostgresLexer(), TerminalFormatter()))
    return JsonResponse(serialized_data, safe=False, status=200)
