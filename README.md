# 📌 Wallet API  

A simple **Django REST Framework** project to manage users and their wallet balances.  
This project was built as part of a technical assignment.  

---

## 🚀 Features
- List all users with their wallet balances  
- Update a user’s wallet (add funds, record transactions)  
- Fetch all wallet transactions for a specific user  
- Interactive API documentation with **Swagger**  

---

## 🛠️ Tech Stack
- **Backend:** Django, Django REST Framework  
- **Database:** SQLite (default, can be changed)  
- **API Docs:** drf-yasg (Swagger/OpenAPI)  

---

## 📂 Project Structure
    wallet_project/
    ├── wallet_api/ # Main Django project
    ├── wallet/ # App with models, views, urls
    ├── db.sqlite3 
    ├── manage.py
    └── requirements.txt


## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/wallet-api.git
cd wallet-api
````

### 2. Create & activate virtual environment
    python -m venv venv

    # Windows
    venv\Scripts\activate

    # Mac/Linux
    source venv/bin/activate

### 3. Install dependencies

    pip install -r requirements.txt

### 4. Run migrations

    python manage.py migrate

### 5. Create a superuser (for Django admin)

    python manage.py createsuperuser

### Run the server

    python manage.py runserver


## 🔗 API Endpoints

### Users

**List all users**

- GET /api/users/

### Wallet

**Update wallet balance**

- POST /api/wallet/update/

        {
        "user_id": 1,
        "amount": 100.0
        }

### Transactions

**Fetch user transactions**

- GET /api/transactions/{user_id}/

## 📖 API Documentation (Swagger)

    http://127.0.0.1:8000/swagger/

