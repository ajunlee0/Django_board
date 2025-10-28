from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)      # 글 제목
    content = models.TextField()                  # 글 본문
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.PositiveIntegerField(default=0)  # 공감 수

    def __str__(self):
        return f"{self.id}. {self.title}"


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comments",
    )
    content = models.TextField()                  # 댓글 내용
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment on Post {self.post_id}: {self.content[:20]}"
