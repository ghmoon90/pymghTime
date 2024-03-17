import numpy as np

########################################################################################

def isLeap (year):

    f_Leap = False
    if (year % 4 == 0):
        f_Leap = True
        if(year %100 == 0):
            f_Leap = False
            if(year%400 == 0):
                f_Leap = True
    
    return f_Leap
    
########################################################################################    
# UTC2KST(2024,3,17,12,00,30)
def UTC2KST(YYYY=1980,MM=1,DD=6,hh=0,mm=0,ss=0,TIMEStr='None',option='default'):



    
    if ( (TIMEStr) != 'None'):
        # format 1980.1.6_00:00:00
        print(TIMEStr)
        Temp = TIMEStr.split('_')
        YearMonDay = Temp[0]
        hhmmss = Temp[1]
        Temp1 = YearMonDay.split('.')
        Temp2 = hhmmss.split(':')
        YYYY =  int(Temp1[0])
        MM = int(Temp1[1])
        DD = int(Temp1[2])
        hh = int(Temp2[0])
        mm = int(Temp2[1])
        ss = int(Temp2[2])    

    
    if ((hh >=  24) | (hh< 0 )):
        print('hh should in [0,23]') 
        return -1
    if ((mm >= 60) |( mm < 0 )):
        print('mm should in [0, 59]')
    if ((ss >= 60 )|( ss < 0)) :
        print('ss should in [0, 59]')    
    
    hh = hh + 9
    mm = mm
    ss = ss
    
    YYYY,MM,DD,hh,mm,ss= refine_Clock(YYYY,MM,DD,hh,mm,ss)
    
    if option == 'default':
        return YYYY,MM,DD,hh,mm,ss
    elif option == 'timestr':
        return f'{YYYY:4.0f}.{MM:02.0f}.{DD:02.0f}_{hh:02.0f}:{mm:02.0f}:{ss:02.0f}'

########################################################################################
    
def refine_Clock(YYYY,MM,DD,hh,mm,ss):

    f_Leap = isLeap(YYYY)

    if hh>24.0:
        hh = hh -24
        DD = DD+1
        
    conA = (MM == 2) & (( (DD==30) & f_Leap )|((DD==29) & -f_Leap))
    conB = (DD == 32) & (MM in set([1,3,5,7,8,10,12]))
    conC = (DD == 31) & (MM in set([4,6,9,11]))
    
    if (conA | conB | conC):
        MM = MM+1
        DD = 1
    
    if MM > 12:
        YYYY = YYYY+1
        MM = 1
    
    return YYYY,MM,DD,hh,mm,ss
    
########################################################################################

def GPST2UTC(GPSWeek=0,GPSSec=0,option='default'):
    
    #GPS epoch initiation on 1980.1.6 00:00:00
    GPSDay = ((GPSWeek) * 7 )+6 + np.floor( GPSSec / (3600 * 24) )
    YYYY   = 1980
    f_Leap = isLeap(YYYY)
    
    while ((( GPSDay > 366 ) & f_Leap ) | (( GPSDay > 365 ) & ( not f_Leap ) )):    
        
        if f_Leap :
            GPSDay = GPSDay - 366
        else:
            GPSDay = GPSDay - 365
        
        YYYY = YYYY+1       
        f_Leap = isLeap(YYYY)
    
    MM = 1
    if f_Leap :
        MonSet = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]        
    else :
        MonSet = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    while ( (GPSDay > MonSet[MM-1]) ):
        #print(MM)
        #print(GPSDay)
        GPSDay = GPSDay - MonSet[MM-1]
        MM = MM+1
        if MM>12:
            break;
        
    DD = GPSDay
    
    
    hh = np.floor( ( GPSSec % (3600 * 24) ) / 3600 )     
    mm = np.floor( ( GPSSec % (3600) ) / 60 )    
    ss = np.floor( GPSSec % (60) )
        
    
    if option == 'default':
        return YYYY,MM,DD,hh,mm,ss
    elif option == 'timestr':
        return f'{YYYY:4.0f}.{MM:02.0f}.{DD:02.0f}_{hh:02.0f}:{mm:02.0f}:{ss:02.0f}'

