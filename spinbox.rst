SpinBox
=======
The SpinBox widget provides a way to enter numbers. Thw widget provides integrated adjustment buttons which allow the user to adjust the number by clicking the arrows, while also allowing adjustment by typing into a text entry.

===========
Constructor
===========
The SpinBox is constructed with the call::

  spinbox = QSpinBox()

=======
Methods
=======
Minimum and maximum values are defined for the SpinBox using::

  spinbox.minimum(value)
  spinbox.maximum(value)

Setting a value on the SpinBox is done using::

  spinbox.value(value)

If the *value* paramter is out of the minimum and maximum boundaries, the value will be adjusted so that it fits between the minimum and maximum.

A prefix and suffix can be displayed within the SpinBox::

  spinbox.setPrefix(suffix)
  spinbox.setSuffix(suffix)

The *prefix* and *suffix* parameters should be set to a string. It is useful when displaying a unit associated with the value (e.g. "mph", "cm").

By default, the adjustment arrows change the displayed value by 1. The step can be changed with::

  spinbox.setSingleStep(value)
