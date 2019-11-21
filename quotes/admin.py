from django.contrib import admin
from django import forms
from .models import Post, Category, Author, Background, PostCategory, PostBackground, Like, QuoteCollections


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = []


class PostCategoryInline(admin.TabularInline):
    model = PostCategory
    extra = 1


class PostBackgroundInline(admin.TabularInline):
    model = PostBackground
    extra = 1


class PostAdmin(admin.ModelAdmin):
    form = PostForm
    inlines = [PostCategoryInline, PostBackgroundInline]
    list_display = ('quote', 'author', 'feature_qotd', 'featured_as_qotd')
    list_filter = ('date_posted',)


class QuoteCollectionsAdmin(admin.ModelAdmin):
    list_display = ('name', 'title')


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Background)
admin.site.register(Author)
admin.site.register(Like)
admin.site.register(QuoteCollections, QuoteCollectionsAdmin)


