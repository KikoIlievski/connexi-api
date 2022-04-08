# python-api

A social media RESTful API designed using [FastAPI](https://fastapi.tiangolo.com/) and [PostgreSQL](https://www.postgresql.org/). The documentation for the API can be found [here](https://kiko-python-api.herokuapp.com/docs).

This project gave me the opportunity to explore some of the worderful design patterns and tech stacks that make up backend development. 

* Through the project, the first steps were fleshing out a local devolpment environment, using only FastAPI. I setup the core CRUD functionality, testing along the way 
using [Postman](https://www.postman.com/), but beyond recieving HTTP requests, the API couldn't do anything with the information. 
* Next, I introduced PostgreSQL into the project. First this began as writing SQL queries as strings in Python and passing them to the database, but eventually
I shifted to implementing Object Relational Mapping (ORM), using [SQLAlchemy](https://www.sqlalchemy.org/). This made communicating with the database much easier 
and cleaner, as it could all be done using Python functions, instead of writing SQL strings in my code. As well as this, it provided a level of protection against SQL 
injection attacks. 
* At this point, I had a database that could communicate with my API; the database had a table to store posts and users, but the concept of a user being able to sign in, 
was yet to be introduced. So from here the next step was to introduce [OAuth2](https://oauth.net/2/) and [JWT](https://github.com/mpdavis/python-jose)(JSON web tokens) to allow a user to login, and remember the logged in state of the user. Here I learnt about the best practices of hashing passwords, and how (JWT)s worked.
* The database was beginning to get large, and it was cumbersome to edit existing tables whenever I wanted to make a change; a perfect oppurtunity to learn 
the joys of database migration tools! I introduced [Alembic](https://alembic.sqlalchemy.org/en/latest/) into the project, and with it, came the ability to change
the database in exactly the way I wanted, with the benefit of each version being stored. 
* Here came the scary part of the project for me. Almost every project I had done prior to this project, I had only ever developed locally. 
The world of hosting on a public domain, had remained foreign to me, so I had a lot to learn! CORS, SSH, reverse proxies, firewalls, development/production branches... 
The things I learned here, made me feel like I had finally began to mature as a developer. I was finally beginning to see the proper, 
industry standard of doing some tasks (turns out, it's not "best practice" to hardcode your passwords and credentials directly into your code pushed to GitHub :D)
* I set up my own Linux server, to serve as an IP from which the world could access my baby. I began to setup [NGINX](https://www.nginx.com/), but an issue arose
Getting an SSL certificate for my HTTP to have that glorious "S" on the end, would be a bit ~~expensive~~ *ahem* 'difficult'. So I tucked my tail between my legs, 
and decided to host the project on [Heroku](heroku.com). *sigh*, the wonderful feeling of reinventing the wheel was gone just like that (I'm looking at you! 
You know the feeling I mean!! :D) 

This is where the project sits for now. My plans in the very near future, are build a frontend for this API, exploring the CI/CD pipeline, and 
exploring the world of [Docker](https://www.docker.com/). 

This project was my first introduction to all-out backend development, and I closely followed [this 20 hour course](https://www.youtube.com/watch?v=0sOvCWFmrtA) 
offered by FreeCodeCamp. I'm incredibly grateful to [Sanjeev Thiyagarajan](https://github.com/Sanjeev-Thiyagarajan) for putting together such an 
amazing comprehensive course!
