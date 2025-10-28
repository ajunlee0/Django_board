from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Post, Comment

def index(request):
    posts = Post.objects.order_by("-created_at")
    return render(request, "board/post_list.html", {"posts": posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.order_by("created_at")
    context = {
        "post": post,
        "comments": comments,
    }
    return render(request, "board/post_detail.html", context)

def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == "POST":
        content = request.POST.get("content", "").strip()
        if content != "":
            Comment.objects.create(
                post=post,
                content=content,
            )

    return redirect("post_detail", post_id=post.id)

def new_post(request):
    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        content = request.POST.get("content", "").strip()

        if title != "" and content != "":
            post = Post.objects.create(
                title=title,
                content=content,
            )
            return redirect("post_detail", post_id=post.id)

        # 실패한 경우: 다시 폼 보여주기 + 에러 메시지 + 입력값 유지
        return render(
            request,
            "board/post_new.html",
            {
                "error": "제목과 내용을 모두 입력해주세요.",
                "title_value": title,
                "content_value": content,
            },
        )

    # GET일 때: 빈 폼 보여주기
    return render(request, "board/post_new.html")


# ✅ 공감(좋아요) 기능
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    # 안전하게: POST 요청으로만 좋아요를 받도록 하자 (버튼도 POST로 만들 거야)
    if request.method == "POST":
        post.likes += 1
        post.save()

    # 끝나면 다시 글 상세 페이지로
    return redirect("post_detail", post_id=post.id)
