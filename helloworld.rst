Hello World
===========
As is typical with any programming guide or tutorial, a "Hello, World!" example is required. This gives a basic example of creating a graphical window, and displaying some content in it.

.. literalinclude:: _examples/helloworld.py

Download: :download:`PushButton <_examples/helloworld.py>`

=========================
Stepping Through The Code
=========================
The first line is the hashbang (also known as crunchbang, shebang) which declares the Python interpreter version to use.

The import statements on the second and third lines allow us to import additional modules, including Qt.

The class statement defines our window and the type of object it will be, in this case QWidget. The ``QWidget.__init__(self)`` defines that the class is the QWindow object and allows setting of :doc:`window` methods directly on the class.

The ninth line in the example defines the title of the Window, and is displayed on the titlebar if shown by your desktop environment/window manager.

Window object in Qt can only display one object at a time. To allow additional objects to be added, a container is used that can display multiple items. In this case, the :doc:`gridlayout` is used and subsequently assigned to the Window.

On line fourteen, the :doc:`label` is constructed, and the parameter passed is the "Hello, World!" string which will be displayed. Line fifteen is then used to pack the label into the layout, with the ``0, 0`` indicating the position in the grid the top-left corner of the label will be attached.

Once the class has constructed itself, the Application object is constructed.

On line nineteen, the Window class is instantiated and then shown.

The Qt main loop is then executed inside the ``sys.exit`` statement, allowing the Python interpreter to exit when the main loop execution is ended.
