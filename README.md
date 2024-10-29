# SCA API

This Django-based API allows the management of missions, targets, and spy cats. The API supports CRUD operations for missions, the ability to update targets within a mission, and the management of spy cats and their availability.

## Overview

The **SCA API** is designed to manage missions for spy cats. Each mission can have multiple targets, and a spy cat can be assigned to a mission. Once a mission is marked as complete, the assigned cat is made available for new assignments, and targets can be updated or completed within a mission.

## Features

- **Manage Spy Cats**: Add, update, delete, and list spy cats.
- **Manage Missions**: Create, update, delete, and list missions.
- **Manage Targets**: Update targets within a mission.
- **Assign Cats to Missions**: Manage cat assignments to missions.
- **Complete Missions**: Mark missions as complete and unassign cats.

### Prerequisites

- Python 3.8+
- Django 3.1+
- Django REST Framework
- Poetry

### Installation

1. Clone the repository
   ```sh
      git clone <repository-url>
      cd <repository-directory>
      ```
2. Install Poetry if you don't have it installed
   ```sh
   curl -sSL https://install.python-poetry.org | python3 -
   ```
3. Install dependencies
   ```sh
    poetry install
    ```
4. Create a `.env` file in the root directory with the following content as in the `.env.example` file
5. Apply migrations
    ```sh
    poetry run python manage.py migrate
    ```
6. Start the server
    ```sh
    poetry run python manage.py runserver
    ```
7. Access the API at `http://localhost:8000/api/`

8. Postman collection for testing endpoints `https://drive.google.com/file/d/1vcjYFniVLbTshgiMStn9BiEJDodKbB10/view`
