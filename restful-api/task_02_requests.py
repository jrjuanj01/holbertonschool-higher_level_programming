#!/usr/bin/python3
"""API Request module"""
import requests, csv


def fetch_and_print_posts():
    """Requests Post data fron JSONPlaceholder"""

    post_data = requests.get('https://jsonplaceholder.typicode.com/posts')
    print(f"Status Code: {post_data.status_code}")
    if post_data.status_code >= 200 and post_data.status_code < 300:
        for posts in post_data.json():
            print(posts["title"])


def fetch_and_save_posts():
    """Requests Post data fron JSONPlaceholder"""

    post_data = requests.get('https://jsonplaceholder.typicode.com/posts')
    print(f"Status Code: {post_data.status_code}")
    if post_data.status_code >= 200 and post_data.status_code < 300:
        new_data = []
        for posts in post_data.json():
            new_data.append({'id': posts['id'], 'title': posts['title'],
                            'body' : posts['body']})
        fieldnames = ['id', 'title', 'body']
        with open('posts.csv', "w", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for row in new_data:
                writer.writerow(row)
