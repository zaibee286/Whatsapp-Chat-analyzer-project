import re
import  pandas as pd
def preprocessor(data):
    data=data.replace("\u202fAM"," AM").replace('\u202fPM',' PM')
    pattern='\d{1,2}\/\d{1,2}\/\d{1,2}, \d{1,2}\:\d{1,2} [A-Z]{1,2} \- '
    date=re.findall(pattern,data)
    msg=re.split(pattern,data)[1:]
    df=pd.DataFrame({
    "date":date,
    "msg":msg})
    df['date']=df['date'].str.split('-').str.get(0)
    users=[]
    messeges=[]
    for msg in df['msg']:
        entry=re.split('([\w\W]+?):\s',msg)
        if entry[1:]:
            users.append(entry[1])
            messeges.append(entry[2])
        else:
            users.append("group_notification")
            messeges.append(entry[0])

    df['users']=users
    df['messeges']=messeges
    df.drop(columns='msg',inplace=True)
    df['date']=pd.to_datetime(df['date'].str.strip(),format="%m/%d/%y, %I:%M %p")
    df['messeges']=df['messeges'].str.replace('\n','')
    df['messeges'][df['messeges']=='<Media omitted>']='@media_shared'
    df['messeges'][df['messeges'].str.contains('www.')]='@link_shared'
    df['year']=df['date'].dt.year
    df['month']=df['date'].dt.month
    df['day']=df['date'].dt.day
    df['month_name']=df['date'].dt.month_name()
    df['only_date']=df['date'].dt.date
    df['day_name']=df['date'].dt.day_name()
    df['hour'] = df['date'].dt.hour
    df['minute'] = df['date'].dt.minute
    period = []
    for hour in df[['day_name', 'hour']]['hour']:
        if hour == 23:
            period.append(str(hour) + "-" + str('00'))
        elif hour == 0:
            period.append(str('00') + "-" + str(hour + 1))
        else:
            period.append(str(hour) + "-" + str(hour + 1))

    df['period'] = period

    return df