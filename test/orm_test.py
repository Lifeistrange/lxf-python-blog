#!/usr/bin/env python3
# coding=utf-8

import sys
from static import sql
from static.model import User, Blog, Comment
import asyncio

loop = asyncio.get_event_loop()

@asyncio.coroutine
def test():
    yield from sql.create_pool(loop=loop, user='www-data', password='www-data', db='blog')

    u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank', admin=True)

    yield from u.save()

loop.run_until_complete(test())
loop.close()
if loop.is_closed():
    sys.exit(0)
