from django.test import TestCase
from blog.models import Comment, Post
from django.contrib.auth.models import User


class CommentTest(TestCase):

    def setUp(self) -> None:
        self.user = User.objects.create_user(username='test')
        self.post = Post.objects.create(author=self.user, title='test-post', summary='this', content='test')

    def test_can_create_comments_for_users_and_posts(self):
        c1 = Comment.objects.create(creator=self.user, content='test', content_object=self.user)
        self.assertEqual(c1.content_type.model_class(), User)
        self.assertEqual(Comment.objects.count(), 1)

        c2 = Comment.objects.create(creator=self.user, content='test2', content_object=self.post)
        self.assertEqual(c2.content_type.model_class(), Post)
        self.assertEqual(Comment.objects.count(), 2)
