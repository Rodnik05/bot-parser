from datetime import datetime
def turn_into_date(dates: tuple)->tuple[datetime]:
    if(len(dates)==1):
        if(dates[0][0] == 'До'):
            if(dates[0][2]>8):
                return datetime(*(tuple([1, 1, 1]))), \
                datetime(*(tuple([2021, dates[0][2],dates[0][1]])))
            else:
                return datetime(*(tuple([1, 1, 1]))), \
                    datetime(*(tuple([2022, dates[0][2],dates[0][1]])))
        else:
            #10 дек (10, 12)
            if(dates[0][1]>8):
                return datetime(*(tuple([2021, dates[0][1],dates[0][0]]))), \
                datetime(*(tuple([2021, dates[0][1],dates[0][0]])))
            else:
                return datetime(*(tuple([2022, dates[0][1],dates[0][0]]))),\
                datetime(*(tuple([2021, dates[0][1],dates[0][0]])))
    else:
        #finish it
        if(dates[0][1]>8 and dates[1][1]>8):
                return datetime(*(tuple([2021, dates[0][1],dates[0][0]]))), \
                    datetime(*(tuple([2021, dates[1][1],dates[1][0]])))
        elif(dates[0][1]>8 and dates[1][1]<=8):
                return datetime(*(tuple([2021, dates[0][1],dates[0][0]]))), \
                    datetime(*(tuple([2022, dates[1][1],dates[1][0]])))
        elif(dates[0][1]<=8 and dates[1][1]<=8):
                return datetime(*(tuple([2022, dates[0][1],dates[0][0]]))), \
                    datetime(*(tuple([2022, dates[1][1],dates[1][0]])))

date = ((4, 12), (12, 12))
print(turn_into_date(date))
