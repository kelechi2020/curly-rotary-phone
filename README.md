# Project Readme:  Book listing Service
## Overview

The Simple Book Service is a Django-based web application designed to provide a platform for users to browse, favorite, and manage books. 

## Key Features

- **Book Listing:** Displays a list of books with titles linking to their detail pages.
- **Book Detail View:** Shows detailed information about a book, including title, author, and description.
- **User Authentication:** Utilizes Django's built-in authentication system for user login.
- **Favorite System:** Allows authenticated users to mark books as favorites and view them on a separate page.
- **REST API:** Includes a RESTful API endpoint for searching book information based on various filter
- **Admin Interface:** Leverages Django's admin capabilities for book management.


A step-by-step series of examples that tell you how to get a development environment running.


1. **Clone the Repository**

    ```bash
    git clone https://github.com/netboxlabs-recruitment/takehome-swe-django-kelechi2020
    cd takehome-swe-django-kelechi2020
    ```


2. **Build and Run with Docker**

    Use Docker Compose to build and run the application:

    ```bash
    docker-compose up --build
    ```

   This command will build the Docker image for this project and start the containers defined in your `docker-compose.yml` file.


3. **Apply migrations**
   
   ```bash
   docker-compose exec web python manage.py migrate
   ```
   
4. **Create root user**
   
   ```bash
   docker-compose exec web python manage.py createsuperuser --email [email] --username [username]
   ```

5. **Create come books**

   ```
   Please visit "http://localhost:8079/addmin", login with superuser and create some books record.
   
   Then visit "/" to view and interact with records
   ```

6. **Running Tests**
   
   ```bash
   
   docker-compose exec web python manage.py test
   ```

7. **Accessing the Application**

    Once the containers are up and running, you can access the application at:

    ```
    http://localhost:8079/
    ```
## API Documentation and playground

 Swagger documentation can be accessed at:
 ```
 http://localhost:8079/api
 ```


## Usage

- **Home Page:** Accessible to all users, showing a list of book titles.
- **Book Detail Page:** Click on a book title to view its details. Staff users can edit book information.
- **Favorites Page:** Logged-in users can view their favorite books.
- **Admin Panel:** Accessible at `/admin` for managing books and users.

## ###  Project Improvement roadmap (Things I would do if I had more time)

1. **User Registration:** Implement a user registration system to allow new users to sign up.
2. **Advanced Book Search:** Add a feature for advanced searching and filtering of books based on different criteria.
3. **User Profiles:** Create user profiles where users can manage their information and view their activity.
4. **Book Ratings and Reviews:** Allow users to rate and review books, and display these on the book detail pages.
5. **Responsive Design:** Enhance the frontend with a responsive design to improve usability on various devices.
6. **Social Media Integration:** Add features for sharing books on social media platforms.
7. **Recommendation Engine:** Implement a recommendation system to suggest books based on user preferences and history.
8. **Internationalization:** Add support for multiple languages to cater to a global audience.
9. **Performance Optimization:** Optimize backend queries and implement caching for improved performance.
10. **Comprehensive Testing:** Expand the test suite to cover more scenarios and edge cases for robustness.







- 