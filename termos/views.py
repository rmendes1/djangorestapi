from rest_framework import generics
# from rest_framework.permissions import IsAuthenticated
from .serializers import (
    Term1Serializer,
    Term2Serializer,
    Term3Serializer,
    Term4Serializer,
)
from .models import (
    Term1,
    Term2,
    Term3,
    Term4,
)


def create_term_view(model, serializer):
    class ListCreate(generics.ListCreateAPIView):
        queryset = model.objects.all()
        serializer_class = serializer
        # permission_classes = [IsAuthenticated]

        # def get_queryset(self):
        #     return self.queryset.filter(user=self.request.user)

    class RetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
        queryset = model.objects.all()
        serializer_class = serializer
        lookup_field = 'uuid'
        # permission_classes = [IsAuthenticated]

        # def get_queryset(self):
        #     return self.queryset.filter(user=self.request.user)

    return ListCreate, RetrieveUpdateDestroy


Term1ListCreate, Term1RetrieveUpdateDestroy = create_term_view(Term1, Term1Serializer)
Term2ListCreate, Term2RetrieveUpdateDestroy = create_term_view(Term2, Term2Serializer)
Term3ListCreate, Term3RetrieveUpdateDestroy = create_term_view(Term3, Term3Serializer)
Term4ListCreate, Term4RetrieveUpdateDestroy = create_term_view(Term4, Term4Serializer)

