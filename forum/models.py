from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


STATUS = ((0, "Draft"), (1, "Published"))

# Forum post model
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True,)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="forum_posts"
    )
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"The title of this post is {self.title}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        original_slug = self.slug
        counter = 1
        while Post.objects.filter(slug=self.slug).exclude(id=self.id).exists():
            self.slug = f"{original_slug}-{counter}"
            counter += 1
        super().save(*args, **kwargs)

# Forum comment model
class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.author.username

# Forum nested replies model
class Reply(models.Model):
    comment = models.ForeignKey(Comment, related_name="replies", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    reply = models.TextField()
    parent = models.ForeignKey("self", null=True, blank=True, related_name="child_replies", on_delete=models.CASCADE)

    class Meta:
        ordering = ['timestamp']

    def __str__(self):
        return f"Reply by {self.user.username} on {self.timestamp}"
        
    @property
    def get_replies(self):
        return self.child_replies.all()