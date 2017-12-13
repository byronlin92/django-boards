from django.test import TestCase
from django.core.urlresolvers import reverse
from django.urls import resolve #match a requested URL with a list of URL in urls.py
from ..views import BoardListView, new_topic
from ..models import Board, Topic, Post
from ..forms import NewTopicForm
from django.contrib.auth.models import User

class HomeTests(TestCase):
    def setUp(self):
        self.board = Board.objects.create(name='Django', description='Django board.')
        url = reverse('home')
        self.response = self.client.get(url)

    def test_home_view_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func.view_class, BoardListView)

#est if the response body contains a given text. The text we are using in the test,
#is the href part of an a tag. So basically we are testing if the response body has the text
#href="/boards/1/".
    def test_home_view_contains_link_to_topics_page(self):
        board_topics_url = reverse('board_topics', kwargs = {'pk':self.board.pk})
        self.assertContains(self.response, 'href="{0}"'.format(board_topics_url))
