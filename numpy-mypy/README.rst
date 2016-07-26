==========
numpy-mypy
==========

Introduction
------------

This package contains the `MyPy <http://www.mypy-lang.org/>`_ type stubs for the `NumPy <http://www.numpy.org/>`_ scientific package.

So far, only `ndarrays <http://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.html>`_, `scalars <http://docs.scipy.org/doc/numpy/reference/arrays.scalars.html#scalars>`_, and `array creation routines <http://docs.scipy.org/doc/numpy/reference/routines.array-creation.html#array-creation-routines>`_ are covered, but we think it's enough to get you started on type checking programs that depend on ``numpy``.

Usage
-----

We've defined the interface for ``numpy.ndarray`` with a type parameter that allows developers to declare the type of scalars that each cell contains:

.. code-block:: python

    my_array = numpy.ndarray([1,2,3])  # type: numpy.ndarray[int]

Afterwards you can operate with the array as usual. For the moment being, due to some limitations (listed below), you'll have to declare the type of the array explicitly.

In order to run mypy against your numpy based code, you need to download the numpy-mypy stub and put its contents in a folder (we recommend naming the folder ``stubs`` as per mypy's documentation suggestion). Once there, you can check your code setting the ``MYPYPATH`` environment variable: ::

  MYPYPATH=stubs/ mypy my_program.py
  test_numpy.py:8: error: Argument 1 to "do_something" has incompatible type ndarray[float]; expected ndarray[bool]

Limitations
-----------

As we mentioned in the introduction, not all the package has types signatures yet, but we'll keep adding them in subsequent releases.

Quite a few numpy methods are incredibly flexible and they do their best to accommodate to any possible argument combination. Most of these problems are solved behind the scenes and a sensible response is almost always given. Although this is great for users, it caused us a lot of problems when trying to describe the type signature for those methods. In those cases we opted to give the user the chance of being explicit with their intentions. For instance, the ``array`` function is used to create arrays, and its first argument is an arbitrary "array-like" object. You can pass pretty much anything as the ``object`` argument: ::

  In [1]: import numpy as np

  In [2]: np.array('a string')
  Out[2]:
  array('a string',
        dtype='<U8')

  In [3]: np.array(2)
  Out[3]: array(2)

  In [4]: np.array([1,2,3])
  Out[4]: array([1, 2, 3])

  In [5]: np.array((1,2,"3"))
  Out[5]:
  array(['1', '2', '3'],
        dtype='<U21')

As you can see, you give "something" to ``array``, and it manages to build an array out of it. With our signatures, mypy can only guess that these arrays are of type ``ndarray[Any]``. We wrote the signature so you can explicitly state the type of arrays:

.. code-block:: python

  my_array = numpy.array([1.0, 2.0, 3.0])  # type: numpy.array[float]

Most methods signatures were written trying to maintain as much type information as possible.

There are some mypy `issues <https://github.com/python/mypy/issues/1907>`_ that prevent us from writing smarter type signatures. Once those are resolved, we'll be able to expose more type information to mypy which, will make it easier to keep track of the type of scalars stored in the arrays and have stricter checking. For the time being, we designed this to prefer "when in doubt, allow it" rather than "when in doubt, forbid it", so some invalid operations may pass uncaught.

Feedback
--------

We would appreciate any comments, suggestions and bug reports on this package.
