
/* Unsigned integer object implementation */

#include "Python.h"
#include <ctype.h>

#define UNSIGNED_MAX 4294967296

long
PyUnsignedInt_GetMax(void)
{
	return UNSIGNED_MAX;	/* To initialize sys.maxunsigned */
}

/* Standard Booleans */

PyUnsignedIntObject _Py_ZeroStruct = {
	PyObject_HEAD_INIT(&PyUnsignedInt_Type)
	0
};

PyUnsignedIntObject _Py_TrueStruct = {
	PyObject_HEAD_INIT(&PyUnsignedInt_Type)
	1
};

/* Return 1 if exception raised, 0 if caller should retry using longs */
static int
err_ovf(char *msg)
{
	if (PyErr_Warn(PyExc_OverflowWarning, msg) < 0) {
		if (PyErr_ExceptionMatches(PyExc_OverflowWarning))
			PyErr_SetString(PyExc_OverflowError, msg);
		return 1;
	}
	else
		return 0;
}

/* Integers are quite normal objects, to make object handling uniform.
   (Using odd pointers to represent integers would save much space
   but require extra checks for this special case throughout the code.)
   Since, a typical Python program spends much of its time allocating
   and deallocating integers, these operations should be very fast.
   Therefore we use a dedicated allocation scheme with a much lower
   overhead (in space and time) than straight malloc(): a simple
   dedicated free list, filled when necessary with memory from malloc().
*/

#define BLOCK_SIZE	1000	/* 1K less typical malloc overhead */
#define BHEAD_SIZE	8	/* Enough for a 64-bit pointer */
#define N_INTOBJECTS	((BLOCK_SIZE - BHEAD_SIZE) / sizeof(PyUnsignedIntObject))

struct _intblock {
	struct _intblock *next;
	PyUnsignedIntObject objects[N_INTOBJECTS];
};

typedef struct _intblock PyUnsignedIntBlock;

static PyUnsignedIntBlock *block_list = NULL;
static PyUnsignedIntObject *free_list = NULL;

static PyUnsignedIntObject *
fill_free_list(void)
{
	PyUnsignedIntObject *p, *q;
	/* XXX Int blocks escape the object heap. Use PyObject_MALLOC ??? */
	p = (PyUnsignedIntObject *) PyMem_MALLOC(sizeof(PyUnsignedIntBlock));
	if (p == NULL)
		return (PyUnsignedIntObject *) PyErr_NoMemory();
	((PyUnsignedIntBlock *)p)->next = block_list;
	block_list = (PyUnsignedIntBlock *)p;
	p = &((PyUnsignedIntBlock *)p)->objects[0];
	q = p + N_INTOBJECTS;
	while (--q > p)
		q->ob_type = (struct _typeobject *)(q-1);
	q->ob_type = NULL;
	return p + N_INTOBJECTS - 1;
}

#ifndef NSMALLPOSINTS
#define NSMALLPOSINTS		100
#endif
#ifndef NSMALLNEGINTS
#define NSMALLNEGINTS		1
#endif
#if NSMALLNEGINTS + NSMALLPOSINTS > 0
/* References to small integers are saved in this array so that they
   can be shared.
   The integers that are saved are those in the range
   -NSMALLNEGINTS (inclusive) to NSMALLPOSINTS (not inclusive).
*/
static PyUnsignedIntObject *small_ints[NSMALLNEGINTS + NSMALLPOSINTS];
#endif
#ifdef COUNT_ALLOCS
int quick_unsignedint_allocs, quick_neg_unsignedint_allocs;
#endif

PyObject *
PyUnsignedInt_FromLong(long ival)
{
	register PyUnsignedIntObject *v;
#if NSMALLNEGINTS + NSMALLPOSINTS > 0
	if (-NSMALLNEGINTS <= ival && ival < NSMALLPOSINTS &&
	    (v = small_ints[ival + NSMALLNEGINTS]) != NULL) {
		Py_INCREF(v);
#ifdef COUNT_ALLOCS
		if (ival >= 0)
			quick_unsignedint_allocs++;
		else
			quick_neg_unsignedint_allocs++;
#endif
		return (PyObject *) v;
	}
#endif
	if (free_list == NULL) {
		if ((free_list = fill_free_list()) == NULL)
			return NULL;
	}
	/* PyObject_New is inlined */
	v = free_list;
	free_list = (PyUnsignedIntObject *)v->ob_type;
	PyObject_INIT(v, &PyUnsignedInt_Type);
	v->ob_ival = ival;
#if NSMALLNEGINTS + NSMALLPOSINTS > 0
	if (-NSMALLNEGINTS <= ival && ival < NSMALLPOSINTS) {
		/* save this one for a following allocation */
		Py_INCREF(v);
		small_ints[ival + NSMALLNEGINTS] = v;
	}
#endif
	return (PyObject *) v;
}

