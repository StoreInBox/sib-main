Product list page
=================

URL details
^^^^^^^^^^^

* URL itself: **^(?P<category_id>[\d+])/(?P<category_slug>[-\w]+)/$**
* URL name: **products**


Template names
^^^^^^^^^^^^^^

* products/product_list.html
* products/product_list_ajax.html

Template variables
^^^^^^^^^^^^^^^^^^

* product_list - list of products_


.. rubric:: Objects description

.. _products:
.. autoclass:: products.models.Product
   :members:
