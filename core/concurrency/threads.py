import concurrent.futures
import os
from asyncio import Future

import requests
import threading
import time
import json

# In Python ,only one thread executes at a time.
BASE_URL = "https://jsonplaceholder.typicode.com/"
thread_local = threading.local()


def get_post(post_id):
    post_url = f"{BASE_URL}posts/{post_id}"
    parsed_json = get_http(post_url)
    return parsed_json


def get_comment(post_id):
    comment_url = f"{BASE_URL}posts/{post_id}/comments"
    parsed_json = get_http(comment_url)
    return parsed_json


def get_http( url: str ):
    session = get_session()
    with session.get(url) as response:
        parsed_json = json.loads(response.text)
        return parsed_json


def get_session():
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
    return thread_local.session
def onSuccess(json_response_future):
    print(json_response_future.result())

with concurrent.futures.ThreadPoolExecutor(max_workers=os.cpu_count()) as executor:
    postFuture : Future = executor.submit(get_post, 1)
    commentsFuture : Future = executor.submit(get_comment, 1)
    postFuture.add_done_callback(onSuccess)
    commentsFuture.add_done_callback(onSuccess)


