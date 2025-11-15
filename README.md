
# Meli API CRUD

Example API (FastAPI + SQLAlchemy) to manage products. This project is configured to run with Docker Compose — the stack includes the Python API and a PostgreSQL database.

## Highlights

- Technologies: FastAPI, SQLAlchemy, PostgreSQL
- API port: 8000 (mapped by docker-compose)
- Database: PostgreSQL (data persists in `postgres-data/`)

## Repository structure

- `backend/` — API source code (FastAPI)
	- `main.py` — creates tables and registers the router
	- `router.py` — API routes for `/products`
	- `crud.py` — database access logic (CRUD)
	- `database.py` — SQLAlchemy configuration / Session
	- `models.py` — SQLAlchemy models (table `products`)
	- `schema.py` — Pydantic schemas (request/response)
	- `Dockerfile` — app image
- `docker-compose.yml` — orchestrates API + Postgres

## Requirements

- Docker and Docker Compose installed
- (Optional) Python 3.10+ and a local Postgres if you prefer to run without Docker

## Running with Docker (recommended)

1. From the repository root, build and start the services:

```powershell
docker-compose up --build -d
```

2. Optional: follow API logs:

```powershell
docker-compose logs -f api
```

3. The API will be available at http://localhost:8000

Notes:
- The `docker-compose.yml` already sets the `DATABASE_URL` environment variable used by the application:
	- `postgresql://user:password@postgres:5432/meli`
- The Postgres service exposes port 5432 and persists data under `postgres-data/`.

## Running locally without Docker

1. Create and activate a virtual environment:

```powershell
python -m venv .venv; .\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r backend/requirements.txt
```

3. Set the `DATABASE_URL` environment variable to point to an accessible Postgres instance. Example (PowerShell):

```powershell
$env:DATABASE_URL = "postgresql://user:password@localhost:5432/meli"
```

4. Run the API with uvicorn from the project root:

```powershell
uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
```

## Main endpoints

The API exposes CRUD routes for `products` under `/products`.

- GET /products/ — list all products
- GET /products/{product_id} — get a product by id
- POST /products/ — create a product
- PUT /products/{product_id} — update a product
- DELETE /products/{product_id} — delete a product

Example payload for creation (POST /products/):

```json
{
	"name": "Sample Product",
	"description": "Optional description",
	"price": 19.9,
	"category": "electronics",
	"supplier_email": "supplier@example.com"
}
```

Validation notes:
- `price` must be a positive number (PositiveFloat)
- `supplier_email` must be a valid email address

You can also access the interactive FastAPI docs at:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Database / model

The `products` table contains the following fields (see `models.py`):

- id (int, PK)
- name (string)
- description (string, optional)
- price (float)
- category (string, optional)
- supplier_email (string)
- created_at, updated_at (timestamps)

## Helpful tips

- To reset the database (delete persisted data) stop the containers and remove `postgres-data/` (warning: this permanently deletes data):

```powershell
docker-compose down
Remove-Item -Recurse -Force .\postgres-data
```

- If you change models (`models.py`), the app will create tables automatically on startup via `models.Base.metadata.create_all(bind=engine)`, but database migrations are not configured (e.g. Alembic is not included).

## Contributing

If you'd like to contribute, open an issue or submit a PR. For schema changes, consider adding migrations in the future.

## License

This repository follows the `LICENSE` file in the root.

---

Would you like me to also add curl examples for each endpoint or a small pytest suite to exercise the API? If yes, tell me which you prefer and I will add it.

