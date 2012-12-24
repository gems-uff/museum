museum
======

CBSoft Tools Museum

hints
=====

Use "python manage.py schemamigration tools --auto" after any changes to the model to create migrations.

Use "python manage.py migrate tools" to apply the existing migrations.

development
===========

Use "python manage.py runserver" to run a local server.

production
==========

Remember to create "local_settings.py" with ADMINS, DATABASES, and STATIC_ROOT information.

Use "python manage.py collectstatic" when deploying for the first time into production.