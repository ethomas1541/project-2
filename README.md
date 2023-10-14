Elijah Thomas
ethomas7@uoregon.edu

CS 322 Project 1

Reiteration of Project 1 that uses Docker and Flask to make it more portable, maintainable and scalable.

/web/app.py has config parsing logic that has worked flawlessly on my machine, with fallback logic in case default.ini
is needed. Four routes are defined, the default route (trivia.html), an open-ended route that accepts any filename,
and error handlers for errors 403 and 404.

403 needs to be invoked manually but Flask itself appears to handle 404. Either way, the respective error handlers
each fire no matter how error 403 or 404 was fired.