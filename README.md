# Django Takehome

## **Simple Book Service**

Create a book list website in Python using Django. It can be very simple and look plain or be as fancy as you like, however **graphical design is not a grading consideration.** 

Use **best practices**, pay **attention to detail** and write **clean, testable code.** We wish to understand your experience with Python, Django, and general software engineering practices. You can pull in any Python libraries that you need (make sure to include them in the requirements.txt). You should include a simple README in the source directory with instructions and any notes.

**The target time to complete the exercise is 1-3 hours**, but as it is not a “live” exercise there is no time limit and you may spend as much time as you wish. It is better to focus on a few well-functioning pages than to work on many half-working pages. 

When in doubt about implementation specifics, you are free to make your own reasonable project choices based on the details below. **Be ready to discuss design decisions** and ways to extend the project in further interviews.

Please work within the provided Github private repo in a new branch. **Upon completion**, signal to us via opening a new PR from your branch to main. Email a link to the PR to careers@netboxlabs.com

**Details**

- Create a new Django app, use SQLite as the database
- Login for users can be handled by the regular Django admin login
- Screens can be plain HTML or you can use any UI framework that you like
- Try to make the code **DRY** and **keep database calls to a minimum**

**Database**

- Use SQLite.
- Create a books model with a **title**, **description** and **author** (link to the user model)
- Create the model such that users can mark one or more books as their favorites

**Home Page**

- On the home page (open to everyone even if not logged in) show a list of book titles where the title links to a detail page for the book

**Book Detail Page**

- The detail page of the book should show the title, author and description
- Have an **edit button** on the page where staff users can go to change the book information including title, author and description
- Have a **“Favorite” button** that will mark the book as one of the users favorites

**Favorites Page**

- At the top of all pages have a **“Favorites” link** which will go to a page showing the logged-in user all their books that they marked as favorites

**Optional but encouraged**

- Create a REST API endpoint to get a list of the books and book details
