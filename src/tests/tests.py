from django.urls import reverse
from rest_framework.test import APIClient


def test_posts_availability():
    client = APIClient()
    url = reverse("api-blog:posts")
    response = client.get(url)
    assert response.status_code == 200


def test_comments_availability():
    client = APIClient()
    url = reverse("api-blog:comments")
    response = client.get(url)
    assert response.status_code == 200


def test_posts_and_comments():

    # start posts test

    client = APIClient()
    url_posts = reverse("api-blog:posts")
    response = client.get(url_posts)
    assert response.status_code == 200

    response_post = client.post(
        url_posts,
        data={
            "title": "Hello",
            "votes": 2780,
            "author": "марина",
            "link": "https://www.google.com/",
        },
        format="json",
    )
    assert response_post.status_code == 201
    assert response_post.json().get("title") == "Hello"
    assert response_post.json().get("votes") == 2780
    assert response_post.json().get("author") == "марина"
    assert response_post.json().get("link") == "https://www.google.com/"

    url_post = reverse("api-blog:post", args=[f'{response_post.json().get("id")}'])
    response_get = client.get(url_post)
    assert response_get.status_code == 200

    response_patch = client.patch(url_post, data={"votes": 3100}, format="json",)
    assert response_patch.status_code == 200
    assert response_patch.json().get("title") == "Hello"
    assert response_patch.json().get("votes") == 3100
    assert response_patch.json().get("author") == "марина"
    assert response_patch.json().get("link") == "https://www.google.com/"

    response_put = client.put(
        url_post,
        data={
            "title": "Not_Hello",
            "votes": 22,
            "author": "Татьяна",
            "link": "https://www.gogle.com/",
        },
        format="json",
    )

    assert response_put.status_code == 200
    assert response_put.json().get("title") == "Not_Hello"
    assert response_put.json().get("votes") == 22
    assert response_put.json().get("author") == "Татьяна"
    assert response_put.json().get("link") == "https://www.gogle.com/"

    # start comments test

    url_comments = reverse("api-blog:comments")
    response = client.get(url_comments)
    assert response.status_code == 200

    response_post = client.post(
        url_comments,
        data={"post": 1, "content": "Nice post!", "author": "Kevin",},
        format="json",
    )
    assert response_post.status_code == 201
    assert response_post.json().get("post") == 1
    assert response_post.json().get("content") == "Nice post!"
    assert response_post.json().get("author") == "Kevin"

    url_comment = reverse(
        "api-blog:comment", args=[f'{response_post.json().get("id")}']
    )
    response_get = client.get(url_comment)
    assert response_get.status_code == 200

    response_patch = client.patch(
        url_comment, data={"content": "Great Post!"}, format="json",
    )
    assert response_patch.status_code == 200
    assert response_patch.json().get("post") == 1
    assert response_patch.json().get("content") == "Great Post!"
    assert response_patch.json().get("author") == "Kevin"

    response_put = client.put(
        url_comment,
        data={"post": 1, "content": "Like it!", "author": "John",},
        format="json",
    )

    assert response_put.status_code == 200
    assert response_put.json().get("post") == 1
    assert response_put.json().get("content") == "Like it!"
    assert response_put.json().get("author") == "John"

    response_delete = client.delete(url_comment)
    assert response_delete.status_code == 204

    response_delete = client.delete(url_post)
    assert response_delete.status_code == 204
