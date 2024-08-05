# E-Commerce-Website
it is a Django-based e-commerce website with two main applications: `shop` and `blog`. The `shop` app allows users to browse and purchase products, while the `blog` app enables content creation and management for blogging.

## Features

- **Product Management**: Add, update, and delete products.
- **Order Management**: Place and track orders.
- **Search Functionality**: Search for products based on various criteria.
- **Contact Form**: Users can reach out via the contact form.
- **Blog**: Create and manage blog posts.
- **Payment Integration**: Integrate with PayTm for handling payments.

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/xamurani/E-Commerce-Website.git
    cd myawesomecart
    ```

2. **Install the dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

3. **Setup the database**:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

4. **Create a superuser**:

    ```bash
    python manage.py createsuperuser
    ```

5. **Run the development server**:

    ```bash
    python manage.py runserver
    ```

## Project Structure

- `MyAwesomeCart/`
  - `__init__.py`
  - `asgi.py`
  - `settings.py`
  - `urls.py`
  - `views.py`
  - `wsgi.py`
- `shop/`
  - `images/`
  - `migrations/`
  - - `Paytm/`
    - - `Checksum.py`
  - `static/`
  - `templates/shop/`
    - `shop/`
      - `about.html`
      - `basic.html`
      - `index.html`
      - `contact.html`
      - `search.html`
      - `prodView.html`
      - `checkout.html`
      - `tracker.html`
      - `paymentstatus.html`
  - `__init__.py`
  - `admin.py`
  - `apps.py`
  - `models.py`
  - `urls.py`
  - `views.py`
- `blog/`
  - `migrations/`
  - `static/`
  - `templates/blog/`
    - `basic.html`
    - `blogpost.html`
    - `index.html`
  - `__init__.py`
  - `admin.py`
  - `apps.py`
  - `models.py`
  - `tests.py`
  - `urls.py`
  - `views.py`

- `media/`
- `manage.py`
- `db.sqlite3.py`

## Models

### Shop Models

- **Product**: Represents a product with fields like `product_name`, `category`, `sub_category`, `price`, `desc`, `pub_date`, and `image`.
- **Contact**: Stores contact form submissions with fields like `name`, `email`, `phone`, and `desc`.
- **Place_Orders**: Represents an order with fields like `items_json`, `name`, `amount`, `email`, `address`, `city`, `state`, `zip_code`, and `phone`.
- **OrderUpdate**: Represents updates to an order with fields like `order_id`, `update_desc`, and `timestamp`.

### Blog Models

- **Blogpost**: Represents a blog post with fields like `post_id`, `tilte`, `head0`, `chead0`, `head1`, `chead1`, `head2`, `chead2`, `pub_date`, and `thumbnail`.

## Views

### Shop Views

- `index`: Displays the home page with product categories.
- `search`: Handles product search functionality.
- `about`: Displays the about page.
- `contact`: Handles contact form submissions.
- `tracker`: Tracks order status.
- `productView`: Displays a single product view.
- `checkout`: Handles the checkout process.
- `handlerequest`: Handles payment requests and responses.

### Blog Views

- `index`: Displays a list of blog posts.
- `blogpost`: Displays a single blog post.

## URL Configuration

### Project URLs

- `/admin/`: Admin panel.
- `/`: Home page (redirects to shop).
- `/blog/`: Blog application.
- `/shop/`: Shop application.

### Shop URLs

- `/shop/`: Home page.
- `/shop/about/`: About page.
- `/shop/contact/`: Contact page.
- `/shop/tracker/`: Order tracking page.
- `/shop/search/`: Search page.
- `/shop/products/<int:myid>`: Product detail page.
- `/shop/checkout/`: Checkout page.
- `/shop/handlerequest/`: Payment handling page.

### Blog URLs

- `/blog/`: Blog home page.
- `/blog/blogpost/<int:id>`: Blog post detail page.

## Payment Integration

The project integrates with PayTm for handling payments. The `shop/payTm/CheckSum.py` file contains the necessary functions to generate and verify checksums for secure transactions.

## License

Copyright (c) 2024 Muhammad

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
