from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail
from taggit.models import Tag
from .models import Post, Comment
from .forms import EmailPostForm, CommentForm

def post_home(request, tag_slug=None):

    object_list = Post.published.all()
    tag = None

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tag__in=[tag])

    paginator = Paginator(object_list, 4)               #3 post in each page
    page = request.GET.get('page')
    
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)                       #if page is not an integer deliver the first page
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)     #if page is out of range deliver last page of results

    return render(request,
                'blog/post_list.html',
                {'page' : page,
                'posts' : posts,
                'tag': tag})

def post_list(request, tag_slug=None):
    
    object_list = Post.published.all()
    tag = None

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tag__in=[tag])

    paginator = Paginator(object_list, 7)               #3 post in each page
    page = request.GET.get('page')
    
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)                       #if page is not an integer deliver the first page
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)     #if page is out of range deliver last page of results

    return render(request,
                'blog/post_list.html',
                {'page' : page,
                'posts' : posts,
                'tag': tag})

def  post_detail(request, post):
    
	post = get_object_or_404(Post, slug=post)

	# List of the active comments for this post
	comments = post.comments.filter(active=True)
	if request.method == 'POST':
		comment_form = CommentForm(data=request.POST)        # A comment was posted

		if comment_form.is_valid() :          
			new_commment = comment_form.save(commit=False)  # Create Comment object but don't save to database yet 
			new_comment.post = post                         # Assign the current post to the comment          
			new_comment.save()                              # Save the comment to the database

	else :
		comment_form = CommentForm()

	return render(request, 
					'blog/post_detail.html',
					{'post' : post,
					'comments' : comments,
					'comment_form': comment_form})

def post_share(request, post):
    # Retrieve post by id
    post = get_object_or_404(Post, slug=post, status='published')
    sent = False

    if request.method == 'POST' :
        # Form was submitted
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # Form fields passed validation 
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = '{} ({}) recommends you reading "{}"'.format(cd['name'], cd['email'], post.title)
            message = 'Read "{}" at {}\n\n{}\'s comments: {}'.format(post.title, post_url, cd['name'], cd['comments'])
            send_mail(subject, message, 'user.agent.example@gmail.com', [cd['to']])
            sent = True                                            
    else:
        form = EmailPostForm()
    
    return render(request, 'blog/post_share.html', {'post' : post,
                                                    'form' : form, 
                                                    'sent' : sent})								
