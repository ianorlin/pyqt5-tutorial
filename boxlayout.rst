BoxLayout
=========
The BoxLayout is similar to the :doc:`gridlayout`, however it only supports a single row or column of widgets depending on the orientation. It does however dynamically size to the number of widgets it is to contain.

===========
Constructor
===========
The constructor for the BoxLayout is::

  boxlayout = QBoxLayout()

=======
Methods
=======
Widgets are inserted into the BoxLayout with the methods::

  boxlayout.addWidget(widget, stretch, alignment)
  boxlayout.insertWidget(index, widget, stretch, alignment)

An *index* value in the ``.insertWidget`` method indicates the location at which the child widget should be placed. The *widget* parameter is the child widget which is to be added to the BoxLayout. The *stretch* value should be set to an integer indicating the factor at which the child widget stretches to fill the space. Finally, the *alignment* value can be set to one of the following:

* ``Qt::AlignmentLeft``
* ``Qt::AlignmentRight``
* ``Qt::AlignmentHCenter``
* ``Qt::AlignmentJustify``

Layout objects are added to the BoxLayout via alternative methods::

  boxlayout.addLayout(layout, stretch)
  boxlayout.insertLayout(index, layout, stretch)

The pixel spacing between each child widget defaults to zero, however this is configurable with::

  boxlayout.setSpacing(spacing)

Spacing can be added as with a normal widget by::

  boxlayout.addSpacing(spacing)
  boxlayout.insertSpacing(index, spacing)

The *spacing* value indicates the number of pixels spacing to be displayed. The ``.insertSpacing()`` method also takes an *index* indicating the location at which the spacing should be inserted.

The direction of the BoxLayout is settable with the method::

  boxlayout.setDirection(direction)

The *direction* parameter should be set to one of the following:

* ``QBoxLayout::LeftToRight``
* ``QBoxLayout::RightToLeft``
* ``QBoxLayout::TopToBottom``
* ``QBoxLayout::BottomToTop``

