Installation
============

1. Clone project from git:

    .. code-block:: bash

    $ git clone git@github.com:StoreInBox/sib-main.git

    $ cd sib-main

2. Install project (recommended to use virtual environment):

    .. code-block:: bash

    $ python setup.py develop -U

3. Create custom settings for project and configure them if needed:

    .. code-block:: bash

    $ cp main/server/settings/custom.py.example main/server/settings/custom.py

4. Migrate database:

    .. code-block:: bash

    $ python manage.py migrate

5. Create test data:

    .. code-block:: bash

    $ python manage.py createtestdata

6. Start server:

    .. code-block:: bash

    $ python manage.py runserver


Update project
==============

Project is in active development phase so there is no migrations for applications.
Please recreate database after each update. Follow next steps

1. Pull latest project version

    .. code-block:: bash

    $ git pull origin master

2. Update dependencies:

    .. code-block:: bash

    $ python setup.py develop -U

3. Remove project database

    .. code-block:: bash

    $ rm db.sqlite3

4. Migrate tables

    .. code-block:: bash

    $ python manage.py migrate

5. Create test data

    .. code-block:: bash

    $ python manage.py createtestdata
