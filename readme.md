# GPS Time


GPS epoch starts from Jan 1, 1980 00:00:00

It is continous increasing clock

It consts of GPS Week and GPS second

GPS week is the number of weeks from 1st epoch



# UTC2KST

## Usage
```
UTC2KST(YYYY,MM,DD,hh,mm,ss)
UTC2KST(TIMEStr='1980.01.06_00:00:00')
UTC2KST(TIMEStr='1980.01.06_00:00:00',option='timestr')
```
YYYY : year ( default : 1980)

MM : month (default : 1)

DD : date (default : 6)

hh : hour (default : 0)

mm : miniute (default : 0)

ss : second (default : 0)

or u can transfer the input parameter by TIMEStr


TIMEStr : time string (default '1980.01.06_00:00:00')


Option : output option parameter, available cases are 'timestr' and 'default'
default returns in tuple, timestr returns in string format