static void
unsignedint_dealloc(PyUnsignedIntObject *v)
{
	if (PyUnsignedInt_CheckExact(v)) {
		v->ob_type = (struct _typeobject *)free_list;
		free_list = v;
	}
	else
		v->ob_type->tp_free((PyObject *)v);
}

static void
unsignedint_free(PyUnsignedIntObject *v)
{
	v->ob_type = (struct _typeobject *)free_list;
	free_list = v;
}

long
PyUnsignedInt_AsLong(register PyObject *op)
{
	PyNumberMethods *nb;
	PyUnsignedIntObject *io;
	long val;

	if (op && PyUnsignedInt_Check(op))
		return PyUnsignedInt_AS_LONG((PyUnsignedIntObject*) op);

	if (op == NULL || (nb = op->ob_type->tp_as_number) == NULL ||
	    nb->nb_int == NULL) {
		PyErr_SetString(PyExc_TypeError, "an integer is required");
		return -1;
	}

	io = (PyUnsignedIntObject*) (*nb->nb_int) (op);
	if (io == NULL)
		return -1;
	if (!PyUnsignedInt_Check(io)) {
		PyErr_SetString(PyExc_TypeError,
				"nb_int should return int object");
		return -1;
	}

	val = PyUnsignedInt_AS_LONG(io);
	Py_DECREF(io);

	return val;
}

PyObject *
PyUnsignedInt_FromString(char *s, char **pend, int base)
{
	char *end;
	long x;
	char buffer[256]; /* For errors */

	if ((base != 0 && base < 2) || base > 36) {
		PyErr_SetString(PyExc_ValueError, "int() base must be >= 2 and <= 36");
		return NULL;
	}

	while (*s && isspace(Py_CHARMASK(*s)))
		s++;
	errno = 0;
	if (base == 0 && s[0] == '0')
		x = (long) PyOS_strtoul(s, &end, base);
	else
		x = PyOS_strtol(s, &end, base);
	if (end == s || !isalnum(Py_CHARMASK(end[-1])))
		goto bad;
	while (*end && isspace(Py_CHARMASK(*end)))
		end++;
	if (*end != '\0') {
  bad:
		PyOS_snprintf(buffer, sizeof(buffer),
			      "invalid literal for int(): %.200s", s);
		PyErr_SetString(PyExc_ValueError, buffer);
		return NULL;
	}
	else if (errno != 0) {
		PyOS_snprintf(buffer, sizeof(buffer),
			      "int() literal too large: %.200s", s);
		PyErr_SetString(PyExc_ValueError, buffer);
		return NULL;
	}
	if (pend)
		*pend = end;
	return PyUnsignedInt_FromLong(x);
}

#ifdef Py_USING_UNICODE
PyObject *
PyUnsignedInt_FromUnicode(Py_UNICODE *s, int length, int base)
{
	char buffer[256];

	if (length >= sizeof(buffer)) {
		PyErr_SetString(PyExc_ValueError,
				"int() literal too large to convert");
		return NULL;
	}
	if (PyUnicode_EncodeDecimal(s, length, buffer, NULL))
		return NULL;
	return PyUnsignedInt_FromString(buffer, NULL, base);
}
#endif

/* Methods */

/* Integers are seen as the "smallest" of all numeric types and thus
   don't have any knowledge about conversion of other types to
   integers. */

#define CONVERT_TO_LONG(obj, lng)		\
	if (PyUnsignedInt_Check(obj)) {			\
		lng = PyUnsignedInt_AS_LONG(obj);	\
	}					\
	else {					\
		Py_INCREF(Py_NotImplemented);	\
		return Py_NotImplemented;	\
	}

/* ARGSUSED */
static int
unsignedint_print(PyUnsignedIntObject *v, FILE *fp, int flags)
     /* flags -- not used but required by interface */
{
	fprintf(fp, "%ld", v->ob_ival);
	return 0;
}

static PyObject *
unsignedint_repr(PyUnsignedIntObject *v)
{
	char buf[64];
	PyOS_snprintf(buf, sizeof(buf), "%ld", v->ob_ival);
	return PyString_FromString(buf);
}

