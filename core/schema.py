import graphene
from graphene_django import DjangoObjectType
from .models import Category, Note


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ('id', 'title')


class NoteType(DjangoObjectType):
    class Meta:
        model = Note
        fields = ('id', 'title', 'description')


class CoreQuery(graphene.ObjectType):
    categories = graphene.List(CategoryType)
    notes = graphene.List(NoteType)
    category = graphene.Field(CategoryType, category_id=graphene.ID())
    category_title = graphene.Field(CategoryType, category_title=graphene.String())
    note = graphene.Field(NoteType, note_id=graphene.ID())
    note_title = graphene.Field(NoteType, note_title=graphene.String())

    def resolve_categories(root, info, **kwargs):
        return Category.objects.all()

    def resolve_notes(root, info, **kwargs):
        return Note.objects.all()

    def resolve_category(self, info, category_id):
        return Category.objects.get(pk=category_id)

    def resolve_category_title(self, info, category_title):
        return Category.objects.get(title__iexact=category_title)

    def resolve_note(self, info, note_id):
        return Note.objects.get(pk=note_id)

    def resolve_note_title(self, info, note_title):
        return Note.objects.get(title__iexact=note_title)


