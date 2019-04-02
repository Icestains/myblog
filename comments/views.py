from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post

from .models import Comment
from .forms import CommentForm


# Create your views here.


def post_comment(request, post_pk):
    # 获取关联的博客
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == 'POST':
        # 获取用户提交在post里的数据
        form = CommentForm(request.POST)
        # 检查数据合法性
        if form.is_valid():
            # 数据合法 保存数据并生成Comment模型类实例
            comment = form.save(commit=False)
            # 评论和博客关联
            comment.post = post
            comment.save()
            return redirect(post)
        else:
            comment_list = post.comment_set.all()
            context = {
                'post': post,
                'form': form,
                'comment_list': comment_list
            }
            return render(request, 'blog/detail.html', context=context)
        return redirect(post)
