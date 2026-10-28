# Healthcare Backend API - Miss Nurse Joy 🌸
# This is to grab your attention nothing else (^^)
## Yeah I have Deployed it on the Cloud so you need not take the effort for testing it on your machine locally : )

A healthcare management backend built using Django REST Framework and PostgreSQL.

**Status:** Deployed and working on Vercel with Neon PostgreSQL.

**Live API:** https://healthcare-backend-inky-one.vercel.app/

You can explore and test the API using Postman. Feel free to register a test account, obtain JWT tokens, and try out the available endpoints. Protected endpoints require authentication.

## Tech Stack

- Python
- Django
- Django REST Framework
- PostgreSQL
- JWT Authentication using Simple JWT
- Vercel (Backend Hosting)
- Neon (Managed PostgreSQL Database)
- Postman (API Testing)

## Features

- User registration and login
- JWT access and refresh tokens
- Patient management
- Doctor management
- Patient-doctor assignments
- Authenticated API endpoints
- PostgreSQL database integration
- Deployed backend with Vercel and Neon

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

The deployed application uses **Neon PostgreSQL** for database hosting and **Vercel** for backend deployment.

## Testing with Postman

The live API is available at:

`https://healthcare-backend-inky-one.vercel.app/`

You can use Postman to test registration, login, patient and doctor CRUD operations, and patient-doctor mappings.

For protected endpoints, first log in to obtain an access token, then select **Authorization → Bearer Token** in Postman and provide the token.

Have a good day ahead bye bye <33333
🌷🍀
