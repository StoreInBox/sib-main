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
