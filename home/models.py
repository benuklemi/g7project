from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.timezone import now
from ckeditor_uploader.fields import RichTextUploadingField
from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField

# Create your models here.
STATUS = (
    (0, "Draft"),
    (1, "Published")
)


class Category(models.Model):  # Category for the Article
    title = models.CharField(max_length=200)  # Title of the Category
    created_on = models.DateTimeField(auto_now_add=True)  # Date of creation

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['title']

    def __str__(self):
        return self.title


class BlogPost(models.Model):
    # Title of the Article
    title = models.CharField(max_length=200, unique=True)
    # Unique identifier for the article
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(upload_to="profile_pics", blank=True, null=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts')  # Author of the Article
    # Short Description of the article
    description = models.CharField(max_length=500)
    # Content of the article, you need to install CKEditor
    content = RichTextUploadingField(config_name='awesome_ckeditor')
    body = RichTextField (config_name='awesome_ckeditor')
    tags = TaggableManager()  # Tags for a Particular Article, You need to install Taggit
    category = models.ForeignKey(
        'Category', related_name='category', on_delete=models.CASCADE)  # Category of the article
    keywords = models.CharField(max_length=250)  # Keywords to be used in SEO
    # Cover Image of the article
    cover = models.ImageField(upload_to='images/')
    created_on = models.DateTimeField(auto_now_add=True)  # Date of creation
    updated_on = models.DateTimeField(auto_now=True)  # Date of updation
    # Status of the Article either Draft or Published
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:detail", args=[str(self.slug)])


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to="profile_pics", blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    phone_no = models.CharField(max_length=15,  blank=True, null=True)
    facebook = models.CharField(max_length=300, blank=True, null=True)
    instagram = models.CharField(max_length=300, blank=True, null=True)
    linkedin = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return str(self.user)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    blog = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    parent_comment = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True)
    dateTime = models.DateTimeField(default=now)

    def __str__(self):
        return self.user.username + " Comment: " + self.content