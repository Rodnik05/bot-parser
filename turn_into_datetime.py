from datetime import datetime
def turn_into_datetime(dates: tuple)->tuple[datetime]:
    if(len(dates)==1):
        if(dates[0][0] == 'До'):
            #('До',12, 10)
            if(dates[0][2]>8):
                return datetime(*(tuple([1, 1, 1]))), \
                datetime(*(tuple([2021, dates[0][2],dates[0][1]])))
            #('До', 12, 1)
            else:
                return datetime(*(tuple([1, 1, 1]))), \
                    datetime(*(tuple([2022, dates[0][2],dates[0][1]])))
        else:
            #(10, 12)
            if(dates[0][1]>8):
                return datetime(*(tuple([2021, dates[0][1],dates[0][0]]))), \
                datetime(*(tuple([2021, dates[0][1],dates[0][0]])))
            #(12, 1)
            else:
                return datetime(*(tuple([2022, dates[0][1],dates[0][0]]))),\
                datetime(*(tuple([2021, dates[0][1],dates[0][0]])))
    else:
        #((12,1),(12,2))
        if(dates[0][1]>8 and dates[1][1]>8):
                return datetime(*(tuple([2021, dates[0][1],dates[0][0]]))), \
                    datetime(*(tuple([2021, dates[1][1],dates[1][0]])))
        #((12,10),(12,1))
        elif(dates[0][1]>8 and dates[1][1]<=8):
                return datetime(*(tuple([2021, dates[0][1],dates[0][0]]))), \
                    datetime(*(tuple([2022, dates[1][1],dates[1][0]])))
        #((12,11),(12,12))
        elif(dates[0][1]<=8 and dates[1][1]<=8):
                return datetime(*(tuple([2022, dates[0][1],dates[0][0]]))), \
                    datetime(*(tuple([2022, dates[1][1],dates[1][0]])))
