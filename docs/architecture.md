# StayWise API — Architecture

StayWise is a backend API for managing PG/hostel operations.

## Technology Stack

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Alembic
- Pydantic
- JWT authentication

## Architecture

```text
Client
  |
  v
FastAPI Router
  |
  v
Pydantic Schema
  |
  v
Service / CRUD Layer
  |
  v
SQLAlchemy ORM
  |
  v
PostgreSQL

Application Structure
core/

Application-wide configuration and settings.

database/

Database engine, SQLAlchemy Base and database session dependency.

models/

SQLAlchemy models representing database tables.

schemas/

Pydantic schemas used for request validation and response serialization.

routers/

HTTP endpoints grouped by resource.

crud/

Database operations such as create, read, update and delete.

services/

Business logic that should remain separate from HTTP routing and direct database operations.

dependencies/

Reusable FastAPI dependencies such as authentication and authorization.

utils/

Reusable helper functions.

Database Migrations

Alembic is used to version and apply database schema changes.

Application Structure
core/

Application-wide configuration and settings.

database/

Database engine, SQLAlchemy Base and database session dependency.

models/

SQLAlchemy models representing database tables.

schemas/

Pydantic schemas used for request validation and response serialization.

routers/

HTTP endpoints grouped by resource.

crud/

Database operations such as create, read, update and delete.

services/

Business logic that should remain separate from HTTP routing and direct database operations.

dependencies/

Reusable FastAPI dependencies such as authentication and authorization.

utils/

Reusable helper functions.

Database Migrations

Alembic is used to version and apply database schema changes.

Multi-Tenancy Design

The application is designed around a shared PostgreSQL database and shared schema.

Tenant-specific records are associated with a hostel/tenant identifier.

                    StayWise API
                         |
              Shared PostgreSQL DB
                         |
          +--------------+--------------+
          |                             |
       Hostel A                      Hostel B
          |                             |
       Users/Rooms                  Users/Rooms
       Meals/etc.                   Meals/etc.

Authenticated requests will determine the user's tenant/hostel context, and tenant-scoped queries will use that context to prevent access to another hostel's data.

Authentication

The planned authentication flow uses JWT.

Login
  |
  v
Verify credentials
  |
  v
Generate JWT
  |
  v
Client sends Bearer token
  |
  v
Authentication dependency
  |
  v
Identify user + role + tenant

Current Development Status

The project is under active development.

Current foundation includes:

FastAPI project structure
PostgreSQL connection
SQLAlchemy configuration
Alembic migrations
Initial user model/database schema

Upcoming modules include authentication, hostel management, rooms, tenants and meal-related functionality.

