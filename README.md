# Library Project

Library app is like a mini book shelf. It allows you to browse authors and books. Catalog tab directs user to the list of available books, and users can see who the author is for a given book. Users can also navigate to see details of books (book status: on loan, available, out of stock etc.) and authors (biography, date of birth and death). Any user can register and sign in, and once the user is signed in, s/he is authorized to add authors and/or books simply by filling out corresponding forms. Project makes heavy use of Class-Based-Views rather than Function-Based-Views. 



### Requirements

* pip install django
* pip install django_crispy_forms
* pip install Pillow
* Python 3.6+
* Django 2.1+


### Installation

Clone the repo, create virtual environment:

    $ git clone https://github.com/yucehan57/libraryproject.git
    $ virtualenv env
    $ source /env/bin/activate
    
Environment is set up. To proceed, you begin by making necessary migrations:

    $ python manage.py makemigrations
    $ python manage.py migrate
    
And, run the server:

    $ python manage.py runserver
