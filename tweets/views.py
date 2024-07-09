from django.shortcuts import redirect,render, get_object_or_404,HttpResponse
from .models import Tweet
from django.contrib import messages
from django.views import View
from django.utils import timezone
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.http import JsonResponse

# Create your views here.
class TweetsViews(View):
  def get(self,request):
    all_tweets = Tweet.objects.all().order_by('-id')
    page = request.GET.get('page', 1)
    paginator = Paginator(all_tweets, 10)
    try:
      tweets = paginator.page(page)
    except (PageNotAnInteger, EmptyPage):
      tweets = paginator.page(1)
    return render(request,'home.html', {'all_tweets': tweets})

  def post(self, request):
    tweet_message = request.POST.get('tweet_message')
    Tweet.objects.create(user = request.user, tweet_message = tweet_message)
    messages.success(request, "Tweet uploaded")
    return redirect('home')

class TweetDetailViews(View):
  def dispatch(self, request, *args, **kwargs):
    action = kwargs.pop('action', None)
    if action and hasattr(self, action):
      handler = getattr(self, action)
      return handler(request, *args, **kwargs)
    return super().dispatch(request, *args, **kwargs)

  def get(self, request, id):
    tweet = get_object_or_404(Tweet, id=id)
    return render(request, 'tweets/show.html',{'tweet':tweet})

  def edit(self, request, id):
    tweet = get_object_or_404(Tweet, id=id, user_id=request.user.id)
    if tweet.original_tweet is not None:
      return HttpResponse("Retweets can't be retweeted", status=422)
    return render(request, 'tweets/edit.html',{'tweet':tweet})

  def post(self, request, id):
    tweet = get_object_or_404(Tweet, id=id, user_id=request.user.id)
    if tweet.original_tweet is not None:
      return HttpResponse("Retweets can't be retweeted", status=422)
    tweet.tweet_message = request.POST.get('tweet_message')
    tweet.last_edited_at = timezone.now()
    tweet.save()
    messages.success(request, "Tweet updated")
    return redirect('tweets:ManageTweet', id=id)

  def delete(self, request, id):
    tweet = get_object_or_404(Tweet, id=id, user_id=request.user.id)
    tweet.delete()
    messages.success(request, "Tweet deleted")
    return JsonResponse({'status': 'success'})
    # return redirect('home')