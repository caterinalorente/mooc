'''
http://spark-public.s3.amazonaws.com/programming1/a1/a1.html

A1 Problem Domain: Coordinated Universal Time

The problem domain for this assignment involves time zones, and in particular Coordinated Universal Time (UTC), 
which is "the primary time standard by which the world regulates clocks and time" [Wikipedia]. 
As you know, there are many different time zones in the world. Wikipedia has a nice map of the time zones.

As of this writing, there are 40 time zones. One of them, UTC+00:00, is considered to be in the "middle" 
of the other time zones. All time zones have names, such as UTC+02:00, that indicate the number of hours 
and minutes they are away from UTC+00:00. For example, the Philippines are in time zone UTC+08:00 because 
clocks there are set 8 hours later than in time zone UTC+00:00. If it's noon in time zone UTC+00:00, 
it's 20:00 in time zone UTC+08:00. 

Hours and minutes: representation

In this assignment, we are often going to represent hours and minutes and seconds together as a float. 
1 hour will be represented as 1.0, 1 hour and 30 minutes as 1.5, and so on. 
Henceforth, when we specify a time zone, we will use this float representation, so the time zone for Nepal, 
which is in time zone UTC+05:45, will be represented here as UTC+5.75.

Preconditions

Some of the functions you will write assume that parameter values are in a certain range. 
The technical term for these restrictions is precondition: in order for the function to work, the precondition 
must be met. A precondition is a warning to whoever calls the function that the function was designed to work
only under those conditions. When you see a precondition, that means we are guaranteeing that we will only call 
that function with values that meet the precondition. You can assume that the parameter values meet the 
preconditions, you do not need to check them. The preconditions are there to make your lives easier!
'''

def seconds_difference(time_1, time_2):
    '''(float, float) -> float

    Return the number of seconds later that a time in seconds
    time_2 is than a time in seconds time_1.
        
    >>> seconds_difference(1800.0, 3600.0)
    1800.0
    >>> seconds_difference(3600.0, 1800.0)
    -1800.0
    >>> seconds_difference(1800.0, 2160.0)
    360.0
    >>> seconds_difference(1800.0, 1800.0)
    0.0
    '''
    
    secondsDifference = time_2 - time_1
    return (secondsDifference)
    
def hours_difference(time_1, time_2):
    '''(float, float) -> float

    Return the number of hours later that a time in seconds
    time_2 is than a time in seconds time_1.
        
    >>> hours_difference(1800.0, 3600.0)
    0.5
    >>> hours_difference(3600.0, 1800.0)
    -0.5
    >>> hours_difference(1800.0, 2160.0)
    0.1
    >>> hours_difference(1800.0, 1800.0)
    0.0
    '''
    
    time_2 = time_2 / 3600
    time_1 = time_1 / 3600
    hoursDifference = time_2 - time_1
    
    return (hoursDifference)

def to_float_hours(hours, minutes, seconds):
    '''(int, int, int) -> float

   Return the total number of hours in the specified number
   of hours, minutes, and seconds.
   
   Precondition: 0 <= minutes < 60  and  0 <= seconds < 60
   
   >>> to_float_hours(0, 15, 0)
   0.25
   >>> to_float_hours(2, 45, 9)
   2.7525
   >>> to_float_hours(1, 0, 36)
   1.01
   '''
    
    minutes = minutes / 60.0
    seconds = seconds / 3600.0
    hours = hours + minutes + seconds
    
    return (hours)
    
def to_24_hour_clock(hours):
    '''(number) -> number
    
    hours is a number of hours since midnight. Return the
    hour as seen on a 24-hour clock.

    Precondition: hours >= 0

    >>> to_24_hour_clock(24)
    0
    >>> to_24_hour_clock(48)
    0
    >>> to_24_hour_clock(25)
    1
    >>> to_24_hour_clock(4)
    4
    >>> to_24_hour_clock(28.5)
    4.5
    '''

    return hours % 24

def get_hours(time):
    '''
    (int) -> int
    
    The parameter is a number of seconds since midnight. 
    Return the number of hours that have elapsed since midnight, as seen on a 24-hour clock. 
    (You should call to_24_hour_clock to convert the number of full hours to a time on a 24 hour clock. 
    This means that the return value should be in the range 0 to 23, inclusive.) 
    
    >>> get_hours(3800)
    1
    '''
    hours = time // 3600
    return (hours)

def get_minutes(time):
    '''
    (int) -> int
    
    The parameter is a number of seconds since midnight. 
    Return the number of minutes that have elapsed since midnight, as seen on a 24-hour clock. 
    (You should call to_24_hour_clock to convert the number of full minutes to a time on a 24 hour clock. 
    This means that the return value should be in the range 0 to 59, inclusive.) 
    
    >>> get_minutes(3800)
    3
    '''    
    
    minutes = (time % 3600) // 60
    return (minutes)

def get_seconds(time):
    '''
    (int) -> int
    
    The parameter is a number of seconds since midnight. 
    Return the number of seconds that have elapsed since midnight, as seen on a 24-hour clock. 
    (You should call to_24_hour_clock to convert the number of full seconds to a time on a 24 hour clock. 
    This means that the return value should be in the range 0 to 59, inclusive.) 
    
    >>> get_seconds(3800)
    20
    ''' 
    
    seconds = (time % 3600) % 60
    return (seconds)

def time_to_utc(utc_offset, time):
    '''(number, float) -> float

    Return time at UTC+0, where utc_offset is the number of hours away from
    UTC+0.

    >>> time_to_utc(+0, 12.0)
    12.0
    >>> time_to_utc(+1, 12.0)
    11.0
    >>> time_to_utc(-1, 12.0)
    13.0
    >>> time_to_utc(-11, 18.0)
    5.0
    >>> time_to_utc(-1, 0.0)
    1.0
    >>> time_to_utc(-1, 23.0)
    0.0
    '''
    
    utcTime = time - utc_offset
    utcTimeParsed = to_24_hour_clock(utcTime)
    
    return(utcTimeParsed)

def time_from_utc(utc_offset, time):
    '''(number, float) -> float

    Return UTC time in time zone utc_offset.

    >>> time_from_utc(+0, 12.0)
    12.0
    >>> time_from_utc(+1, 12.0)
    13.0
    >>> time_from_utc(-1, 12.0)
    11.0
    >>> time_from_utc(+6, 6.0)
    12.0
    >>> time_from_utc(-7, 6.0)
    23.0
    >>> time_from_utc(-1, 0.0)
    23.0
    >>> time_from_utc(-1, 23.0)
    22.0
    >>> time_from_utc(+1, 23.0)
    0.0
    '''
    
    time = time + utc_offset
    timeParsed = to_24_hour_clock(time)
    
    return(timeParsed)


"""
For Python 2
def test_get_seconds():
    print "3800", get_seconds(3800)
    print "less than 60", get_seconds(43)
    print "greater than 60", get_seconds(121)

def test_get_minutes():
    print "3800", get_minutes(3800)
    print "seconds zero", get_minutes(0)
    print "seconds on minute", get_minutes(60)
    print "just after minute", get_minutes(61)
    print "just before minute", get_minutes(59)
    
def test_get_hours():
    print "3800", get_hours(3800)
    print "just after hour", get_hours(3601)
    print "just before hour", get_hours(3599)
    
test_get_hours()
test_get_minutes()
test_get_seconds()
"""