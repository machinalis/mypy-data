from typing import Any, Generic, Iterator, List, Optional, Sequence, Tuple, TypeVar, Union, io

class dtype: ...
_dtype_alias = dtype


class flagsobj:
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
    def __getitem__(self, item: str) -> bool: ...


# TODO Complete scalar hierarchy
class generic: ...
class bool_(generic): ...
class object_(generic): ...
class number(generic): ...
class flexible(generic): ...

AxesType = Union[int, Tuple[int, ...]]

S = TypeVar('S')
U = TypeVar('U')
NdarrayLike = TypeVar('NdarrayLike', bound='ndarray')

class ndarray(Generic[S]):
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

    def all(self, axis: Optional[AxesType]=None, out: Optional['ndarray[U]]']=None,
            keepdims: Optional[bool]=None) -> Union['ndarray[U]', 'ndarray[bool]', bool]: ...

    def any(self, axis: Optional[AxesType]=None, out: Optional['ndarray']=None,
            keepdims: Optional[bool]=None) -> Union['ndarray', bool]: ...

    def argmax(self, axis: Optional[int]=None,
               out: Optional['ndarray[U]']=None) -> Union['ndarray[int]', 'ndarray[U]', int]: ...

    def argmin(self, axis: Optional[int]=None,
               out: Optional['ndarray[U]']=None) -> Union['ndarray[int]', 'ndarray[U]', int]: ...

    def argpartition(self, kth: Union[int, Sequence[int]], axis: Optional[int]=-1,
                     kind: Optional[str]='introselect',
                     order: Optional[str, List[str]]=None) -> 'ndarray[int]': ...

    def argsort(self, axis: Optional[int]=None, kind: Optional[str]='quicksort',
                order: Optional[str, List[str]]=None) -> 'ndarray[int]': ...

    def astype(self, dtype: Union[str, _dtype_alias], order: Optional[str]='K',
               casting: Optional[str]='unsafe', subok: Optional[bool]=None,
               copy: Optional[bool]=None) -> 'ndarray[Any]': ...  # TODO not entirely sure how to express the relation between dtype and return value

    def byteswap(self, inplace: Optional[bool]=False) -> 'ndarray[S]': ...

    def choose(self, choices:Sequence['ndarray[Any]'], out: Optional['ndarray[U]']=None,  # TODO verify if choices can be anything other than 'ndarray'
               mode: Optional['str']='raise') -> 'ndarray[U]': ...

    def clip(self, a_min: Union[generic, 'ndarray[Any]'], a_max: Union[generic, 'ndarray[Any]'],
             out: Optional['ndarray[U]']=None) -> Union['ndarray[S]', 'ndarray[U]']: ...  # TODO don't know what to do with a_min and a_max

    def compress(self, condition: [Sequence[bool], 'ndarray[bool]'], axis: Optional[int]=None,
                 out: Optional['ndarray']=None) -> 'ndarray': ...

    def conj(self) -> 'ndarray[S]': ...  # TODO there are no docs. verify interface and semantics.

    def conjugate(self) -> 'ndarray[S]': ...  # TODO there are no docs. verify interface and semantics.

    def copy(self, order: Optional['str']='C') -> 'ndarray[S]': ...

    def cumprod(self, axis: Optional[int]=None, dtype: Optional[_dtype_alias]=None,
                out: Optional['ndarray[Any]']=None) -> 'ndarray[Any]': ...  # TODO figure out a way to express relationship between dtype and return value

    def cumsum(self, axis: Optional[int]=None, dtype: Optional[_dtype_alias]=None,
                out: Optional['ndarray[ANY]']=None) -> 'ndarray[Any]': ...  # TODO figure out a way to express relationship between dtype and return value

    def diagonal(self, offset: Optional[int]=0, axis1: Optional[int]=0,
                 axis2: Optional[int]=1) -> 'ndarray[S]': ...

    def dot(self, b: 'ndarray[S]',
            out: Optional['ndarray[U]']=None) -> Union['ndarray[S]', 'ndarray[U]']: ...

    def dump(self, file: 'str') -> None: ...

    def dumps(self) -> 'str': ...  # TODO documentation is incomplete. validate signature.

    def fill(self, value: generic) -> None: ...

    def flatten(self, order: Optional[str]='C') -> 'ndarray[S]': ...

    def getfield(self, dtype: _dtype_alias, offset: Optional[int]=0) -> 'ndarray[_dtype_alias]': ...  # TODO documentation is incomplete. validate signature.

    def item(self, args: Optional[Union[int, Tuple[int, ...]]]) -> generic: ...  # TODO verify this signature

    def itemset(self, arg0: Union[int, Tuple[int, ...]], arg1: Optional[generic]=None) -> None: ...  # TODO verify this signature

    def max(self, axis: Optional[Union[int, Tuple[int, ...]]]=None,
            out: Optional['ndarray[U]]']=None) -> Union['ndarray[S]', 'ndarray[U]', generic]: ...

    def mean(self, axis: Optional[Union[int, Tuple[int, ...]]]=None,
             dtype: Optional[_dtype_alias]=None, out=Optional['ndarray[U]'],
             keepdims: Optional[bool]=False) -> Union['ndarray[U]', 'ndarray[_dtype_alias]', 'ndarray[S]']: ...

    def min(self, axis: Optional[Union[int, Tuple[int, ...]]]=None,
            out: Optional['ndarray[U]]']=None) -> Union['ndarray[S]', 'ndarray[U]', generic]: ...

    def newbyteorder(self, new_order: Optional['str']='S') -> 'ndarray[Any]': ...  # TODO verify the return value type changes

    def nonzero(self) -> 'ndarray[int]': ...

    def partition(self, kth: AxesType, axis: Optional[int]=-1, kind: Optional[str]='introselect',
                  order: Optional[Union[Sequence[str], str]]=None) -> None: ...

    def prod(self, axis: Optional[AxesType]=None, dtype: Optional[_dtype_alias]=None,
             out: Optional['ndarray[U]]']=None, keepdims: Optional[bool]=False) -> Union['ndarray[S]', 'ndarray[U]', 'ndarray[_dtype_alias]']: ...

    def ptp(self, axis: Optional[int]=None,
            out: Optional['ndarray[U]']=None) -> Union['ndarray[S]', 'ndarray[U]']: ...

    def put(self, ind: Any, v: Any, mode: Optional[str]='raise') -> None: ...  # TODO figure out a way to express "array-like" ind and v

    def ravel(self, order: Optional[str]='C') -> 'ndarray[S]': ...  # TODO verify return value

    def repeat(self, repeats: Union[int, Sequence[int]],
               axis: Optional[int]=None) -> 'ndarray[S]': ...

    def reshape(self, newshape: Union[int, Tuple[int]],
                order: Optional[str]='C') -> 'ndarray[S]': ...

    def resize(self, new_shape: Union[int, Tuple[int]], refcheck: Optional[bool]=True) -> None: ...

    def round(self, decimals: int=0,
              out: Optional['ndarray[U]']=None) -> Union['ndarray[S]', 'ndarray[U]']: ...

    def searchsorted(self, v: Any, side: Optional[str]='left',
                     sorter: Optional[Any]=None) -> 'ndarray[int]': ...  # TODO find a way to describe v and sorter

    def setfield(self, val: Any, dtype: _dtype_alias, offset: Optional[int]=0) -> None: ...

    def setflags(self, write: Optional[bool]=None, align: Optional[bool]=None,
                 uic: Optional[bool]=None) -> None: ...

    def sort(self, axis: Optional[int]=-1, kind: Optional[str]='quicksort',
             order: Optional[Union[str, Sequence[str]]]=None) -> None: ...

    def squeeze(self, axis: Optional[AxesType]) -> 'ndarray[S]': ...

    def std(self, axis: Optional[AxesType]=None, dtype=Optional[_dtype_alias],
            out=Optional['ndarray[U]'], ddof: Optional[int]=0,
            keepdims: Optional[bool]=False) -> Union['ndarray[U]', 'ndarray[_dtype_alias]', 'ndarray[S]']: ...

    def sum(self, axis: Optional[AxesType]=None, dtype=Optional[_dtype_alias],
            out: Optional['ndarray[U]']=None, keepdims: Optional[bool]=False) -> Union['ndarray[U]', 'ndarray[_dtype_alias]', 'ndarray[S]']: ...

    def swapaxes(self, axis1: int, axis2: int) -> 'ndarray[S]': ...

    def take(self, indices: Any, axis: Optional[int]=None, out: Optional['ndarray[U]']=None,
             mode: Optional[str]='raise') -> Union['ndarray[U]', 'ndarray[S]']: ...

    def tobytes(self, order: Optional[str]='C') -> bytes: ...

    def tofile(self, fid: Union[io.BinaryIO, str], sep: Optional[str]="",
               format: Optional[str]="%s") -> None: ...

    def tolist(self) -> List[Any]: ...

    def tostring(self, order: Optional[str]='C') -> bytes: ...

    def trace(self, offset: Optional[int]=0, axis1: Optional[int]=0, axis2: Optional[int]=1,
              dtype=Optional[_dtype_alias], out=Optional['ndarray[U]']) -> Union['ndarray[U]', 'ndarray[_dtype_alias]', 'ndarray[S]']: ...  # TODO define trace

    def transpose(self, args0: Optional[Union[int, Tuple[int]]], *args: int) -> 'ndarray[S]': ...

    def var(self, axis: Optional[AxesType]=None, dtype=Optional[_dtype_alias],
            out=Optional['ndarray[U]'], ddof: Optional[int]=0,
            keepdims: Optional[bool]=False) -> Union['ndarray[U]', 'ndarray[_dtype_alias]', 'ndarray[S]']: ...

    def view(self, dtype=Optional[Union[_dtype_alias, NdarrayLike]],
             type: Optional[U]=None) -> Union['ndarray[_dtype_alias]', NdarrayLike, 'ndarray[U]']: ...