static int
unsignedint_compare(PyUnsignedIntObject *v, PyUnsignedIntObject *w)
{
	register long i = v->ob_ival;
	register long j = w->ob_ival;
	return (i < j) ? -1 : (i > j) ? 1 : 0;
}

static long
unsignedint_hash(PyUnsignedIntObject *v)
{
	/* XXX If this is changed, you also need to change the way
	   Python's long, float and complex types are hashed. */
	long x = v -> ob_ival;
	if (x == -1)
		x = -2;
	return x;
}

static PyObject *
unsignedint_add(PyUnsignedIntObject *v, PyUnsignedIntObject *w)
{
	register long a, b, x;
	CONVERT_TO_LONG(v, a);
	CONVERT_TO_LONG(w, b);
	x = a + b;
	if ((x^a) >= 0 || (x^b) >= 0)
		return PyUnsignedInt_FromLong(x);
	if (err_ovf("integer addition"))
		return NULL;
	return PyLong_Type.tp_as_number->nb_add((PyObject *)v, (PyObject *)w);
}

static PyObject *
unsignedint_sub(PyUnsignedIntObject *v, PyUnsignedIntObject *w)
{
	register long a, b, x;
	CONVERT_TO_LONG(v, a);
	CONVERT_TO_LONG(w, b);
	x = a - b;
	if ((x^a) >= 0 || (x^~b) >= 0)
		return PyUnsignedInt_FromLong(x);
	if (err_ovf("integer subtraction"))
		return NULL;
	return PyLong_Type.tp_as_number->nb_subtract((PyObject *)v,
						     (PyObject *)w);
}

/*
Integer overflow checking for * is painful:  Python tried a couple ways, but
they didn't work on all platforms, or failed in endcases (a product of
-sys.maxint-1 has been a particular pain).

Here's another way:

The native long product x*y is either exactly right or *way* off, being
just the last n bits of the true product, where n is the number of bits
in a long (the delivered product is the true product plus i*2**n for
some integer i).

The native double product (double)x * (double)y is subject to three
rounding errors:  on a sizeof(long)==8 box, each cast to double can lose
info, and even on a sizeof(long)==4 box, the multiplication can lose info.
But, unlike the native long product, it's not in *range* trouble:  even
if sizeof(long)==32 (256-bit longs), the product easily fits in the
dynamic range of a double.  So the leading 50 (or so) bits of the double
product are correct.

We check these two ways against each other, and declare victory if they're
approximately the same.  Else, because the native long product is the only
one that can lose catastrophic amounts of information, it's the native long
product that must have overflowed.
*/

/* Return true if the sq_repeat method should be used */
#define USE_SQ_REPEAT(o) (!PyUnsignedInt_Check(o) && \
			  o->ob_type->tp_as_sequence && \
			  o->ob_type->tp_as_sequence->sq_repeat && \
			  !(o->ob_type->tp_as_number && \
                            o->ob_type->tp_flags & Py_TPFLAGS_CHECKTYPES && \
			    o->ob_type->tp_as_number->nb_multiply))

static PyObject *
unsignedint_mul(PyObject *v, PyObject *w)
{
	long a, b;
	long longprod;			/* a*b in native long arithmetic */
	double doubled_longprod;	/* (double)longprod */
	double doubleprod;		/* (double)a * (double)b */

	if (USE_SQ_REPEAT(v)) {
	  repeat:
		/* sequence * int */
		a = PyUnsignedInt_AsLong(w);
#if LONG_MAX != INT_MAX
		if (a > INT_MAX) {
			PyErr_SetString(PyExc_ValueError,
					"sequence repeat count too large");
			return NULL;
		}
		else if (a < INT_MIN)
			a = INT_MIN;
		/* XXX Why don't I either

		   - set a to -1 whenever it's negative (after all,
		     sequence repeat usually treats negative numbers
		     as zero(); or

		   - raise an exception when it's less than INT_MIN?

		   I'm thinking about a hypothetical use case where some
		   sequence type might use a negative value as a flag of
		   some kind.  In those cases I don't want to break the
		   code by mapping all negative values to -1.  But I also
		   don't want to break e.g. []*(-sys.maxint), which is
		   perfectly safe, returning [].  As a compromise, I do
		   map out-of-range negative values.
		*/
#endif
		return (*v->ob_type->tp_as_sequence->sq_repeat)(v, a);
	}
	if (USE_SQ_REPEAT(w)) {
		PyObject *tmp = v;
		v = w;
		w = tmp;
		goto repeat;
	}

	CONVERT_TO_LONG(v, a);
	CONVERT_TO_LONG(w, b);
	longprod = a * b;
	doubleprod = (double)a * (double)b;
	doubled_longprod = (double)longprod;

	/* Fast path for normal case:  small multiplicands, and no info
	   is lost in either method. */
	if (doubled_longprod == doubleprod)
		return PyUnsignedInt_FromLong(longprod);

	/* Somebody somewhere lost info.  Close enough, or way off?  Note
	   that a != 0 and b != 0 (else doubled_longprod == doubleprod == 0).
	   The difference either is or isn't significant compared to the
	   true value (of which doubleprod is a good approximation).
	*/
	{
		const double diff = doubled_longprod - doubleprod;
		const double absdiff = diff >= 0.0 ? diff : -diff;
		const double absprod = doubleprod >= 0.0 ? doubleprod :
							  -doubleprod;
		/* absdiff/absprod <= 1/32 iff
		   32 * absdiff <= absprod -- 5 good bits is "close enough" */
		if (32.0 * absdiff <= absprod)
			return PyUnsignedInt_FromLong(longprod);
		else if (err_ovf("integer multiplication"))
			return NULL;
		else
			return PyLong_Type.tp_as_number->nb_multiply(v, w);
	}
}

