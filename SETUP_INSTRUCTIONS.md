# SumanthCommerce - Quick Setup Guide

## 🚀 Quick Start (Windows)

1. **Run the startup script:**
   ```bash
   start.bat
   ```

2. **Open your browser and visit:**
   ```
   http://127.0.0.1:8000
   ```

3. **Login with these accounts:**
   - **Admin**: username=`admin`, password=`admin123`
   - **Customer**: username=`customer1`, password=`password123`

## 🚀 Quick Start (Linux/Mac)

1. **Make the script executable and run:**
   ```bash
   chmod +x start.sh
   ./start.sh
   ```

2. **Open your browser and visit:**
   ```
   http://127.0.0.1:8000
   ```

## 🚀 Manual Setup

If the scripts don't work, follow these steps:

1. **Install dependencies:**
   ```bash
   pip install Django Pillow
   ```

2. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

3. **Populate sample data:**
   ```bash
   python manage.py populate_data
   ```

4. **Start the server:**
   ```bash
   python manage.py runserver
   ```

## 🎯 What You Can Do

### As a Customer:
- Browse products by category
- Search for products
- Add items to cart
- Place orders
- Write product reviews
- Add items to wishlist
- View order history

### As an Admin:
- Manage products and categories
- Update order statuses
- View all orders
- Manage user accounts
- Moderate reviews

## 📱 Features Included

- ✅ User registration and authentication
- ✅ Product catalog with categories
- ✅ Shopping cart functionality
- ✅ Order processing
- ✅ Product reviews and ratings
- ✅ Wishlist functionality
- ✅ Search and filtering
- ✅ Responsive design
- ✅ Admin panel
- ✅ Sample data

## 🔧 Troubleshooting

### Server won't start?
- Make sure you're in the project directory
- Check if port 8000 is available
- Try: `python manage.py runserver 8001`

### Database errors?
- Run: `python manage.py migrate`
- Delete `db.sqlite3` and run migrations again

### Static files not loading?
- Make sure `DEBUG = True` in settings
- Check browser console for errors

## 📁 Project Structure

```
webapp/
├── manage.py                 # Django management script
├── sumanth_commerce/         # Main project settings
├── store/                    # Main app
│   ├── models.py            # Database models
│   ├── views.py             # View functions
│   ├── templates/           # HTML templates
│   └── static/              # CSS/JS files
├── media/                   # User uploaded files
├── start.bat               # Windows startup script
├── start.sh                # Linux/Mac startup script
└── README.md               # Detailed documentation
```

## 🎉 Success!

If everything is working, you should see:
- A beautiful e-commerce homepage
- Product listings with images
- Working cart functionality
- User authentication
- Admin panel access

**Happy Shopping with SumanthCommerce! 🛒**
