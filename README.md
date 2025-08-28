# ALX Backend Caching: Property Listings Project

This project is a Django-based property listing application designed to demonstrate multi-level caching strategies using Redis. The entire development environment, including a PostgreSQL database and a Redis cache, is containerized with Docker for consistency and ease of setup.

## Key Features
- **Multi-level Caching**: Implements view-level and low-level queryset caching.
- **Cache Invalidation**: Uses Django signals to ensure data consistency.
- **Containerized Services**: Manages PostgreSQL and Redis with Docker Compose.
- **Database Optimization**: Reduces database load through intelligent caching.

## Tech Stack
- **Framework**: Django
- **Database**: PostgreSQL
- **Cache**: Redis
- **Containerization**: Docker & Docker Compose
- **Libraries**: `django-redis`, `psycopg2-binary`

---

## 🚀 Getting Started

Follow these instructions to get the project up and running on your local machine.

### Prerequisites
- [Python 3.8+](https://www.python.org/downloads/)
- [Docker](https://www.docker.com/get-started) and [Docker Compose](https://docs.docker.com/compose/install/)

### Installation and Setup

1.  **Clone the Repository:**
    ```sh
    git clone [https://github.com/](https://github.com/)<your-username>/alx-backend-caching_property_listings.git
    cd alx-backend-caching_property_listings
    ```

2.  **Create and Activate a Virtual Environment:**
    ```sh
    # Create the virtual environment
    python3 -m venv venv

    # Activate it (macOS/Linux)
    source venv/bin/activate

    # Or on Windows
    # .\venv\Scripts\activate
    ```

3.  **Install Python Dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4.  **Start the Docker Services:**
    This command will build and start the PostgreSQL and Redis containers in the background.
    ```sh
    docker-compose up -d --build
    ```

5.  **Apply Database Migrations:**
    This step creates the necessary tables in the PostgreSQL database.
    ```sh
    python manage.py migrate
    ```

6.  **Run the Django Development Server:**
    ```sh
    python manage.py runserver
    ```
    The application will be available at `http://127.0.0.1:8000`.

---

## Project Structure

```
alx-backend-caching_property_listings/
├── alx_backend_caching_property_listings/  # Django project configuration
├── properties/                         # Django app for property listings
├── docker-compose.yml                  # Defines Docker services (Postgres, Redis)
├── manage.py                           # Django's command-line utility
├── requirements.txt                    # Python package dependencies
└── README.md                           # This file
```