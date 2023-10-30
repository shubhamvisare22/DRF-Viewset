# Project Name

**Description**: A CRUD-based project using Django Rest Framework (DRF) ViewSets.

## Overview

This project demonstrates basic CRUD operations for an "Employee" model using DRF ViewSets. It includes:

- Create, Read, Update, Delete (CRUD) operations.
- Use of Postman collection for testing.

## Installation

1. Clone the repository.
2. Create and activate a virtual environment.
3. Install dependencies: `pip install -r requirements.txt`.
4. Apply migrations: `python manage.py migrate`.
5. Run the development server: `python manage.py runserver`.

## Usage

- Create: POST to `/create-emp/`.
- Read: GET to `/list-emp/` or `/retrieve-emp/<employee_id>/`.
- Update: PUT to `/update-emp/<employee_id>/`.
- Partial Update: PATCH to `/partial_update-emp/<employee_id>/`.
- Delete: DELETE to `/delete-emp/<employee_id>/`.

- Use Postman collection in the `postman` folder for testing.

## Contributing

Fork, create a feature branch, commit changes, and make a pull request.

## License

MIT License.

## Acknowledgments

- Built with Django and DRF.