/* Return type of i_divmod */
enum divmod_result {
	DIVMOD_OK,		/* Correct result */
	DIVMOD_OVERFLOW,	/* Overflow, try again using longs */
	DIVMOD_ERROR		/* Exception raised */
};

static enum divmod_result
i_divmod(register long x, register long y,
         long *p_xdivy, long *p_xmody)
{
	long xdivy, xmody;

	if (y == 0) {
		PyErr_SetString(PyExc_ZeroDivisionError,
				"integer division or modulo by zero");
		return DIVMOD_ERROR;
	}
	/* (-sys.maxint-1)/-1 is the only overflow case. */
	if (y == -1 && x < 0 && x == -x) {
		if (err_ovf("integer division"))
			return DIVMOD_ERROR;
		return DIVMOD_OVERFLOW;
	}
	xdivy = x / y;
	xmody = x - xdivy * y;
	/* If the signs of x and y differ, and the remainder is non-0,
	 * C89 doesn't define whether xdivy is now the floor or the
	 * ceiling of the infinitely precise quotient.  We want the floor,
	 * and we have it iff the remainder's sign matches y's.
	 */
	if (xmody && ((y ^ xmody) < 0) /* i.e. and signs differ */) {
		xmody += y;
		--xdivy;
		assert(xmody && ((y ^ xmody) >= 0));
	}
	*p_xdivy = xdivy;
	*p_xmody = xmody;
	return DIVMOD_OK;
}

static PyObject *
unsignedint_div(PyUnsignedIntObject *x, PyUnsignedIntObject *y)
{
	long xi, yi;
	long d, m;
	CONVERT_TO_LONG(x, xi);
	CONVERT_TO_LONG(y, yi);
	switch (i_divmod(xi, yi, &d, &m)) {
	case DIVMOD_OK:
		return PyUnsignedInt_FromLong(d);
	case DIVMOD_OVERFLOW:
		return PyLong_Type.tp_as_number->nb_divide((PyObject *)x,
							   (PyObject *)y);
	default:
		return NULL;
	}
}

static PyObject *
unsignedint_classic_div(PyUnsignedIntObject *x, PyUnsignedIntObject *y)
{
	long xi, yi;
	long d, m;
	CONVERT_TO_LONG(x, xi);
	CONVERT_TO_LONG(y, yi);
	if (Py_DivisionWarningFlag &&
	    PyErr_Warn(PyExc_DeprecationWarning, "classic int division") < 0)
		return NULL;
	switch (i_divmod(xi, yi, &d, &m)) {
	case DIVMOD_OK:
		return PyUnsignedInt_FromLong(d);
	case DIVMOD_OVERFLOW:
		return PyLong_Type.tp_as_number->nb_divide((PyObject *)x,
							   (PyObject *)y);
	default:
		return NULL;
	}
}

static PyObject *
unsignedint_true_divide(PyObject *v, PyObject *w)
{
	/* If they aren't both ints, give someone else a chance.  In
	   particular, this lets int/long get handled by longs, which
	   underflows to 0 gracefully if the long is too big to convert
	   to float. */
	if (PyUnsignedInt_Check(v) && PyUnsignedInt_Check(w))
		return PyFloat_Type.tp_as_number->nb_true_divide(v, w);
	Py_INCREF(Py_NotImplemented);
	return Py_NotImplemented;
}

