from django.urls import path
from .models import Term1, Term2, Term3, Term4
from .views import (
    Term1ListCreate, 
    Term2ListCreate, 
    Term3ListCreate, 
    Term4ListCreate,
    Term1RetrieveUpdateDestroy,
    Term2RetrieveUpdateDestroy,
    Term3RetrieveUpdateDestroy,
    Term4RetrieveUpdateDestroy
)

models = [
    (Term1, Term1ListCreate, Term1RetrieveUpdateDestroy, 'term1'),
    (Term2, Term2ListCreate, Term2RetrieveUpdateDestroy, 'term2'),
    (Term3, Term3ListCreate, Term3RetrieveUpdateDestroy, 'term3'),
    (Term4, Term4ListCreate, Term4RetrieveUpdateDestroy, 'term4'),
]

urlpatterns = []

for m in models:
    urlpatterns += [
        path(f'{m[3]}/', m[1].as_view(), name=f'{m[3]}-list-create'),
        path(f'{m[3]}/<uuid:uuid>', m[2].as_view(), name=f'{m[3]}-retrieve-update-destroy'),
    ]
