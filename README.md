# turnq

[![PyPI](https://img.shields.io/pypi/v/turnq)](https://pypi.org/project/turnq/)
[![PyPI - License](https://img.shields.io/pypi/l/turnq)](https://github.com/HexDecimal/turnq/blob/main/LICENSE)
[![Documentation Status](https://readthedocs.org/projects/turnq/badge/?version=latest)](https://turnq.readthedocs.io)
[![codecov](https://codecov.io/gh/HexDecimal/turnq/branch/main/graph/badge.svg?token=4Ak5QpTLZB)](https://codecov.io/gh/HexDecimal/turnq)
[![CommitsSinceLastRelease](https://img.shields.io/github/commits-since/HexDecimal/turnq/latest)](https://github.com/HexDecimal/turnq/blob/main/CHANGELOG.md)

A turn-based scheduler built on top of heapq.

```py

>>> import turnq
>>> from dataclasses import dataclass
>>> @dataclass
... class Actor:
...     speed: int
...
...     def act(self, tqueue: "turnq.TurnQueue[Actor]") -> None:
...         """Reschedule `self` into the `tqueue` at the rate of `self.speed`."""
...         tqueue.schedule(interval=self.speed, value=self)
...
>>> scheduler = turnq.TurnQueue[Actor]()
>>> scheduler.schedule(interval=0, value=Actor(speed=3))
Ticket(time=0, uid=0, value=Actor(speed=3), insert_time=0)
>>> scheduler.schedule(interval=0, value=Actor(speed=5))
Ticket(time=0, uid=1, value=Actor(speed=5), insert_time=0)
>>> while scheduler.time < 20:
...     ticket = scheduler.pop()  # Pop the next scheduled Ticket
...     print(ticket)
...     assert scheduler.time == ticket.time  # TurnQueue.time advances to the recently popped Ticket
...     ticket.value.act(scheduler)  # Call the Actor with the scheduler, allowing it to reschedule itself
...
Ticket(time=0, uid=0, value=Actor(speed=3), insert_time=0)
Ticket(time=0, uid=1, value=Actor(speed=5), insert_time=0)
Ticket(time=3, uid=2, value=Actor(speed=3), insert_time=0)
Ticket(time=5, uid=3, value=Actor(speed=5), insert_time=0)
Ticket(time=6, uid=4, value=Actor(speed=3), insert_time=3)
Ticket(time=9, uid=6, value=Actor(speed=3), insert_time=6)
Ticket(time=10, uid=5, value=Actor(speed=5), insert_time=5)
Ticket(time=12, uid=7, value=Actor(speed=3), insert_time=9)
Ticket(time=15, uid=8, value=Actor(speed=5), insert_time=10)
Ticket(time=15, uid=9, value=Actor(speed=3), insert_time=12)
Ticket(time=18, uid=11, value=Actor(speed=3), insert_time=15)
Ticket(time=20, uid=10, value=Actor(speed=5), insert_time=15)

```
