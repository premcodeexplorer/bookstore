# 📚 Django Bookstore Application

A complete e-commerce bookstore built with Django, MySQL, and Bootstrap. Features user authentication, shopping cart, book catalog, and admin dashboard.

## 📸 Screenshots
![Screenshot 2025-04-11 021900](https://github.com/user-attachments/assets/e8be2604-8bf2-4a7c-99b9-9d972da591a3)
![Screenshot 2025-04-11 022150](https://github.com/user-attachments/assets/8ab53ec4-2ed4-4673-8156-53d7cb2c7077)
![Screenshot 2025-04-11 021933](https://github.com/user-attachments/assets/687a5333-697f-4329-aab3-f9622823733d)
![Screenshot 2025-04-11 021921](https://github.com/user-attachments/assets/e95c4574-32f4-4968-ad7d-3b92b3490e11)


## ✨ Features

- **User Authentication**: Login, logout, and registration system
- **Book Catalog**: Browse books by category/publication
- **Shopping Cart**: Add/remove items, view cart total
- **Admin Dashboard**: Manage books, publications, and orders
- **Responsive Design**: Works on mobile and desktop

## 🛠️ Technologies Used

- **Backend**: Django 5.2
- **Database**: MySQL
- **Frontend**: Bootstrap 5, HTML5, CSS3
- **Authentication**: Django Auth System
- **Deployment**: (Specify when deployed)

## 🚀 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/premcodeexplorer/bookstore.git
   cd bookstore
   ```
2. Set up virtual environment:
    ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate    # Windows
   ```
3. Install dependencies:
  ```bash
   pip install -r requirements.txt
   ```
4. Configure MySQL:
   ```bash
   CREATE DATABASE bookstore_db;
   CREATE USER 'bookstore_user'@'localhost' IDENTIFIED BY 'yourpassword';
   GRANT ALL PRIVILEGES ON bookstore_db.* TO 'bookstore_user'@'localhost';
   ```
5. Run migrations:
   ```bash
   python manage.py migrate
   ```
6. Create superuser:
    ```bash
   python manage.py createsuperuser
   ```
7. Run development server:
   ```bash
   python manage.py runserver
   ```
##📂 Project Structure
bookstore_project/
├── bookstore/               # Main app
│   ├── migrations/          # Database migrations
│   ├── static/              # CSS, JS, images
│   ├── templates/           # HTML templates
│   ├── admin.py             # Admin config
│   ├── models.py            # Database models
│   └── views.py             # Application logic
├── bookstore_project/       # Project config
└── manage.py                # Django CLI


