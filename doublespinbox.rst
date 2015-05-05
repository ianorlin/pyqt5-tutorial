DoubleSpinBox
=============
A DoubleSpinBox is much like a regular :doc:`spinbox`, however it is used to handle double type numbers.

===========
Constructor
===========
The DoubleSpinBox is constructed with the call::

  doublespinbox = QDoubleSpinBox()

=======
Methods
=======
Minimum and maximum values are defined for the DoubleSpinBox using::

  doublespinbox.minimum(value)
  doublespinbox.maximum(value)

Setting a value on the DoubleSpinBox is done using::

  doublespinbox.value(value)

If the *value* paramter is out of the minimum and maximum boundaries, the value will be adjusted so that it fits between the minimum and maximum.

A prefix and suffix can be displayed within the DoubleSpinBox::

  doublespinbox.setPrefix(suffix)
  doublespinbox.setSuffix(suffix)

The *prefix* and *suffix* parameters should be set to a string. It is useful when displaying a unit associated with the value (e.g. "mph", "cm").

By default, the adjustment arrows change the displayed value by 1. The step can be changed with::

  doublespinbox.setSingleStep(value)