static PyObject *
unsignedint_mod(PyUnsignedIntObject *x, PyUnsignedIntObject *y)
{
	long xi, yi;
	long d, m;
	CONVERT_TO_LONG(x, xi);
	CONVERT_TO_LONG(y, yi);
	switch (i_divmod(xi, yi, &d, &m)) {
	case DIVMOD_OK:
		return PyUnsignedInt_FromLong(m);
	case DIVMOD_OVERFLOW:
		return PyLong_Type.tp_as_number->nb_remainder((PyObject *)x,
							      (PyObject *)y);
	default:
		return NULL;
	}
}

static PyObject *
unsignedint_divmod(PyUnsignedIntObject *x, PyUnsignedIntObject *y)
{
	long xi, yi;
	long d, m;
	CONVERT_TO_LONG(x, xi);
	CONVERT_TO_LONG(y, yi);
	switch (i_divmod(xi, yi, &d, &m)) {
	case DIVMOD_OK:
		return Py_BuildValue("(ll)", d, m);
	case DIVMOD_OVERFLOW:
		return PyLong_Type.tp_as_number->nb_divmod((PyObject *)x,
							   (PyObject *)y);
	default:
		return NULL;
	}
}

static PyObject *
unsignedint_pow(PyUnsignedIntObject *v, PyUnsignedIntObject *w, PyUnsignedIntObject *z)
{
	register long iv, iw, iz=0, ix, temp, prev;
	CONVERT_TO_LONG(v, iv);
	CONVERT_TO_LONG(w, iw);
	if (iw < 0) {
		if ((PyObject *)z != Py_None) {
			PyErr_SetString(PyExc_TypeError, "pow() 2nd argument "
			     "cannot be negative when 3rd argument specified");
			return NULL;
		}
		/* Return a float.  This works because we know that
		   this calls float_pow() which converts its
		   arguments to double. */
		return PyFloat_Type.tp_as_number->nb_power(
			(PyObject *)v, (PyObject *)w, (PyObject *)z);
	}
 	if ((PyObject *)z != Py_None) {
		CONVERT_TO_LONG(z, iz);
		if (iz == 0) {
			PyErr_SetString(PyExc_ValueError,
					"pow() 3rd argument cannot be 0");
			return NULL;
		}
	}
	/*
	 * XXX: The original exponentiation code stopped looping
	 * when temp hit zero; this code will continue onwards
	 * unnecessarily, but at least it won't cause any errors.
	 * Hopefully the speed improvement from the fast exponentiation
	 * will compensate for the slight inefficiency.
	 * XXX: Better handling of overflows is desperately needed.
	 */
 	temp = iv;
	ix = 1;
	while (iw > 0) {
	 	prev = ix;	/* Save value for overflow check */
	 	if (iw & 1) {
		 	ix = ix*temp;
			if (temp == 0)
				break; /* Avoid ix / 0 */
			if (ix / temp != prev) {
				if (err_ovf("integer exponentiation"))
					return NULL;
				return PyLong_Type.tp_as_number->nb_power(
					(PyObject *)v,
					(PyObject *)w,
					(PyObject *)z);
			}
		}
	 	iw >>= 1;	/* Shift exponent down by 1 bit */
	        if (iw==0) break;
	 	prev = temp;
	 	temp *= temp;	/* Square the value of temp */
	 	if (prev!=0 && temp/prev!=prev) {
			if (err_ovf("integer exponentiation"))
				return NULL;
			return PyLong_Type.tp_as_number->nb_power(
				(PyObject *)v, (PyObject *)w, (PyObject *)z);
		}
	 	if (iz) {
			/* If we did a multiplication, perform a modulo */
		 	ix = ix % iz;
		 	temp = temp % iz;
		}
	}
	if (iz) {
	 	long div, mod;
		switch (i_divmod(ix, iz, &div, &mod)) {
		case DIVMOD_OK:
			ix = mod;
			break;
		case DIVMOD_OVERFLOW:
			return PyLong_Type.tp_as_number->nb_power(
				(PyObject *)v, (PyObject *)w, (PyObject *)z);
		default:
			return NULL;
		}
	}
	return PyUnsignedInt_FromLong(ix);
}

static PyObject *
unsignedint_neg(PyUnsignedIntObject *v)
{
	register long a, x;
	a = v->ob_ival;
	x = -a;
	if (a < 0 && x < 0) {
		PyObject *o;
		if (err_ovf("integer negation"))
			return NULL;
		o = PyLong_FromLong(a);
		if (o != NULL) {
			PyObject *result = PyNumber_Negative(o);
			Py_DECREF(o);
			return result;
		}
		return NULL;
	}
	return PyUnsignedInt_FromLong(x);
}

