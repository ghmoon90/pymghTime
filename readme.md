# GPS Time


GPS epoch starts from Jan 1, 1980 00:00:00

It is continous increasing clock

It consts of GPS Week and GPS second

GPS week is the number of weeks from 1st epoch



# UTC2KST

## input
```
UTC2KST(YYYY,MM,DD,hh,mm,ss)
```
YYYY : year ( default : 1980)

MM : month (default : 1)

DD : date (default : 6)

hh : hour (default : 0)

mm : miniute (default : 0)

ss : second (default : 0)

or u can transfer the input parameter by TIMEStr

```
UTC2KST(TIMEStr='1980.01.06_00:00:00')
```

TIMEStr : time string (default '1980.01.06_00:00:00')
