# trighomework
AI generated and then massaged program to solve trig problems

## Sample usage

The input is in the format: `a, b, c, A, B`
Where `a` is one non-hypotenuse side and `A` is the non-right angle adjacent to it.
Where `B` is one non-hypotenuse side and `B` is the non-right angle adjacent to it.
And `c` is the hypotenuse.

Note that not all arguments are required and `0` values are treated as "unknown".

### Two sides
```
$ python3 trighomework.py 
Enter the sides and angles of the right triangle in the format:
a,b,c,A (side a, side b, side c, angle A in degrees where A is one of the non-90° angles)
Enter the values: **3,4,0**


Triangle Details:
Sides: a = 3.00, b = 4.00, c = 5.00
Angles: A = 53.13°, B = 36.87°, C = 90.00° (right angle)
```

### One side, one angle
```
$ python3 trighomework.py 
Enter the sides and angles of the right triangle in the format:
a,b,c,A (side a, side b, side c, angle A in degrees where A is one of the non-90° angles)
Enter the values: **3,0,0,53.13**

Triangle Details:
Sides: a = 3.00, b = 4.00, c = 5.00
Angles: A = 53.13°, B = 36.87°, C = 90.00° (right angle)
```

### One side, hypotenuse
```
$ python3 trighomework.py 
Enter the sides and angles of the right triangle in the format:
a,b,c,A (side a, side b, side c, angle A in degrees where A is one of the non-90° angles)
Enter the values: **0,4,5**

Triangle Details:
Sides: a = 3.00, b = 4.00, c = 5.00
Angles: A = 53.13°, B = 36.87°, C = 90.00° (right angle)
```

### One side, opposite angle
```
$ python3 trighomework.py 
Enter the sides and angles of the right triangle in the format:
a,b,c,A (side a, side b, side c, angle A in degrees where A is one of the non-90° angles)
Enter the values: **0,4,0,53.13**

Triangle Details:
Sides: a = 3.00, b = 4.00, c = 5.00
Angles: A = 53.13°, B = 36.87°, C = 90.00° (right angle)

```