static PyObject *
unsignedint_pos(PyUnsignedIntObject *v)
{
	if (PyUnsignedInt_CheckExact(v)) {
		Py_INCREF(v);
		return (PyObject *)v;
	}
	else
		return PyUnsignedInt_FromLong(v->ob_ival);
}

static PyObject *
unsignedint_abs(PyUnsignedIntObject *v)
{
	if (v->ob_ival >= 0)
		return int_pos(v);
	else
		return int_neg(v);
}

static int
unsignedint_nonzero(PyUnsignedIntObject *v)
{
	return v->ob_ival != 0;
}

static PyObject *
unsignedint_invert(PyUnsignedIntObject *v)
{
	return PyUnsignedInt_FromLong(~v->ob_ival);
}

static PyObject *
unsignedint_lshift(PyUnsignedIntObject *v, PyUnsignedIntObject *w)
{
	register long a, b;
	CONVERT_TO_LONG(v, a);
	CONVERT_TO_LONG(w, b);
	if (b < 0) {
		PyErr_SetString(PyExc_ValueError, "negative shift count");
		return NULL;
	}
	if (a == 0 || b == 0)
		return int_pos(v);
	if (b >= LONG_BIT) {
		return PyUnsignedInt_FromLong(0L);
	}
	a = (long)((unsigned long)a << b);
	return PyUnsignedInt_FromLong(a);
}

static PyObject *
unsignedint_rshift(PyUnsignedIntObject *v, PyUnsignedIntObject *w)
{
	register long a, b;
	CONVERT_TO_LONG(v, a);
	CONVERT_TO_LONG(w, b);
	if (b < 0) {
		PyErr_SetString(PyExc_ValueError, "negative shift count");
		return NULL;
	}
	if (a == 0 || b == 0)
		return int_pos(v);
	if (b >= LONG_BIT) {
		if (a < 0)
			a = -1;
		else
			a = 0;
	}
	else {
		a = Py_ARITHMETIC_RIGHT_SHIFT(long, a, b);
	}
	return PyUnsignedInt_FromLong(a);
}

static PyObject *
unsignedint_and(PyUnsignedIntObject *v, PyUnsignedIntObject *w)
{
	register long a, b;
	CONVERT_TO_LONG(v, a);
	CONVERT_TO_LONG(w, b);
	return PyUnsignedInt_FromLong(a & b);
}

static PyObject *
unsignedint_xor(PyUnsignedIntObject *v, PyUnsignedIntObject *w)
{
	register long a, b;
	CONVERT_TO_LONG(v, a);
	CONVERT_TO_LONG(w, b);
	return PyUnsignedInt_FromLong(a ^ b);
}

static PyObject *
unsignedint_or(PyUnsignedIntObject *v, PyUnsignedIntObject *w)
{
	register long a, b;
	CONVERT_TO_LONG(v, a);
	CONVERT_TO_LONG(w, b);
	return PyUnsignedInt_FromLong(a | b);
}

static int
unsignedint_coerce(PyObject **pv, PyObject **pw)
{
	if (PyUnsignedInt_Check(*pw)) {
		Py_INCREF(*pv);
		Py_INCREF(*pw);
		return 0;
	}
	return 1; /* Can't do it */
}

static PyObject *
unsignedint_int(PyUnsignedIntObject *v)
{
	Py_INCREF(v);
	return (PyObject *)v;
}

static PyObject *
unsignedint_long(PyUnsignedIntObject *v)
{
	return PyLong_FromLong((v -> ob_ival));
}

static PyObject *
unsignedint_float(PyUnsignedIntObject *v)
{
	return PyFloat_FromDouble((double)(v -> ob_ival));
}

static PyObject *
unsignedint_oct(PyUnsignedIntObject *v)
{
	char buf[100];
	long x = v -> ob_ival;
	if (x == 0)
		strcpy(buf, "0");
	else
		PyOS_snprintf(buf, sizeof(buf), "0%lo", x);
	return PyString_FromString(buf);
}

static PyObject *
unsignedint_hex(PyUnsignedIntObject *v)
{
	char buf[100];
	long x = v -> ob_ival;
	PyOS_snprintf(buf, sizeof(buf), "0x%lx", x);
	return PyString_FromString(buf);
}

staticforward PyObject *
unsignedint_subtype_new(PyTypeObject *type, PyObject *args, PyObject *kwds);

