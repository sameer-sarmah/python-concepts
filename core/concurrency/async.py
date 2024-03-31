import asyncio
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


async def get_post( post_id ):
    post_url = f"{BASE_URL}posts/{post_id}"
    parsed_json = get_http(post_url)
    return parsed_json


async def get_comment( post_id ):
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

async def execute_tasks():
    loop = asyncio.get_running_loop()
    get_post_task = asyncio.create_task(get_post(1))
    get_post_task.add_done_callback(onSuccess)
    get_comment_task = asyncio.create_task(get_comment(1))
    get_comment_task.add_done_callback(onSuccess)

async def wait_for_coroutines_to_complete():
    loop = asyncio.get_running_loop()
    results = await asyncio.gather(get_post(1), get_comment(1))
    post = results[0]
    print(post)
    comments = results[1]
    print(comments)

async def wait_for_tasks_to_complete():
    loop = asyncio.get_running_loop()
    get_post_task = asyncio.create_task(get_post(1))
    get_comment_task = asyncio.create_task(get_comment(1))
    tasks = [get_post_task,get_comment_task]
    results = await asyncio.wait(tasks)
    post = results[0].pop().result()
    print(post)
    comments = results[0].pop().result()
    print(comments)

# asyncio.run(execute_tasks())
# asyncio.run(wait_for_coroutines_to_complete())
asyncio.run(wait_for_tasks_to_complete())