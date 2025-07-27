# 🛒 ShopKart - E-commerce Web Application

ShopKart is a fully-functional e-commerce website built using **Django**. It includes features like user registration/login, product catalog, category filtering, image management, cart functionality, and order placement.

## 🔗 Live Demo

🌐 [Visit ShopKart on Render](https://shopkart-5j96.onrender.com/)

---

## 🚀 Features

- 🧑‍💻 User Authentication (Register/Login/Logout)
- 📦 Product listing with categories
- 🖼️ Image handling using Cloudinary / local media
- 🛒 Add to Cart & Checkout functionality
- 📝 Order placement and invoice summary
- 📊 Admin Panel for product/category management

---

## 🛠️ Tech Stack

- **Frontend**: HTML, CSS, Bootstrap
- **Backend**: Python, Django
- **Database**: SQLite (default, can be upgraded to PostgreSQL)
- **Deployment**: Render
- **Media Handling**: Cloudinary / Django media

---

## 🧱 Folder Structure

# 🛒 ShopKart - E-commerce Web Application

ShopKart is a fully-functional e-commerce website built using **Django**. It includes features like user registration/login, product catalog, category filtering, image management, cart functionality, and order placement.

## 🔗 Live Demo

🌐 [Visit ShopKart on Render](https://shopkart-5j96.onrender.com/)

---

## 🚀 Features

- 🧑‍💻 User Authentication (Register/Login/Logout)
- 📦 Product listing with categories
- 🖼️ Image handling using Cloudinary / local media
- 🛒 Add to Cart & Checkout functionality
- 📝 Order placement and invoice summary
- 📊 Admin Panel for product/category management

---

## 🛠️ Tech Stack

- **Frontend**: HTML, CSS, Bootstrap
- **Backend**: Python, Django
- **Database**: SQLite (default, can be upgraded to PostgreSQL)
- **Deployment**: Render
- **Media Handling**: Cloudinary / Django media

---


---

## 🧑‍💻 Setup Instructions

1. Clone the repository
   ```bash
   git clone https://github.com/meghavardhan-git/ShopKart.git
   cd ShopKart
2.Create and activate virtual environment

python -m venv venv
source venv/bin/activate   # For Linux/macOS
venv\Scripts\activate      # For Windows

3.Install dependencies

pip install -r requirements.txt

4.Set up environment variables

Create a .env file and add the following:

SECRET_KEY=your_django_secret_key
DEBUG=True
CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret

or else on render add this in environment section

5.Run migrations and start server

python manage.py makemigrations
python manage.py migrate
python manage.py runserver

else add this commands to yaml for render deployment

📸 Screenshots
Home Page
<img width="1909" height="918" alt="image" src="https://github.com/user-attachments/assets/707594b7-581a-49e2-953e-069c2f1e3a9b" />

Collections page
<img width="1913" height="919" alt="image" src="https://github.com/user-attachments/assets/7f4e0b07-3a29-4c4c-aa1b-b08c15f8d372" />

Cart Page
<img width="1919" height="929" alt="image" src="https://github.com/user-attachments/assets/2a198d29-e3e5-440f-be54-2e96e255fbc4" />

Favorites Page
<img width="1906" height="909" alt="image" src="https://github.com/user-attachments/assets/d92c613b-b946-44fb-879b-4f5caa114186" />

Products Page
<img width="1897" height="910" alt="image" src="https://github.com/user-attachments/assets/e4ffcc17-c2e7-42c2-ada9-cb98d95d8c8f" />

📬 Contact
Created by Meghavardhan T – feel free to reach out!

Let me know if you’d like this tailored more to your deployment (e.g., mention specific AWS services, database choices, etc.) or if you want this pushed directly to your repo.
