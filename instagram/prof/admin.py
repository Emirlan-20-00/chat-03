from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin


class PostLikeInline(admin.TabularInline):
    model = PostLike
    extra = 1


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1


class CommentLikeInline(admin.TabularInline):
    model = CommentLike
    extra = 1


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    inlines = [CommentLikeInline]


@admin.register(Post)
class PostAdmin(TranslationAdmin):
    inlines = [PostLikeInline, CommentInline]

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


admin.site.register(UserProFile)
admin.site.register(Follow)
admin.site.register(Story)
admin.site.register(Save)
admin.site.register(SaveItem)
