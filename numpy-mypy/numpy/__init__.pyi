from typing import Any, Dict, Iterator, List, Optional, Sequence, Tuple, Union

class dtype: ...
_dtype_alias = dtype


class flagsobj(Dict[str, bool]):
    aligned = None       # type: bool
    behaved = None       # type: bool
    c_contiguous = None  # type: bool
    carray = None        # type: bool
    contiguous = None    # type: bool
    f_contiguous = None  # type: bool
    farray = None        # type: bool
    fnc = None           # type: bool
    forc = None          # type: bool
    fortran = None       # type: bool
    owndata = None       # type: bool
    updateifcopy = None  # type: bool
    writeable = None     # type: bool


# TODO Complete scalar hierarchy
class generic: ...
class bool_(generic): ...
class object_(generic): ...
class number(generic): ...
class flexible(generic): ...

class ndarray:
    T = None         # type: ndarray
    data = None      # type: Any
    dtype = None     # type: _dtype_alias
    flags = None     # type: flagsobj
    flat = None      # type: Iterator[Any]  # TODO Find out if there's a way to restrict the type argument
    imag = None      # type: ndarray
    real = None      # type: ndarray
    size = None      # type: int
    itemsize = None  # type: int
    nbytes = None    # type: int
    ndim = None      # type: int
    shape = None     # type: Tuple[int, ...]
    strides = None   # type: Tuple[int, ...]
    ctypes = None    # type: Any  # TODO Implement ctypes type hint
    base = None      # type: Optional[ndarray]

    # TODO Need to find a way to restrict buffer type
    def __init__(self, shape: Tuple[int, ...], dtype: Optional[Any]=None,
                 buffer: Optional[Any]=None, offset: Optional[int]=None,
                 strides: Optional[Tuple[int, ...]]=None, order: Optional[str]=None) -> None: ...

    def __abs__(self, *args: Any, **kwargs: Any) -> Any: ...  # TODO define __abs__
    def __add__(self, *args: Any, **kwargs: Any) -> Any: ...  # TODO define __add__
    def __and__(self, *args: Any, **kwargs: Any) -> Any: ...  # TODO define __and__
    def __bool__(self, *args: Any, **kwargs: Any) -> Any: ...  # TODO define __bool__
    def __complex__(self, *args: Any, **kwargs: Any) -> Any: ...  # TODO define __complex__
    def __contains__(self, *args: Any, **kwargs: Any) -> Any: ...  # TODO define __contains__
    def __copy__(self, *args: Any, **kwargs: Any) -> Any: ...  # TODO define __copy__
    def __deepcopy__(self, *args: Any, **kwargs: Any) -> Any: ...  # TODO define __deepcopy__
    def __delattr__(self, *args: Any, **kwargs: Any) -> Any: ...  # TODO define __delattr__
    def __delitem__(self, *args: Any, **kwargs: Any) -> Any: ...  # TODO define __delitem__
    def __dir__(self, *args: Any, **kwargs: Any) -> Any: ...  # TODO define __dir__
    def __divmod__(self, *args: Any, **kwargs: Any) -> Any: ...  # TODO define __divmod__
    def __eq__(self, *args: Any, **kwargs: Any) -> Any: ...  # TODO define __eq__
    def __float__(self, *args: Any, **kwargs: Any) -> Any: ...  # TODO define __float__
    def __floordiv__(self, *args: Any, **kwargs: Any) -> Any: ...  # TODO define __floordiv__
    def __format__(self, *args: Any, **kwargs: Any) -> Any: ...  # TODO define __format__
    def __ge__(self, *args: Any, **kwargs: Any) -> Any: ...  # TODO define __ge__
    def __getattribute__(self, *args: Any, **kwargs: Any) -> Any: ...  # TODO define __getattribute__
    def __getitem__(self, *args: Any, **kwargs: Any) -> Any: ...  # TODO define __getitem__
    def __gt__(self, *args: Any, **kwargs: Any) -> Any: ...  # TODO define __gt__
    def __iadd__(self, *args: Any, **kwargs: Any) -> Any: ...  # TODO define __iadd__
    def __iand__(self, *args: Any, **kwargs: Any) -> Any: ...  # TODO define __iand__
    def __ifloordiv__(self, *args: Any, **kwargs: Any) -> Any: ...  # TODO define __ifloordiv__
    def __ilshift__(self, *args: Any, **kwargs: Any) -> Any: ...  # TODO define __ilshift__
    def __imatmul__(self, *args: Any, **kwargs: Any) -> Any: ...  # TODO define __imatmul__
    def __imod__(self, *args: Any, **kwargs: Any) -> Any: ...  # TODO define __imod__
    def __imul__(self, *args: Any, **kwargs: Any) -> Any: ...  # TODO define __imul__
    def __index__(self, *args: Any, **kwargs: Any) -> Any: ...  # TODO define __index__
    def __int__(self, *args: Any, **kwargs: Any) -> Any: ...  # TODO define __int__
    def __invert__(self, *args: Any, **kwargs: Any) -> Any: ...  # TODO define __invert__
    def __ior__(self, *args: Any, **kwargs: Any) -> Any: ...  # TODO define __ior__
    def __ipow__(self, *args: Any, **kwargs: Any) -> Any: ...  # TODO define __ipow__
    def __irshift__(self, *args: Any, **kwargs: Any) -> Any: ...  # TODO define __irshift__
    def __isub__(self, *args: Any, **kwargs: Any) -> Any: ...  # TODO define __isub__
    def __iter__(self, *args: Any, **kwargs: Any) -> Any: ...  # TODO define __iter__
    def __itruediv__(self, *args: Any, **kwargs: Any) -> Any: ...  # TODO define __itruediv__
    def __ixor__(self, *args: Any, **kwargs: Any) -> Any: ...  # TODO define __ixor__
    def __le__(self, *args: Any, **kwargs: Any) -> Any: ...  # TODO define __le__
    def __len__(self, *args: Any, **kwargs: Any) -> Any: ...  # TODO define __len__
    def __lshift__(self, *args: Any, **kwargs: Any) -> Any: ...  # TODO define __lshift__
    def __lt__(self, *args: Any, **kwargs: Any) -> Any: ...  # TODO define __lt__
    def __matmul__(self, *args: Any, **kwargs: Any) -> Any: ...  # TODO define __matmul__
    def __mod__(self, *args: Any, **kwargs: Any) -> Any: ...  # TODO define __mod__
    def __mul__(self, *args: Any, **kwargs: Any) -> Any: ...  # TODO define __mul__
    def __ne__(self, *args: Any, **kwargs: Any) -> Any: ...  # TODO define __ne__
    def __neg__(self, *args: Any, **kwargs: Any) -> Any: ...  # TODO define __neg__
    def __new__(self, *args: Any, **kwargs: Any) -> Any: ...  # TODO define __new__
    def __or__(self, *args: Any, **kwargs: Any) -> Any: ...  # TODO define __or__
    def __pos__(self, *args: Any, **kwargs: Any) -> Any: ...  # TODO define __pos__
    def __pow__(self, *args: Any, **kwargs: Any) -> Any: ...  # TODO define __pow__
    def __radd__(self, *args: Any, **kwargs: Any) -> Any: ...  # TODO define __radd__
    def __rand__(self, *args: Any, **kwargs: Any) -> Any: ...  # TODO define __rand__
    def __rdivmod__(self, *args: Any, **kwargs: Any) -> Any: ...  # TODO define __rdivmod__
    def __reduce__(self, *args: Any, **kwargs: Any) -> Any: ...  # TODO define __reduce__
    def __reduce_ex__(self, *args: Any, **kwargs: Any) -> Any: ...  # TODO define __reduce_ex__
    def __repr__(self, *args: Any, **kwargs: Any) -> Any: ...  # TODO define __repr__
    def __rfloordiv__(self, *args: Any, **kwargs: Any) -> Any: ...  # TODO define __rfloordiv__
    def __rlshift__(self, *args: Any, **kwargs: Any) -> Any: ...  # TODO define __rlshift__
    def __rmatmul__(self, *args: Any, **kwargs: Any) -> Any: ...  # TODO define __rmatmul__
    def __rmod__(self, *args: Any, **kwargs: Any) -> Any: ...  # TODO define __rmod__
    def __rmul__(self, *args: Any, **kwargs: Any) -> Any: ...  # TODO define __rmul__
    def __ror__(self, *args: Any, **kwargs: Any) -> Any: ...  # TODO define __ror__
    def __rpow__(self, *args: Any, **kwargs: Any) -> Any: ...  # TODO define __rpow__
    def __rrshift__(self, *args: Any, **kwargs: Any) -> Any: ...  # TODO define __rrshift__
    def __rshift__(self, *args: Any, **kwargs: Any) -> Any: ...  # TODO define __rshift__
    def __rsub__(self, *args: Any, **kwargs: Any) -> Any: ...  # TODO define __rsub__
    def __rtruediv__(self, *args: Any, **kwargs: Any) -> Any: ...  # TODO define __rtruediv__
    def __rxor__(self, *args: Any, **kwargs: Any) -> Any: ...  # TODO define __rxor__
    def __setattr__(self, *args: Any, **kwargs: Any) -> Any: ...  # TODO define __setattr__
    def __setitem__(self, *args: Any, **kwargs: Any) -> Any: ...  # TODO define __setitem__
    def __setstate__(self, *args: Any, **kwargs: Any) -> Any: ...  # TODO define __setstate__
    def __sizeof__(self, *args: Any, **kwargs: Any) -> Any: ...  # TODO define __sizeof__
    def __str__(self, *args: Any, **kwargs: Any) -> Any: ...  # TODO define __str__
    def __sub__(self, *args: Any, **kwargs: Any) -> Any: ...  # TODO define __sub__
    def __subclasshook__(self, *args: Any, **kwargs: Any) -> Any: ...  # TODO define __subclasshook__
    def __truediv__(self, *args: Any, **kwargs: Any) -> Any: ...  # TODO define __truediv__
    def __xor__(self, *args: Any, **kwargs: Any) -> Any: ...  # TODO define __xor__

    def all(self, axis: Optional[Union[int, Tuple[int, ...]]]=None, out: Optional['ndarray']=None,
            keepdims: Optional[bool]=None) -> Union['ndarray', bool]: ...

    def any(self, axis: Optional[Union[int, Tuple[int, ...]]]=None, out: Optional['ndarray']=None,
            keepdims: Optional[bool]=None) -> Union['ndarray', bool]: ...

    def argmax(self, axis: Optional[int]=None, out: Optional['ndarray']=None) -> 'ndarray': ...

    def argmin(self, axis: Optional[int]=None, out: Optional['ndarray']=None) -> 'ndarray': ...

    def argpartition(self, kth: Union[int, Sequence[int]], axis: Optional[int]=-1,
                     kind: Optional[str]='introselect',
                     order: Optional[str, List[str]]=None) -> Union['ndarray', int]: ...

    def argsort(self, axis: Optional[int]=None, kind: Optional[str]='quicksort',
                order: Optional[str, List[str]]=None) -> Union['ndarray', int]: ...

    def astype(self, dtype: Union[str, _dtype_alias], order: Optional[str]='K',
               casting: Optional[str]='unsafe', subok: Optional[bool]=None,
               copy: Optional[bool]=None) -> 'ndarray': ...

    def byteswap(self, inplace: Optional[bool]=False) -> 'ndarray': ...

    def choose(self, choices:Sequence['ndarray'], out: Optional['ndarray']=None,  # TODO verify if choices can be anything other than 'ndarray'
               mode: Optional['str']='raise') -> 'ndarray': ...

    def clip(self, a_min: Union[generic, 'ndarray'], a_max: Union[generic, 'ndarray'],
             out: Optional['ndarray']=None) -> 'ndarray': ...

    def compress(self, condition: Any, axis: Optional[int]=None,  # TODO figure out a way to express condition
                 out: Optional['ndarray']=None) -> 'ndarray': ...

    def conj(self) -> 'ndarray': ...  # TODO there are no docs. verify interface and semantics.

    def conjugate(self) -> 'ndarray': ...  # TODO there are no docs. verify interface and semantics.

    def copy(self, order: Optional['str']='C') -> 'ndarray': ...

    def cumprod(self, axis: Optional[int]=None, dtype: Optional[_dtype_alias]=None,
                out: Optional['ndarray']=None) -> 'ndarray': ...

    def cumsum(self, axis: Optional[int]=None, dtype: Optional[_dtype_alias]=None,
                out: Optional['ndarray']=None) -> 'ndarray': ...

    def diagonal(self, offset: Optional[int]=0, axis1: Optional[int]=0,
                 axis2: Optional[int]=1) -> 'ndarray': ...

    def dot(self, b: 'ndarray', out: Optional['ndarray']=None) -> 'ndarray': ...

    def dump(self, file: 'str') -> None: ...

    def dumps(self) -> 'str': ...  # TODO documentation is incomplete. validate signature.

    def fill(self, value: generic) -> None: ...

    def flatten(self, order: Optional[str]='C') -> 'ndarray': ...

    def getfield(self, dtype: _dtype_alias, offset: Optional[int]=0) -> 'ndarray': ...  # TODO documentation is incomplete. validate signature.

    def item(self, args: Optional[Union[int, Tuple[int, ...]]]) -> Any: ...  # TODO verify this signature

    def itemset(self, arg0: Union[int, Tuple[int, ...]], arg1: Optional[generic]=None) -> None: ...  # TODO verify this signature

    def max(self, axis: Optional[Union[int, Tuple[int, ...]]]=None,
            out: Optional['ndarray']=None) -> Union['ndarray', generic]: ...

    def mean(self, axis: Optional[Union[int, Tuple[int, ...]]]=None,
             dtype: Optional[_dtype_alias]=None, out=Optional['ndarray'],
             keepdims: Optional[bool]=False) -> 'ndarray': ...

    def min(self, axis: Optional[Union[int, Tuple[int, ...]]]=None,
            out: Optional['ndarray']=None) -> Union['ndarray', generic]: ...

    def newbyteorder(self, new_order: Optional['str']='S') -> 'ndarray': ...

    def nonzero(self, *args: Any, **kwargs: Any) -> Any: ...  # TODO define nonzero
    def partition(self, *args: Any, **kwargs: Any) -> Any: ...  # TODO define partition
    def prod(self, *args: Any, **kwargs: Any) -> Any: ...  # TODO define prod
    def ptp(self, *args: Any, **kwargs: Any) -> Any: ...  # TODO define ptp
    def put(self, *args: Any, **kwargs: Any) -> Any: ...  # TODO define put
    def ravel(self, *args: Any, **kwargs: Any) -> Any: ...  # TODO define ravel
    def repeat(self, *args: Any, **kwargs: Any) -> Any: ...  # TODO define repeat
    def reshape(self, *args: Any, **kwargs: Any) -> Any: ...  # TODO define reshape
    def resize(self, *args: Any, **kwargs: Any) -> Any: ...  # TODO define resize
    def round(self, *args: Any, **kwargs: Any) -> Any: ...  # TODO define round
    def searchsorted(self, *args: Any, **kwargs: Any) -> Any: ...  # TODO define searchsorted
    def setfield(self, *args: Any, **kwargs: Any) -> Any: ...  # TODO define setfield
    def setflags(self, *args: Any, **kwargs: Any) -> Any: ...  # TODO define setflags
    def sort(self, *args: Any, **kwargs: Any) -> Any: ...  # TODO define sort
    def squeeze(self, *args: Any, **kwargs: Any) -> Any: ...  # TODO define squeeze
    def std(self, *args: Any, **kwargs: Any) -> Any: ...  # TODO define std
    def sum(self, *args: Any, **kwargs: Any) -> Any: ...  # TODO define sum
    def swapaxes(self, *args: Any, **kwargs: Any) -> Any: ...  # TODO define swapaxes
    def take(self, *args: Any, **kwargs: Any) -> Any: ...  # TODO define take
    def tobytes(self, *args: Any, **kwargs: Any) -> Any: ...  # TODO define tobytes
    def tofile(self, *args: Any, **kwargs: Any) -> Any: ...  # TODO define tofile
    def tolist(self, *args: Any, **kwargs: Any) -> Any: ...  # TODO define tolist
    def tostring(self, *args: Any, **kwargs: Any) -> Any: ...  # TODO define tostring
    def trace(self, *args: Any, **kwargs: Any) -> Any: ...  # TODO define trace
    def transpose(self, *args: Any, **kwargs: Any) -> Any: ...  # TODO define transpose
    def var(self, *args: Any, **kwargs: Any) -> Any: ...  # TODO define var
    def view(self, *args: Any, **kwargs: Any) -> Any: ...  # TODO define view
