# Django Medical Inventory Management System

A Django project for managing medical inventory with user authentication, CRUD operations, and API endpoints using Django Rest Framework.

## Overview

The Medical Inventory Management System is designed to efficiently manage medical inventory with features such as user management, seller management, chemical compound tracking, medicine information, and inventory management. The project utilizes Django Rest Framework for building robust APIs and includes custom authentication using JWT tokens.

## Features

- User Management (Login, Signup)
- Seller Management
- Chemical Compound CRUD operations
- Medicine Information CRUD operations
- Inventory Management
- JWT Token-based Authentication

## Getting Started

### Prerequisites

Ensure you have the following prerequisites installed:

- Python (>=3.6)
- Pip
- Virtualenv (optional but recommended)

### Installation

1. Clone the repository:

   ```bash
   git clone git@github.com:Pranav-001/Django-Medical-Inventory.git
   cd Django-Medical-Inventory
   ```

2. Create and activate a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Configuration

Configure the project settings, database, and environment variables as needed. Include instructions for migrations and other necessary setup steps.

## Usage

```bash
python manage.py runserver
```

Visit `http://localhost:8000` in your web browser.

## API Endpoints

Document the available API endpoints along with examples and any necessary details for using them.

- `/admin/` : admin site

- `/user/signup/` : POST request for user signup.
- `/user/login/` : POST request for user login.
- `/user/all/` : GET Request to list all users.
- `/user/select/<int:pk>/` : GET Request to fetch a single user.
- `/user/delete/<int:pk>/` : GET Request to delete a user.
- `/user/update/<int:pk>/` : POST Request to update user info.
  
- `/seller/all/` : GET Request to list all sellers.
- `/seller/signup/` : POST request for seller signup.
- `/seller/select/<int:pk>/` : GET Request to fetch a single seller.
- `/seller/delete/<int:pk>/` : GET Request to delete a seller.
- `/seller/update/<int:pk>/` : POST Request to update seller info. 

- `/company/all/` : GET Request to list all register medicine company.
- `/company/insert/` : POST Request to insert a new medicine company.
- `/company/select/<int:pk>/` : GET Request to fetch a single company.
- `/company/update/<int:pk>/` : GET Request to delete a company.
- `/company/delete/<int:pk>/` : POST Request to update company info.

- `/inventory/all/` : GET Request to fetch all inventory info.
- `/inventory/insert/` : POST Request to insert a new inventory stock.


## Authentication

This project implements JWT token-based authentication with tokens encoded using a `jwt_key`. The tokens include user_id, datetime values, and are valid for 1 hour.

## License

This project is licensed under the [MIT License](LICENSE).
