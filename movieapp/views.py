
from django.shortcuts import render, redirect
from .forms import SnippetForm, ReviewForm
from .models import Snippet, Review,Category
from django.contrib import messages
from django.db.models import Avg
def usblog(request):
    genres = Category.objects.all()  # Query all categories
    snipps = Snippet.objects.all()  # Query all movies
    return render(request, 'movie/home.html', {'genres': genres, 'snipps': snipps})

def snippet_detail(request):
	form = SnippetForm(request.POST or None, request.FILES or None)
	if request.method == 'POST':

		if form.is_valid():

			obj = form.save(commit=False)
			obj.user = request.user
			obj.save()
			return redirect('/movie/home')

	return render(request, 'movie/add.html', {'form': form})

def detail(request,movie_id):
    movies=Snippet.objects.get(id=movie_id)
    reviews = Review.objects.filter(movie=movie_id).order_by("-comment")

    average = reviews.aggregate(Avg("rating"))["rating__avg"]
    if average == None:
        average = 0
    else:
        average = round(average, 2)
    context = {
        "movie": movies,
        "reviews": reviews,
        "average": average,
    }
    return render(request, 'movie/detail.html', context)

def update(request,id):
    movie= Snippet.objects.get(id=id)
    form= SnippetForm(request.POST or None, request.FILES, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/movie/home')
    return render(request, 'movie/edit.html', {'form':form, 'movie':movie})
def delete(request,id):
    if request.method == 'POST':
        movie= Snippet.objects.get(id=id)
        movie.delete()
        return redirect('/movie/home')
    return render(request, 'movie/delete.html')
def add_review(request,id):
            if request.user.is_authenticated:
                movie = Snippet.objects.get(id=id)
                if request.method == "POST":
                    form = ReviewForm(request.POST or None)
                    if form.is_valid():
                        data = form.save(commit=False)
                        data.comment = request.POST["comment"]
                        data.rating = request.POST["rating"]
                        data.user = request.user
                        data.movie = movie
                        data.save()
                        return redirect("movieapp:detail",id)
                else:
                    form = ReviewForm()
                return render(request,'movie/detail1.html',{'form':form})
            else:
                return redirect("users:login")

def edit_review(request,movie_id,review_id):
                if request.user.is_authenticated:
                    movie = Snippet.objects.get(id=movie_id)
                    review = Review.objects.get(movie=movie, id=review_id)
                    if request.user == review.user:
                        if request.method == "POST":
                            form = ReviewForm(request.POST,instance=review)
                            if form.is_valid():
                                data = form.save(commit=False)
                                if (data.rating>10) or (data.rating<0):
                                    error="Out of range. Please select rating from 0 to 10."
                                    return render(request,'movie/editreview.html',{'error':error, "form":form})
                                else:
                                    data.save()
                                    return redirect("movieapp:detail",movie_id)
                        else:
                            form = ReviewForm(instance=review)
                        return render(request,'movie/editreview.html',{"form":form})
                    else:
                        return redirect("movieapp:detail",movie_id)
                else:
                    return redirect("users:login")

def delete_review(request,movie_id,review_id):
                if request.user.is_authenticated:
                    movie = Snippet.objects.get(id=movie_id)
                    review = Review.objects.get(movie=movie, id=review_id)
                    if request.user == review.user:
                        review.delete()
                    return redirect("movieapp:detail",movie_id)
                else:
                    return redirect("users:login")
def genre_detail(request, cat_id):
    genre = Category.objects.get(pk=cat_id)
    items = Snippet.objects.filter(cat=genre)
    return render(request, 'movie/genre_detail.html', {'genre': genre, 'items': items})
