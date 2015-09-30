Frontend installation
=====================

1. Install grunt and bower:

    .. code-block:: bash

    $ sudo npm install

2. Install grunt packages:

    .. code-block:: bash

    $ grunt build

3. For assets files hot reload run:

    .. code-block:: bash

    $ grunt watch


Frontend folders destination
============================

1. **assets** - source of js and css.
2. **static** - compiled assets (this folder is ignored by git).
3. **templates** - final version of templates.
4. **templates-examples** - auto-documented examples of template files. Example template will displayed only if same
   file in templates folder does not exist.


Useful for development links
============================

1. Django templates:
  - Templates: https://docs.djangoproject.com/en/1.8/ref/templates/language/
  - Standard tags and filters: https://docs.djangoproject.com/en/1.8/ref/templates/builtins/
  - Templates from outside(mostly for backend developers): https://docs.djangoproject.com/en/1.8/ref/templates/api/