static PyObject *
unsignedint_new(PyTypeObject *type, PyObject *args, PyObject *kwds)
{
	PyObject *x = NULL;
	int base = -909;
	static char *kwlist[] = {"x", "base", 0};

	if (type != &PyUnsignedInt_Type)
		return int_subtype_new(type, args, kwds); /* Wimp out */
	if (!PyArg_ParseTupleAndKeywords(args, kwds, "|Oi:int", kwlist,
					 &x, &base))
		return NULL;
	if (x == NULL)
		return PyUnsignedInt_FromLong(0L);
	if (base == -909)
		return PyNumber_Int(x);
	if (PyString_Check(x))
		return PyUnsignedInt_FromString(PyString_AS_STRING(x), NULL, base);
#ifdef Py_USING_UNICODE
	if (PyUnicode_Check(x))
		return PyUnsignedInt_FromUnicode(PyUnicode_AS_UNICODE(x),
					 PyUnicode_GET_SIZE(x),
					 base);
#endif
	PyErr_SetString(PyExc_TypeError,
			"int() can't convert non-string with explicit base");
	return NULL;
}

/* Wimpy, slow approach to tp_new calls for subtypes of int:
   first create a regular int from whatever arguments we got,
   then allocate a subtype instance and initialize its ob_ival
   from the regular int.  The regular int is then thrown away.
*/
static PyObject *
unsignedint_subtype_new(PyTypeObject *type, PyObject *args, PyObject *kwds)
{
	PyObject *tmp, *new;

	assert(PyType_IsSubtype(type, &PyUnsignedInt_Type));
	tmp = int_new(&PyUnsignedInt_Type, args, kwds);
	if (tmp == NULL)
		return NULL;
	assert(PyUnsignedInt_Check(tmp));
	new = type->tp_alloc(type, 0);
	if (new == NULL)
		return NULL;
	((PyUnsignedIntObject *)new)->ob_ival = ((PyUnsignedIntObject *)tmp)->ob_ival;
	Py_DECREF(tmp);
	return new;
}

static char int_doc[] =
"int(x[, base]) -> integer\n\
\n\
Convert a string or number to an integer, if possible.  A floating point\n\
argument will be truncated towards zero (this does not include a string\n\
representation of a floating point number!)  When converting a string, use\n\
the optional base.  It is an error to supply a base when converting a\n\
non-string.";

static PyNumberMethods int_as_number = {
	(binaryfunc)int_add,	/*nb_add*/
	(binaryfunc)int_sub,	/*nb_subtract*/
	(binaryfunc)int_mul,	/*nb_multiply*/
	(binaryfunc)int_classic_div, /*nb_divide*/
	(binaryfunc)int_mod,	/*nb_remainder*/
	(binaryfunc)int_divmod,	/*nb_divmod*/
	(ternaryfunc)int_pow,	/*nb_power*/
	(unaryfunc)int_neg,	/*nb_negative*/
	(unaryfunc)int_pos,	/*nb_positive*/
	(unaryfunc)int_abs,	/*nb_absolute*/
	(inquiry)int_nonzero,	/*nb_nonzero*/
	(unaryfunc)int_invert,	/*nb_invert*/
	(binaryfunc)int_lshift,	/*nb_lshift*/
	(binaryfunc)int_rshift,	/*nb_rshift*/
	(binaryfunc)int_and,	/*nb_and*/
	(binaryfunc)int_xor,	/*nb_xor*/
	(binaryfunc)int_or,	/*nb_or*/
	int_coerce,		/*nb_coerce*/
	(unaryfunc)int_int,	/*nb_int*/
	(unaryfunc)int_long,	/*nb_long*/
	(unaryfunc)int_float,	/*nb_float*/
	(unaryfunc)int_oct,	/*nb_oct*/
	(unaryfunc)int_hex, 	/*nb_hex*/
	0,			/*nb_inplace_add*/
	0,			/*nb_inplace_subtract*/
	0,			/*nb_inplace_multiply*/
	0,			/*nb_inplace_divide*/
	0,			/*nb_inplace_remainder*/
	0,			/*nb_inplace_power*/
	0,			/*nb_inplace_lshift*/
	0,			/*nb_inplace_rshift*/
	0,			/*nb_inplace_and*/
	0,			/*nb_inplace_xor*/
	0,			/*nb_inplace_or*/
	(binaryfunc)int_div,	/* nb_floor_divide */
	int_true_divide,	/* nb_true_divide */
	0,			/* nb_inplace_floor_divide */
	0,			/* nb_inplace_true_divide */
};

