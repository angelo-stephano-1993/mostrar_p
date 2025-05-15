# Django MySQL Docker App

This project is a Dockerized Django application that provides a RESTful API for managing products. It uses a MySQL database for data storage and includes phpMyAdmin for database management.

## Project Structure

```
django-mysql-docker-app
├── backend
│   ├── manage.py
│   ├── requirements.txt
│   ├── Dockerfile
│   ├── django_api
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   └── products
│       ├── __init__.py
│       ├── admin.py
│       ├── apps.py
│       ├── models.py
│       ├── serializers.py
│       ├── tests.py
│       ├── urls.py
│       └── views.py
├── docker-compose.yml
├── .env
└── README.md
```

## Getting Started

### Prerequisites

- Docker
- Docker Compose

### Setup

1. Clone the repository:

   ```
   git clone <repository-url>
   cd django-mysql-docker-app
   ```

2. Create a `.env` file in the root directory with the following content:

   ```
   MYSQL_ROOT_PASSWORD=root_password
   MYSQL_DATABASE=products_db
   MYSQL_USER=user
   MYSQL_PASSWORD=user_password
   DJANGO_SECRET_KEY=your_secret_key
   ```

3. Build and run the containers:

   ```
   docker-compose up --build
   ```

### Accessing the Application

- The Django API will be available at `http://localhost:8000/api/`.
- phpMyAdmin can be accessed at `http://localhost:8080/` using the credentials defined in the `.env` file.

### API Endpoints

- `GET /api/products/` - Retrieve a list of products in JSON format.
- `POST /api/products/` - Create a new product.
- `GET /api/products/<id>/` - Retrieve a specific product by ID.
- `PUT /api/products/<id>/` - Update a specific product by ID.
- `DELETE /api/products/<id>/` - Delete a specific product by ID.

### Running Tests

To run tests for the products application, execute the following command inside the backend container:

```
docker-compose exec backend python manage.py test products
```

### License

This project is licensed under the MIT License.