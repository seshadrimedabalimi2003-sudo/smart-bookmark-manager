from django.shortcuts import render, redirect, get_object_or_404
from .models import Bookmark
from .forms import BookmarkForm

# View all bookmarks
def bookmark_list(request):
    bookmarks = Bookmark.objects.all()
    return render(request, 'bookmarks/bookmark_list.html', {'bookmarks': bookmarks})

# Add bookmark
def bookmark_create(request):
    if request.method == "POST":
        form = BookmarkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bookmark_list')
    else:
        form = BookmarkForm()
    return render(request, 'bookmarks/bookmark_form.html', {'form': form})

# Update bookmark
def bookmark_update(request, pk):
    bookmark = get_object_or_404(Bookmark, pk=pk)
    if request.method == "POST":
        form = BookmarkForm(request.POST, instance=bookmark)
        if form.is_valid():
            form.save()
            return redirect('bookmark_list')
    else:
        form = BookmarkForm(instance=bookmark)
    return render(request, 'bookmarks/bookmark_form.html', {'form': form})

# Delete bookmark
def bookmark_delete(request, pk):
    bookmark = get_object_or_404(Bookmark, pk=pk)
    if request.method == "POST":
        bookmark.delete()
        return redirect('bookmark_list')
    return render(request, 'bookmarks/bookmark_confirm_delete.html', {'bookmark': bookmark})
