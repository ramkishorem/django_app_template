Django App Template
========================

This is the template that I use to start a new django app for development in a windows environment. It makes use of the template argument added to startapp command in 1.4.

* admin, urls files and template, static folders created

* some default imports in admin, url files

* reverse imported in models for get_absolute_url method

To create an app with this template

```
git clone https://github.com/affenity/django-app-template.git
python manage.py startapp --template=django-app-template/template <app_name>
```

