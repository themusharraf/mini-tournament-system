# Makefile
.PHONY: migrate-create migrate-up migrate-down migrate-history
# New migration create
migrate-create:
	alembic revision --autogenerate -m "$(msg)"

# Migration usage
migrate-up:
	alembic upgrade head

# Undo the last migration
migrate-down:
	alembic downgrade -1

# Migration history
migrate-history:
	alembic history --verbose


help:
	@echo "Available commands:"
	@echo "  make migrate-create msg='Description' - Create new migration"
	@echo "  make migrate-up                     - Apply migrations"
	@echo "  make migrate-down                   - Rollback last migration"
	@echo "  make migrate-history                - Show migration history"


mypy:
	mypy .

ruff:
	ruff check .

ruff-fix:
	ruff check . --fix

black:
	black .

test:
	pytest -v
