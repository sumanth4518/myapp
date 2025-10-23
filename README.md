# SumanthCommerce - Django E-commerce Application

A full-featured Django e-commerce application inspired by Amazon, built for local development and testing.

## Features

- **User Management**: Registration, login, user profiles
- **Product Catalog**: Categories, products with images, search and filtering
- **Shopping Cart**: Add/remove items, quantity management
- **Order Management**: Checkout, order history, order tracking
- **Reviews & Ratings**: Product reviews and star ratings
- **Wishlist**: Save favorite products
- **Admin Panel**: Complete product and order management
- **Responsive Design**: Mobile-friendly Bootstrap UI

## Tech Stack

- **Backend**: Django 5.1+
- **Database**: SQLite (for local development)
- **Frontend**: Django Templates + Bootstrap 5
- **Static Files**: Local file serving
- **Authentication**: Django's built-in auth system

## Quick Start

### 1. Clone and Setup

```bash
# Navigate to the project directory
cd webapp

# Install dependencies (if using virtual environment)
pip install django pillow

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser
```

### 2. Populate Sample Data

```bash
# Load sample products and categories
python manage.py populate_data
```

This command will create:
- Sample categories and products
- Admin user (username: `admin`, password: `admin123`)
- Test customer users

### 3. Run the Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` to see the application.

## Default Users

After running `populate_data`, you can login with:

- **Admin**: username=`admin`, password=`admin123`
- **Customer**: username=`customer1`, password=`password123`

## Project Structure

```
sumanth_commerce/
├── manage.py
├── sumanth_commerce/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── store/
│   ├── models.py          # Database models
│   ├── views.py           # View functions
│   ├── urls.py            # URL routing
│   ├── forms.py           # Django forms
│   ├── admin.py           # Admin configuration
│   ├── templates/store/   # HTML templates
│   ├── static/store/      # CSS/JS files
│   └── management/commands/
│       └── populate_data.py
├── media/                 # User uploaded files
└── README.md
```

## Key Features Explained

### 1. User Authentication
- User registration and login
- Password reset functionality
- User profiles and order history

### 2. Product Management
- Hierarchical categories
- Product images and descriptions
- Stock management
- Search and filtering

### 3. Shopping Cart
- Session-based cart for guests
- User-linked cart for logged-in users
- Add/remove/update quantities

### 4. Order Processing
- Simple checkout form
- Order confirmation
- Order status tracking
- Admin order management

### 5. Reviews System
- Star ratings and comments
- Review moderation
- Average rating display

## Database Models

### Core Models
- **User**: Extended Django user model
- **Category**: Hierarchical product categories
- **Product**: Product information and pricing
- **Cart/CartItem**: Shopping cart functionality
- **Order/OrderItem**: Order processing
- **Review**: Product reviews and ratings
- **Wishlist**: User wishlist functionality

## Admin Panel

Access the admin panel at `/admin/` with your superuser credentials.

### Admin Features
- Product management (CRUD operations)
- Category management
- Order management and status updates
- User management
- Review moderation

## API Endpoints

The application provides the following main URLs:

- `/` - Home page
- `/products/` - Product listing with filters
- `/product/<id>/` - Product detail page
- `/category/<slug>/` - Category products
- `/cart/` - Shopping cart
- `/checkout/` - Checkout process
- `/orders/` - User order history
- `/wishlist/` - User wishlist
- `/search/` - Product search
- `/register/` - User registration

## Customization

### Adding New Product Fields
1. Update the `Product` model in `store/models.py`
2. Create and run migrations: `python manage.py makemigrations && python manage.py migrate`
3. Update the admin interface in `store/admin.py`
4. Update templates to display new fields

### Styling Changes
- Modify `store/static/store/css/style.css`
- Update Bootstrap classes in templates
- Add custom JavaScript in `store/static/store/js/main.js`

### Adding New Features
1. Create new models in `store/models.py`
2. Add views in `store/views.py`
3. Create templates in `store/templates/store/`
4. Update URL routing in `store/urls.py`

## Development Tips

### Database Reset
```bash
# Delete database and recreate
rm db.sqlite3
python manage.py migrate
python manage.py populate_data
```

### Static Files
```bash
# Collect static files (if needed)
python manage.py collectstatic
```

### Creating New Products
1. Login as admin
2. Go to `/admin/`
3. Navigate to "Products" section
4. Add new products with images

## Troubleshooting

### Common Issues

1. **Static files not loading**
   - Ensure `DEBUG = True` in settings
   - Check that `STATIC_URL` is set correctly

2. **Images not displaying**
   - Verify `MEDIA_URL` and `MEDIA_ROOT` settings
   - Check file permissions in media directory

3. **Database errors**
   - Run `python manage.py migrate`
   - Check database file permissions

4. **Template errors**
   - Verify template paths in `TEMPLATES` setting
   - Check for syntax errors in HTML templates

## Production Considerations

This application is designed for local development. For production deployment, consider:

- Using PostgreSQL instead of SQLite
- Setting up proper static file serving
- Configuring email backend for notifications
- Adding payment gateway integration
- Implementing proper security measures
- Setting up monitoring and logging

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is for educational purposes. Feel free to use and modify as needed.

## Support

For questions or issues, please check the Django documentation or create an issue in the repository.

---

**Happy Shopping with SumanthCommerce! 🛒**
