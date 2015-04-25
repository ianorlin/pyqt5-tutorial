TabWidget
=========
The TabWidget provides a container with multiple pages which are 
switchable via tabs. Each page can contain a widget or other containers.

===========
Constructor
===========
The TabWidget is constructed using::

  tabwidget = QTabWidget()

=======
Methods
=======
Tabs are added to the TabWidget via several methods::

  tabwidget.addTab(child, label)
  tabwidget.insertTab(index, child, label)

The ``.addTab()`` method adds each tab in the order the code is executed 
whereas the ``.insertTab()`` method allows an *index* value indicating 
the location to insert the tab, with the first position identified as 
``0``. The *child* parameter is the name of the child object to be added 
to the tab. Finally, the *label* parameter is the text to be displayed 
on the tab itself.

Tabs are removed from the TabWidget via::

  tabWidget.removeTab(index)

The *index* value is the position of the tab within the TabWidget.

All the tabs currently held by the TabWidget can be removed with::

  tabWidget.clear()

The number of tabs contained can be counted using::

  count = tabWidget.count()

If the TabWidget contains less than two tabs, the tab bar can be 
configured to hide::

  tabWidget.tabBarAutoHide(hide)

When *hide* is set to ``True``, the tab bar will be hidden.

In some cases, individual tabs should be removable. A close button can 
be added to each tab using::

  tabWidget.setTabsClosable(closable)

=======
Example
=======
Below is an example of an TabWidget:

.. literalinclude:: _examples/tabwidget.py

Download: :download:`TabWidget <_examples/tabwidget.py>`
