from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.urls import reverse


class Author(models.Model):
    author_user = models.OneToOneField(User, on_delete=models.CASCADE)
    ratingAuthor = models.SmallIntegerField

    #Обновляет рейтинг текущего автора
    def update(self):
        post_sum = self.post_set.aggregate(postRating=Sum('rating')) # Все данные определённого поля автора
        temp_sum_p = 0
        temp_sum_p += post_sum.get('postRating')

        comment_sum = self.author_user.comment_set.aggregate(commentRating=Sum('rating'))
        temp_sum_c = 0
        temp_sum_c += comment_sum.get('commentRating')

        self.author_user = temp_sum_p * 3 + temp_sum_c
        self.save()

    def __str__(self):
        return self.author_user.username


class Category(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title


class Likeable(models.Model):
    rating = models.SmallIntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    class Meta:
        abstract = True


class Post(Likeable):
    time = models.DateTimeField(auto_now_add=True)
    post_category = models.ManyToManyField(Category, through='PostCategory')
    heading = models.CharField(max_length=255)
    text = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    # Переменные и константа для выбора (статья, новость)
    NEWS = 'NW'
    ARTICLE = 'AR'
    CATEGORY_CHOICES = (
        (ARTICLE, 'Статья'),
        (NEWS, 'Новость')
    )

    category_choices = models.CharField(max_length=2, choices=CATEGORY_CHOICES, default=ARTICLE)

    # Предварительный просмотр
    def preview(self):
        return f'{self.text[:123]} ...'

    def __str__(self):
        return self.heading

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])



class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(Likeable):
    text_com = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True)
    post_com = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text_com


class Subscription(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='subscriptions',
    )
    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        related_name='subscriptions',
    )