PyTypeObject PyUnsignedInt_Type = {
	PyObject_HEAD_INIT(&PyType_Type)
	0,
	"int",
	sizeof(PyUnsignedIntObject),
	0,
	(destructor)int_dealloc,		/* tp_dealloc */
	(printfunc)int_print,			/* tp_print */
	0,					/* tp_getattr */
	0,					/* tp_setattr */
	(cmpfunc)int_compare,			/* tp_compare */
	(reprfunc)int_repr,			/* tp_repr */
	&int_as_number,				/* tp_as_number */
	0,					/* tp_as_sequence */
	0,					/* tp_as_mapping */
	(hashfunc)int_hash,			/* tp_hash */
        0,					/* tp_call */
        (reprfunc)int_repr,			/* tp_str */
	PyObject_GenericGetAttr,		/* tp_getattro */
	0,					/* tp_setattro */
	0,					/* tp_as_buffer */
	Py_TPFLAGS_DEFAULT | Py_TPFLAGS_CHECKTYPES |
		Py_TPFLAGS_BASETYPE,		/* tp_flags */
	int_doc,				/* tp_doc */
	0,					/* tp_traverse */
	0,					/* tp_clear */
	0,					/* tp_richcompare */
	0,					/* tp_weaklistoffset */
	0,					/* tp_iter */
	0,					/* tp_iternext */
	0,					/* tp_methods */
	0,					/* tp_members */
	0,					/* tp_getset */
	0,					/* tp_base */
	0,					/* tp_dict */
	0,					/* tp_descr_get */
	0,					/* tp_descr_set */
	0,					/* tp_dictoffset */
	0,					/* tp_init */
	0,					/* tp_alloc */
	int_new,				/* tp_new */
	(destructor)int_free,         		/* tp_free */
};

void
PyUnsignedInt_Fini(void)
{
	PyUnsignedIntObject *p;
	PyUnsignedIntBlock *list, *next;
	int i;
	int bc, bf;	/* block count, number of freed blocks */
	int irem, isum;	/* remaining unfreed ints per block, total */

#if NSMALLNEGINTS + NSMALLPOSINTS > 0
        PyUnsignedIntObject **q;

        i = NSMALLNEGINTS + NSMALLPOSINTS;
        q = small_ints;
        while (--i >= 0) {
                Py_XDECREF(*q);
                *q++ = NULL;
        }
#endif
	bc = 0;
	bf = 0;
	isum = 0;
	list = block_list;
	block_list = NULL;
	free_list = NULL;
	while (list != NULL) {
		bc++;
		irem = 0;
		for (i = 0, p = &list->objects[0];
		     i < N_INTOBJECTS;
		     i++, p++) {
			if (PyUnsignedInt_CheckExact(p) && p->ob_refcnt != 0)
				irem++;
		}
		next = list->next;
		if (irem) {
			list->next = block_list;
			block_list = list;
			for (i = 0, p = &list->objects[0];
			     i < N_INTOBJECTS;
			     i++, p++) {
				if (!PyUnsignedInt_CheckExact(p) ||
				    p->ob_refcnt == 0) {
					p->ob_type = (struct _typeobject *)
						free_list;
					free_list = p;
				}
#if NSMALLNEGINTS + NSMALLPOSINTS > 0
				else if (-NSMALLNEGINTS <= p->ob_ival &&
					 p->ob_ival < NSMALLPOSINTS &&
					 small_ints[p->ob_ival +
						    NSMALLNEGINTS] == NULL) {
					Py_INCREF(p);
					small_ints[p->ob_ival +
						   NSMALLNEGINTS] = p;
				}
#endif
			}
		}
		else {
			PyMem_FREE(list); /* XXX PyObject_FREE ??? */
			bf++;
		}
		isum += irem;
		list = next;
	}
	if (!Py_VerboseFlag)
		return;
	fprintf(stderr, "# cleanup ints");
	if (!isum) {
		fprintf(stderr, "\n");
	}
	else {
		fprintf(stderr,
			": %d unfreed int%s in %d out of %d block%s\n",
			isum, isum == 1 ? "" : "s",
			bc - bf, bc, bc == 1 ? "" : "s");
	}
	if (Py_VerboseFlag > 1) {
		list = block_list;
		while (list != NULL) {
			for (i = 0, p = &list->objects[0];
			     i < N_INTOBJECTS;
			     i++, p++) {
				if (PyUnsignedInt_CheckExact(p) && p->ob_refcnt != 0)
					fprintf(stderr,
				"#   <int at %p, refcnt=%d, val=%ld>\n",
						p, p->ob_refcnt, p->ob_ival);
			}
			list = list->next;
		}
	}
}
