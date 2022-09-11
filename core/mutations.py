import graphene
from django.core.exceptions import ValidationError
from .models import Category, Note
from .schema import CategoryType, NoteType
from graphql_jwt.decorators import login_required

# Mutation
# Create Category
class CreateCategory(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        # id = graphene.ID()

    category = graphene.Field(CategoryType)
    message = graphene.String()

    @classmethod
    @login_required
    def mutate(cls, root, info, title):
        category = Category()
        category.title = title
        category.save()
        msg = "Category successfully created!"
        return CreateCategory(category=category, message=msg)


# Update Category
class UpdateCategory(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        id = graphene.ID()

    category = graphene.Field(CategoryType)
    message = graphene.String()

    @classmethod
    @login_required
    def mutate(cls, root, info, title, id):
        try:
            category = Category.objects.get(pk=id)
        except Category.DoesNotExist:
            raise ValidationError(message="Category does not exists", code=404)
        if category:
            category.title = title
            category.save()
        else:
            pass
        msg = "Category updated successfully!"
        return UpdateCategory(category=category, message=msg)


# Delete Category
class DeleteCategory(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    category = graphene.Field(CategoryType)

    @classmethod
    @login_required
    def mutate(cls, root, info, id):
        try:
            category = Category.objects.get(pk=id)
        except Category.DoesNotExist:
            raise ValidationError(message="Category does not exists", code=404)
        if category:
            category.delete()
        else:
            pass
        return None


# Create Note
class CreateNote(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        description = graphene.String()
        category_id = graphene.Int(required=True)

    note = graphene.Field(NoteType)
    message = graphene.String()

    @classmethod
    @login_required
    def mutate(cls, root, info, title, category_id, description=None):
        note = Note()
        note.title = title
        note.description = description

        category_res = Category.objects.get(pk=category_id)
        if category_res:
            note.category = category_res

        note.save()
        msg = "Note created Successfully!"
        return CreateNote(note=note, message=msg)


# Update Note
class UpdateNote(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        title = graphene.String(required=True)
        description = graphene.String(required=False)

    note = graphene.Field(NoteType)
    message = graphene.String()

    @classmethod
    @login_required
    def mutate(cls, root, info, id, title, description=None):
        try:
            note = Note.objects.get(id=id)
        except Note.DoesNotExist:
            raise ValidationError(message="Note does not exists", code=404)
        if note:
            note.title = title
            note.description = description
            note.save()
        else:
            pass
        msg = "Note successfully updated!"
        return UpdateNote(note=note, message=msg)


# Delete Note
class DeleteNote(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    note = graphene.Field(NoteType)

    @classmethod
    @login_required
    def mutate(cls, root, info, id):
        try:
            note = Note.objects.get(pk=id)
        except Note.DoesNotExist:
            raise ValidationError(message="Note does not exists", code=404)
        note.delete()
        return None


class CoreMutation(graphene.ObjectType):
    create_category = CreateCategory.Field()
    update_category = UpdateCategory.Field()
    delete_category = DeleteCategory.Field()

    create_note = CreateNote.Field()
    update_note = UpdateNote.Field()
    delete_note = DeleteNote.Field()
