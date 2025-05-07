# Building an API for a Book Shop.

In this project, I will use FastAPI to build an API for a ecommerce website that sells books. 

The first step is to identify the participants or users of the API. The table below provides an overview of the users and their interactions with the API. 

| Participants |	Activities|
| ------------ | ------------ |
|User	       | Signup       |
|              | Signin       |
|              | SignOut      |
| |  |   
| Buyer	       |Browse Products |
|              | View           |
|              | Like/unlike Products |
|              | Add To Cart          |
|               | Edit Cart             |
|               |View Cart              |
|               | Create Order(Checkout) |
|               | View Order |
|               | Add/edit/remove payment method |
|               | View Likes |
|               | View Recommendations |
|               | View/Edit account |
|  |  |
| Admin	        | add/edit/archive Products |
|               | view all orders |
|               | view all users |
|               | view/edit order |
|               | view dashboard |
|               | View/edit user information |
|  |  |
| Owner	| admin activities |
|        | view/add/edit admin |

From the table above, here are the api endpoints for the site:

| Endpoint | Usage |
| -------- | ----- |
| /api/auth | User Authentication |
| /api/books | Books |
| /api/user | User management |
| /api/cart | Cart |
| /api/orders | Orders and Checkout |
| /api/payment | Payments |
| /api/wishlist | Wishlist |
| /api/reviews | Reviews |
| /api/stats | Stats for admin dashboard |

Some of the endpoints are independent: can function alone and some require a parent resource. 
The parent resources are:
/api/auth
/api/users
/api/authors
/api/books

The following status codes will be used in the app.

| Request Code |	Condition |	Verb |
| ------------ | ------------ | ---- |
| 200 OK	| Success | All |
| 201 Created |	Created| Post |
| 202 Accepted | Successful but incomplete | Post |
| 204 No Content |	Deleted	Delete |
| 401 Unauthorized | Authentication failed | All |
| 403 Forbidden	| Authorization Failed | All |
| 404 Not Found | Resource not Found | Get, Put, Delete | 


The tools for the app:
- FastAPI for HTTP requests.
- SQLAlchemy for database operations.
- Kubernetes to orchestrate containers.
- Docker for containers.
- JWT for authentication.
- Postgres for database management.

Microservices:
- Authentication Service
- Orders Service
- Payments Service
- Machine Learning Service
- Books Service


## Useful Commands
- Create a virtual environment to isolate the packages.
 ```virtualenv -p python3 venv```
- Activate the environment
```source venv/bin/activate```
- Install Pacges 
```pip install fastapi``
- View Packages
```pip list``
- Create requirements.txt file using the installed packages
```pip freeze > requirements.txt```
- Install packages in the requirements.txt file
```pip3 install -r requirements.txt```