
# Healthcare Backend API

A healthcare management backend built using Django REST Framework and PostgreSQL.

## Tech Stack

- Python
- Django
- Django REST Framework
- PostgreSQL
- JWT Authentication using Simple JWT

## Features

- User registration and login
- JWT access and refresh tokens
- Patient management
- Doctor management
- Patient-doctor assignments
- Authenticated API endpoints
- PostgreSQL database integration

## Project Setup

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd healthcare-backend
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root.

```env
SECRET_KEY=replace-with-a-secure-secret
DEBUG=True
DB_NAME=healthcare_db
DB_USER=your_postgres_username
DB_PASSWORD=your_postgres_password
DB_HOST=localhost
DB_PORT=5432
```

Update the database credentials for your PostgreSQL installation.

### 5. Create the PostgreSQL database

```sql
CREATE DATABASE healthcare_db;
```

### 6. Apply migrations

```bash
python manage.py migrate
```

### 7. Start the development server

```bash
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/`.

## API Endpoints

### Authentication

| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/auth/register/` | Register a user |
| POST | `/api/auth/login/` | Obtain JWT tokens |
| POST | `/api/auth/token/refresh/` | Refresh access token |

### Patients

| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/patients/` | Create a patient |
| GET | `/api/patients/` | List your patients |
| GET | `/api/patients/<id>/` | Retrieve a patient |
| PUT | `/api/patients/<id>/` | Update a patient |
| DELETE | `/api/patients/<id>/` | Delete a patient |

### Doctors

| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/doctors/` | Create a doctor |
| GET | `/api/doctors/` | List your doctors |
| GET | `/api/doctors/<id>/` | Retrieve a doctor |
| PUT | `/api/doctors/<id>/` | Update a doctor |
| DELETE | `/api/doctors/<id>/` | Delete a doctor |

### Patient-Doctor Mappings

| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/mappings/` | Assign a doctor to a patient |
| GET | `/api/mappings/` | List mappings |
| GET | `/api/mappings/<patient_id>/` | List doctors assigned to a patient |
| DELETE | `/api/mappings/<id>/` | Delete a mapping |

## Authentication

For protected endpoints, include the access token in the request header:

```text
Authorization: Bearer <access_token>
```

## Database

PostgreSQL is used to store user, patient, doctor, and mapping records. Django ORM manages database operations.

## License

Created as an academic assignment.
