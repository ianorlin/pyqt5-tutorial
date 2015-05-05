Splitter
========
The Splitter is an organiser class widget, which provides a way to insert child items which can then be given varying amounts of space. The amount of space allowed is adjusted by the user using a handle on the Splitter.

The widget is commonly seen in File Managers and Web Browsers where the main content may also need to share space with a sidepanel such as a tree view or bookmark list.

===========
Constructor
===========
The Splitter can be constructed with::

  splitter = QSplitter()

=======
Methods
=======
Child widgets can be added to the Splitter with the methods::

  splitter.addWidget(widget)
  splitter.insertWidget(index, widget)

The *widget* parameter is the name of the child widget to be inserted. The *index* value of the ``.insertWidget()`` method specifies the position to insert the widget at. The ``.addWidget()`` method adds items to the Splitter in the order the code is executed.

By default, the Splitter takes on a horizontal orientation. This can be changed with::

  splitter.setOrientation(orientation)

The *orientation* value should be set to one of the following:

* ``Qt::Horizontal``
* ``Qt::Vertical``

In some cases, it may be useful to retrieve the widget for a given index, or the index for a given widget. This can be done using the methods::

  splitter.widget(index)
  splitter.indexOf(widget)

The number of widgets being held by the Splitter can also be found by::

  splitter.count()

The width of the handle in pixels can be retrieved using::

  splitter.handleWidth(width)

It can also be defined using::

  splitter.setHandleWidth(width)

The *width* parameter again should be specified in pixels.
