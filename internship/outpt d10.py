Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import random
dir(random)
['BPF', 'LOG4', 'NV_MAGICCONST', 'RECIP_BPF', 'Random', 'SG_MAGICCONST', 'SystemRandom', 'TWOPI', '_ONE', '_Sequence', '_Set', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_accumulate', '_acos', '_bisect', '_ceil', '_cos', '_e', '_exp', '_floor', '_index', '_inst', '_isfinite', '_log', '_os', '_pi', '_random', '_repeat', '_sha512', '_sin', '_sqrt', '_test', '_test_generator', '_urandom', '_warn', 'betavariate', 'choice', 'choices', 'expovariate', 'gammavariate', 'gauss', 'getrandbits', 'getstate', 'lognormvariate', 'normalvariate', 'paretovariate', 'randbytes', 'randint', 'random', 'randrange', 'sample', 'seed', 'setstate', 'shuffle', 'triangular', 'uniform', 'vonmisesvariate', 'weibullvariate']
i=123
dr(i)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    dr(i)
NameError: name 'dr' is not defined. Did you mean: 'dir'?
i=123
dir(i)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_count', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
help(random)
Help on module random:

NAME
    random - Random variable generators.

MODULE REFERENCE
    https://docs.python.org/3.11/library/random.html
    
    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
        bytes
        -----
               uniform bytes (values between 0 and 255)
    
        integers
        --------
               uniform within range
    
        sequences
        ---------
               pick random element
               pick random sample
               pick weighted random sample
               generate random permutation
    
        distributions on the real line:
        ------------------------------
               uniform
               triangular
               normal (Gaussian)
               lognormal
               negative exponential
               gamma
               beta
               pareto
               Weibull
    
        distributions on the circle (angles 0 to 2pi)
        ---------------------------------------------
               circular uniform
               von Mises
    
    General notes on the underlying Mersenne Twister core generator:
    
    * The period is 2**19937-1.
    * It is one of the most extensively tested generators in existence.
    * The random() method is implemented in C, executes in a single Python step,
      and is, therefore, threadsafe.

CLASSES
    _random.Random(builtins.object)
        Random
            SystemRandom
    
    class Random(_random.Random)
     |  Random(x=None)
     |  
     |  Random number generator base class used by bound module functions.
     |  
     |  Used to instantiate instances of Random to get generators that don't
     |  share state.
     |  
     |  Class Random can also be subclassed if you want to use a different basic
     |  generator of your own devising: in that case, override the following
     |  methods:  random(), seed(), getstate(), and setstate().
     |  Optionally, implement a getrandbits() method so that randrange()
     |  can cover arbitrarily large ranges.
     |  
     |  Method resolution order:
     |      Random
     |      _random.Random
     |      builtins.object
     |  
     |  Methods defined here:
     |  
     |  __getstate__(self)
     |      Helper for pickle.
     |  
     |  __init__(self, x=None)
     |      Initialize an instance.
     |      
     |      Optional argument x controls seeding, as for Random.seed().
     |  
     |  __reduce__(self)
     |      Helper for pickle.
     |  
     |  __setstate__(self, state)
     |  
     |  betavariate(self, alpha, beta)
     |      Beta distribution.
     |      
     |      Conditions on the parameters are alpha > 0 and beta > 0.
     |      Returned values range between 0 and 1.
     |  
     |  choice(self, seq)
     |      Choose a random element from a non-empty sequence.
     |  
     |  choices(self, population, weights=None, *, cum_weights=None, k=1)
     |      Return a k sized list of population elements chosen with replacement.
     |      
     |      If the relative weights or cumulative weights are not specified,
     |      the selections are made with equal probability.
     |  
     |  expovariate(self, lambd)
     |      Exponential distribution.
     |      
     |      lambd is 1.0 divided by the desired mean.  It should be
     |      nonzero.  (The parameter would be called "lambda", but that is
     |      a reserved word in Python.)  Returned values range from 0 to
     |      positive infinity if lambd is positive, and from negative
     |      infinity to 0 if lambd is negative.
     |  
     |  gammavariate(self, alpha, beta)
     |      Gamma distribution.  Not the gamma function!
     |      
     |      Conditions on the parameters are alpha > 0 and beta > 0.
     |      
     |      The probability distribution function is:
     |      
     |                  x ** (alpha - 1) * math.exp(-x / beta)
     |        pdf(x) =  --------------------------------------
     |                    math.gamma(alpha) * beta ** alpha
     |  
     |  gauss(self, mu=0.0, sigma=1.0)
     |      Gaussian distribution.
     |      
     |      mu is the mean, and sigma is the standard deviation.  This is
     |      slightly faster than the normalvariate() function.
     |      
     |      Not thread-safe without a lock around calls.
     |  
     |  getstate(self)
     |      Return internal state; can be passed to setstate() later.
     |  
     |  lognormvariate(self, mu, sigma)
     |      Log normal distribution.
     |      
     |      If you take the natural logarithm of this distribution, you'll get a
     |      normal distribution with mean mu and standard deviation sigma.
     |      mu can have any value, and sigma must be greater than zero.
     |  
     |  normalvariate(self, mu=0.0, sigma=1.0)
     |      Normal distribution.
     |      
     |      mu is the mean, and sigma is the standard deviation.
     |  
     |  paretovariate(self, alpha)
     |      Pareto distribution.  alpha is the shape parameter.
     |  
     |  randbytes(self, n)
     |      Generate n random bytes.
     |  
     |  randint(self, a, b)
     |      Return random integer in range [a, b], including both end points.
     |  
     |  randrange(self, start, stop=None, step=1)
     |      Choose a random item from range(stop) or range(start, stop[, step]).
     |      
     |      Roughly equivalent to ``choice(range(start, stop, step))`` but
     |      supports arbitrarily large ranges and is optimized for common cases.
     |  
     |  sample(self, population, k, *, counts=None)
     |      Chooses k unique random elements from a population sequence.
     |      
     |      Returns a new list containing elements from the population while
     |      leaving the original population unchanged.  The resulting list is
     |      in selection order so that all sub-slices will also be valid random
     |      samples.  This allows raffle winners (the sample) to be partitioned
     |      into grand prize and second place winners (the subslices).
     |      
     |      Members of the population need not be hashable or unique.  If the
     |      population contains repeats, then each occurrence is a possible
     |      selection in the sample.
     |      
     |      Repeated elements can be specified one at a time or with the optional
     |      counts parameter.  For example:
     |      
     |          sample(['red', 'blue'], counts=[4, 2], k=5)
     |      
     |      is equivalent to:
     |      
     |          sample(['red', 'red', 'red', 'red', 'blue', 'blue'], k=5)
     |      
     |      To choose a sample from a range of integers, use range() for the
     |      population argument.  This is especially fast and space efficient
     |      for sampling from a large population:
     |      
     |          sample(range(10000000), 60)
     |  
     |  seed(self, a=None, version=2)
     |      Initialize internal state from a seed.
     |      
     |      The only supported seed types are None, int, float,
     |      str, bytes, and bytearray.
     |      
     |      None or no argument seeds from current time or from an operating
     |      system specific randomness source if available.
     |      
     |      If *a* is an int, all bits are used.
     |      
     |      For version 2 (the default), all of the bits are used if *a* is a str,
     |      bytes, or bytearray.  For version 1 (provided for reproducing random
     |      sequences from older versions of Python), the algorithm for str and
     |      bytes generates a narrower range of seeds.
     |  
     |  setstate(self, state)
     |      Restore internal state from object returned by getstate().
     |  
     |  shuffle(self, x)
     |      Shuffle list x in place, and return None.
     |  
     |  triangular(self, low=0.0, high=1.0, mode=None)
     |      Triangular distribution.
     |      
     |      Continuous distribution bounded by given lower and upper limits,
     |      and having a given mode value in-between.
     |      
     |      http://en.wikipedia.org/wiki/Triangular_distribution
     |  
     |  uniform(self, a, b)
     |      Get a random number in the range [a, b) or [a, b] depending on rounding.
     |  
     |  vonmisesvariate(self, mu, kappa)
     |      Circular data distribution.
     |      
     |      mu is the mean angle, expressed in radians between 0 and 2*pi, and
     |      kappa is the concentration parameter, which must be greater than or
     |      equal to zero.  If kappa is equal to zero, this distribution reduces
     |      to a uniform random angle over the range 0 to 2*pi.
     |  
     |  weibullvariate(self, alpha, beta)
     |      Weibull distribution.
     |      
     |      alpha is the scale parameter and beta is the shape parameter.
     |  
     |  ----------------------------------------------------------------------
     |  Class methods defined here:
     |  
     |  __init_subclass__(**kwargs) from builtins.type
     |      Control how subclasses generate random integers.
     |      
     |      The algorithm a subclass can use depends on the random() and/or
     |      getrandbits() implementation available to it and determines
     |      whether it can generate random integers from arbitrarily large
     |      ranges.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  VERSION = 3
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from _random.Random:
     |  
     |  getrandbits(self, k, /)
     |      getrandbits(k) -> x.  Generates an int with k random bits.
     |  
     |  random(self, /)
     |      random() -> x in the interval [0, 1).
     |  
     |  ----------------------------------------------------------------------
     |  Static methods inherited from _random.Random:
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
    
    class SystemRandom(Random)
     |  SystemRandom(x=None)
     |  
     |  Alternate random number generator using sources provided
     |  by the operating system (such as /dev/urandom on Unix or
     |  CryptGenRandom on Windows).
     |  
     |   Not available on all systems (see os.urandom() for details).
     |  
     |  Method resolution order:
     |      SystemRandom
     |      Random
     |      _random.Random
     |      builtins.object
     |  
     |  Methods defined here:
     |  
     |  getrandbits(self, k)
     |      getrandbits(k) -> x.  Generates an int with k random bits.
     |  
     |  getstate = _notimplemented(self, *args, **kwds)
     |  
     |  randbytes(self, n)
     |      Generate n random bytes.
     |  
     |  random(self)
     |      Get the next random number in the range 0.0 <= X < 1.0.
     |  
     |  seed(self, *args, **kwds)
     |      Stub method.  Not used for a system random number generator.
     |  
     |  setstate = _notimplemented(self, *args, **kwds)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from Random:
     |  
     |  __getstate__(self)
     |      Helper for pickle.
     |  
     |  __init__(self, x=None)
     |      Initialize an instance.
     |      
     |      Optional argument x controls seeding, as for Random.seed().
     |  
     |  __reduce__(self)
     |      Helper for pickle.
     |  
     |  __setstate__(self, state)
     |  
     |  betavariate(self, alpha, beta)
     |      Beta distribution.
     |      
     |      Conditions on the parameters are alpha > 0 and beta > 0.
     |      Returned values range between 0 and 1.
     |  
     |  choice(self, seq)
     |      Choose a random element from a non-empty sequence.
     |  
     |  choices(self, population, weights=None, *, cum_weights=None, k=1)
     |      Return a k sized list of population elements chosen with replacement.
     |      
     |      If the relative weights or cumulative weights are not specified,
     |      the selections are made with equal probability.
     |  
     |  expovariate(self, lambd)
     |      Exponential distribution.
     |      
     |      lambd is 1.0 divided by the desired mean.  It should be
     |      nonzero.  (The parameter would be called "lambda", but that is
     |      a reserved word in Python.)  Returned values range from 0 to
     |      positive infinity if lambd is positive, and from negative
     |      infinity to 0 if lambd is negative.
     |  
     |  gammavariate(self, alpha, beta)
     |      Gamma distribution.  Not the gamma function!
     |      
     |      Conditions on the parameters are alpha > 0 and beta > 0.
     |      
     |      The probability distribution function is:
     |      
     |                  x ** (alpha - 1) * math.exp(-x / beta)
     |        pdf(x) =  --------------------------------------
     |                    math.gamma(alpha) * beta ** alpha
     |  
     |  gauss(self, mu=0.0, sigma=1.0)
     |      Gaussian distribution.
     |      
     |      mu is the mean, and sigma is the standard deviation.  This is
     |      slightly faster than the normalvariate() function.
     |      
     |      Not thread-safe without a lock around calls.
     |  
     |  lognormvariate(self, mu, sigma)
     |      Log normal distribution.
     |      
     |      If you take the natural logarithm of this distribution, you'll get a
     |      normal distribution with mean mu and standard deviation sigma.
     |      mu can have any value, and sigma must be greater than zero.
     |  
     |  normalvariate(self, mu=0.0, sigma=1.0)
     |      Normal distribution.
     |      
     |      mu is the mean, and sigma is the standard deviation.
     |  
     |  paretovariate(self, alpha)
     |      Pareto distribution.  alpha is the shape parameter.
     |  
     |  randint(self, a, b)
     |      Return random integer in range [a, b], including both end points.
     |  
     |  randrange(self, start, stop=None, step=1)
     |      Choose a random item from range(stop) or range(start, stop[, step]).
     |      
     |      Roughly equivalent to ``choice(range(start, stop, step))`` but
     |      supports arbitrarily large ranges and is optimized for common cases.
     |  
     |  sample(self, population, k, *, counts=None)
     |      Chooses k unique random elements from a population sequence.
     |      
     |      Returns a new list containing elements from the population while
     |      leaving the original population unchanged.  The resulting list is
     |      in selection order so that all sub-slices will also be valid random
     |      samples.  This allows raffle winners (the sample) to be partitioned
     |      into grand prize and second place winners (the subslices).
     |      
     |      Members of the population need not be hashable or unique.  If the
     |      population contains repeats, then each occurrence is a possible
     |      selection in the sample.
     |      
     |      Repeated elements can be specified one at a time or with the optional
     |      counts parameter.  For example:
     |      
     |          sample(['red', 'blue'], counts=[4, 2], k=5)
     |      
     |      is equivalent to:
     |      
     |          sample(['red', 'red', 'red', 'red', 'blue', 'blue'], k=5)
     |      
     |      To choose a sample from a range of integers, use range() for the
     |      population argument.  This is especially fast and space efficient
     |      for sampling from a large population:
     |      
     |          sample(range(10000000), 60)
     |  
     |  shuffle(self, x)
     |      Shuffle list x in place, and return None.
     |  
     |  triangular(self, low=0.0, high=1.0, mode=None)
     |      Triangular distribution.
     |      
     |      Continuous distribution bounded by given lower and upper limits,
     |      and having a given mode value in-between.
     |      
     |      http://en.wikipedia.org/wiki/Triangular_distribution
     |  
     |  uniform(self, a, b)
     |      Get a random number in the range [a, b) or [a, b] depending on rounding.
     |  
     |  vonmisesvariate(self, mu, kappa)
     |      Circular data distribution.
     |      
     |      mu is the mean angle, expressed in radians between 0 and 2*pi, and
     |      kappa is the concentration parameter, which must be greater than or
     |      equal to zero.  If kappa is equal to zero, this distribution reduces
     |      to a uniform random angle over the range 0 to 2*pi.
     |  
     |  weibullvariate(self, alpha, beta)
     |      Weibull distribution.
     |      
     |      alpha is the scale parameter and beta is the shape parameter.
     |  
     |  ----------------------------------------------------------------------
     |  Class methods inherited from Random:
     |  
     |  __init_subclass__(**kwargs) from builtins.type
     |      Control how subclasses generate random integers.
     |      
     |      The algorithm a subclass can use depends on the random() and/or
     |      getrandbits() implementation available to it and determines
     |      whether it can generate random integers from arbitrarily large
     |      ranges.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from Random:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from Random:
     |  
     |  VERSION = 3
     |  
     |  ----------------------------------------------------------------------
     |  Static methods inherited from _random.Random:
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.

FUNCTIONS
    betavariate(alpha, beta) method of Random instance
        Beta distribution.
        
        Conditions on the parameters are alpha > 0 and beta > 0.
        Returned values range between 0 and 1.
    
    choice(seq) method of Random instance
        Choose a random element from a non-empty sequence.
    
    choices(population, weights=None, *, cum_weights=None, k=1) method of Random instance
        Return a k sized list of population elements chosen with replacement.
        
        If the relative weights or cumulative weights are not specified,
        the selections are made with equal probability.
    
    expovariate(lambd) method of Random instance
        Exponential distribution.
        
        lambd is 1.0 divided by the desired mean.  It should be
        nonzero.  (The parameter would be called "lambda", but that is
        a reserved word in Python.)  Returned values range from 0 to
        positive infinity if lambd is positive, and from negative
        infinity to 0 if lambd is negative.
    
    gammavariate(alpha, beta) method of Random instance
        Gamma distribution.  Not the gamma function!
        
        Conditions on the parameters are alpha > 0 and beta > 0.
        
        The probability distribution function is:
        
                    x ** (alpha - 1) * math.exp(-x / beta)
          pdf(x) =  --------------------------------------
                      math.gamma(alpha) * beta ** alpha
    
    gauss(mu=0.0, sigma=1.0) method of Random instance
        Gaussian distribution.
        
        mu is the mean, and sigma is the standard deviation.  This is
        slightly faster than the normalvariate() function.
        
        Not thread-safe without a lock around calls.
    
    getrandbits(k, /) method of Random instance
        getrandbits(k) -> x.  Generates an int with k random bits.
    
    getstate() method of Random instance
        Return internal state; can be passed to setstate() later.
    
    lognormvariate(mu, sigma) method of Random instance
        Log normal distribution.
        
        If you take the natural logarithm of this distribution, you'll get a
        normal distribution with mean mu and standard deviation sigma.
        mu can have any value, and sigma must be greater than zero.
    
    normalvariate(mu=0.0, sigma=1.0) method of Random instance
        Normal distribution.
        
        mu is the mean, and sigma is the standard deviation.
    
    paretovariate(alpha) method of Random instance
        Pareto distribution.  alpha is the shape parameter.
    
    randbytes(n) method of Random instance
        Generate n random bytes.
    
    randint(a, b) method of Random instance
        Return random integer in range [a, b], including both end points.
    
    random() method of Random instance
        random() -> x in the interval [0, 1).
    
    randrange(start, stop=None, step=1) method of Random instance
        Choose a random item from range(stop) or range(start, stop[, step]).
        
        Roughly equivalent to ``choice(range(start, stop, step))`` but
        supports arbitrarily large ranges and is optimized for common cases.
    
    sample(population, k, *, counts=None) method of Random instance
        Chooses k unique random elements from a population sequence.
        
        Returns a new list containing elements from the population while
        leaving the original population unchanged.  The resulting list is
        in selection order so that all sub-slices will also be valid random
        samples.  This allows raffle winners (the sample) to be partitioned
        into grand prize and second place winners (the subslices).
        
        Members of the population need not be hashable or unique.  If the
        population contains repeats, then each occurrence is a possible
        selection in the sample.
        
        Repeated elements can be specified one at a time or with the optional
        counts parameter.  For example:
        
            sample(['red', 'blue'], counts=[4, 2], k=5)
        
        is equivalent to:
        
            sample(['red', 'red', 'red', 'red', 'blue', 'blue'], k=5)
        
        To choose a sample from a range of integers, use range() for the
        population argument.  This is especially fast and space efficient
        for sampling from a large population:
        
            sample(range(10000000), 60)
    
    seed(a=None, version=2) method of Random instance
        Initialize internal state from a seed.
        
        The only supported seed types are None, int, float,
        str, bytes, and bytearray.
        
        None or no argument seeds from current time or from an operating
        system specific randomness source if available.
        
        If *a* is an int, all bits are used.
        
        For version 2 (the default), all of the bits are used if *a* is a str,
        bytes, or bytearray.  For version 1 (provided for reproducing random
        sequences from older versions of Python), the algorithm for str and
        bytes generates a narrower range of seeds.
    
    setstate(state) method of Random instance
        Restore internal state from object returned by getstate().
    
    shuffle(x) method of Random instance
        Shuffle list x in place, and return None.
    
    triangular(low=0.0, high=1.0, mode=None) method of Random instance
        Triangular distribution.
        
        Continuous distribution bounded by given lower and upper limits,
        and having a given mode value in-between.
        
        http://en.wikipedia.org/wiki/Triangular_distribution
    
    uniform(a, b) method of Random instance
        Get a random number in the range [a, b) or [a, b] depending on rounding.
    
    vonmisesvariate(mu, kappa) method of Random instance
        Circular data distribution.
        
        mu is the mean angle, expressed in radians between 0 and 2*pi, and
        kappa is the concentration parameter, which must be greater than or
        equal to zero.  If kappa is equal to zero, this distribution reduces
        to a uniform random angle over the range 0 to 2*pi.
    
    weibullvariate(alpha, beta) method of Random instance
        Weibull distribution.
        
        alpha is the scale parameter and beta is the shape parameter.

DATA
    __all__ = ['Random', 'SystemRandom', 'betavariate', 'choice', 'choices...

FILE
    c:\users\pasupuleti\appdata\local\programs\python\python311\lib\random.py








import random
random.Random()
<random.Random object at 0x0000026BE67B2AF0>
random.random()
0.5637343932336583
for i in range(1,10,2):
    print(i)

    
1
3
5
7
9
for i in range(7)
SyntaxError: incomplete input
for in in range(7):
    
SyntaxError: invalid syntax
for i in range(7):
    print(i)

    
0
1
2
3
4
5
6
for i in range(1,10,1):
    print(i)

    
1
2
3
4
5
6
7
8
9
for i in range(10,-1,-1):
    print(i)

    
10
9
8
7
6
5
4
3
2
1
0
random randint(1,10)
               
SyntaxError: invalid syntax
random.randint(1,10)
               
2
random.randrange(1,10)
               
2
import random
random.choice(['rock','paper','scissor'])
'rock'
import random
random.choice(['rock','paper','scissor'])
SyntaxError: multiple statements found while compiling a single statement
random.choice(['rock','paper','scissor'])
'paper'
random.choice(['rock','paper','scissor'])
'scissor'
random.choice(['rock','paper','scissor'])
'scissor'
import random
player1=input('enter rock/paper/scissor')
enter rock/paper/scissor
================================================= RESTART: C:/Users/Pasupuleti/OneDrive/Desktop/internship/d10.py =================================================
enter rock/paper/scissor
================================================= RESTART: C:/Users/Pasupuleti/OneDrive/Desktop/internship/d10.py =================================================
enter rock/paper/scissorrock
scissor
player1 rocks cpu shocks

================================================= RESTART: C:/Users/Pasupuleti/OneDrive/Desktop/internship/d10.py =================================================
enter rock/paper/scissorrock
paper
cpu rocks player1 shocks

================================================= RESTART: C:/Users/Pasupuleti/OneDrive/Desktop/internship/d10.py =================================================
enter rock/paper/scissor;PAPER
scissor
There is a type error in response entered tried again

================================================= RESTART: C:/Users/Pasupuleti/OneDrive/Desktop/internship/d10.py =================================================
Traceback (most recent call last):
  File "C:/Users/Pasupuleti/OneDrive/Desktop/internship/d10.py", line 29, in <module>
    import smtplip
ModuleNotFoundError: No module named 'smtplip'
>>> 
================================================= RESTART: C:/Users/Pasupuleti/OneDrive/Desktop/internship/d10.py =================================================
Traceback (most recent call last):
  File "C:/Users/Pasupuleti/OneDrive/Desktop/internship/d10.py", line 29, in <module>
    import smtplip
ModuleNotFoundError: No module named 'smtplip'
>>> 
================================================= RESTART: C:/Users/Pasupuleti/OneDrive/Desktop/internship/d10.py =================================================
Traceback (most recent call last):
  File "C:/Users/Pasupuleti/OneDrive/Desktop/internship/d10.py", line 34, in <module>
    server.sendm,ail('jahnavipasupuleti1302@gmail.com','manumanisha1999@gmail.com','mail from python')
AttributeError: 'SMTP' object has no attribute 'sendm'. Did you mean: 'send'?
>>> 
================================================= RESTART: C:/Users/Pasupuleti/OneDrive/Desktop/internship/d10.py =================================================
mail sent
>>> 
================================================= RESTART: C:/Users/Pasupuleti/OneDrive/Desktop/internship/d10.py =================================================
enter to mailmanumanisha1999@gmail.com
mail sent
enter otp089
invalid otp -check your eye right
>>> 
================================================= RESTART: C:/Users/Pasupuleti/OneDrive/Desktop/internship/d10.py =================================================
enter to mailmanumanisha1999@gmail.com
mail sent
enter otp837794
The otp is valid
>>> 
================================================= RESTART: C:/Users/Pasupuleti/OneDrive/Desktop/internship/d10.py =================================================
Traceback (most recent call last):
  File "C:/Users/Pasupuleti/OneDrive/Desktop/internship/d10.py", line 52, in <module>
    otp=random.randomrange(123456,999999)
AttributeError: module 'random' has no attribute 'randomrange'. Did you mean: 'randrange'?
>>> 
================================================= RESTART: C:/Users/Pasupuleti/OneDrive/Desktop/internship/d10.py =================================================
176933
537905
