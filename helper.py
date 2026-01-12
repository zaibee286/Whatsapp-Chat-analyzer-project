from wordcloud import WordCloud
import pandas as pd
from collections import Counter
import emoji

def msg_counter(selected_user,df):
    if selected_user!='overall':
        df=df[df['users']==selected_user]
    total_msg=len(df)
    total_media=len(df[df['messeges']=='@media_file'])
    total_link=len(df[df['messeges']=='@link_shared'])

    return total_msg,total_media,total_link
def Busy_user(df):
    x=df['users'][df['users']!='group_notification'].value_counts().head()
    df1=df['users'][df['users']!='group_notification'].value_counts().head().reset_index()
    return x,df1

def create_wordcloud(selected_user,df):

    f = open('stop_hinglish.txt', 'r')
    stop_words = f.read()

    if selected_user != 'overall':
        df = df[df['users'] == selected_user]
    def remove_stop_words(message):
        y = []
        for word in message.lower().split():
            if word not in stop_words:
                y.append(word)
        return " ".join(y)
    wc = WordCloud(width=500,height=500,min_font_size=10,background_color='white')
    df['message'] = df['messeges'].apply(remove_stop_words)
    df_wc = wc.generate(df['messeges'].str.cat(sep=" "))
    return df_wc

def most_common_words(selected_user,df):

    f = open('stop_hinglish.txt','r')
    stop_words = f.read()

    if selected_user != 'overall':
        df = df[df['users'] == selected_user]

    

    words = []

    for message in df['messeges']:
        for word in message.lower().split():
            if word not in stop_words:
                words.append(word)

    most_common_df = pd.DataFrame(Counter(words).most_common(20))
    return most_common_df


def emoji_helper(selected_user, df):
    if selected_user != 'overall':
        df = df[df['users'] == selected_user]

    emojis = []

    for message in df['messeges'].dropna():
        emojis.extend([c for c in message if emoji.is_emoji(c)])

    emoji_df = pd.DataFrame(
        Counter(emojis).most_common(),
        columns=['emoji', 'count']
    )

    return emoji_df.head(10)

def monthly_timeline(selected_user,df):

    if selected_user != 'overall':
        df = df[df['users'] == selected_user]

    timeline = df.groupby(['year', 'month_name', 'month'])['messeges'].count().reset_index()
    
    time = []
    for i in range(timeline.shape[0]):
        time.append(str(timeline['month'][i]) + "-" + str(timeline['year'][i]))

    timeline['time'] = time

    return timeline

def daily_timeline(selected_user,df):

    if selected_user != 'overall':
        df = df[df['users'] == selected_user]

    daily_timeline = df.groupby('only_date').count()['messeges'].reset_index()

    return daily_timeline

def week_activity_map(selected_user,df):

    if selected_user != 'overall':
        df = df[df['users'] == selected_user]

    return df['day_name'].value_counts()
def week_activity_map(selected_user,df):

    if selected_user != 'overall':
        df = df[df['users'] == selected_user]
    return df['day_name'].value_counts()
def month_activity_map(selected_user,df):

    if selected_user != 'overall':
        df = df[df['users'] == selected_user]

    return df['month'].value_counts()
def activity_heatmap(selected_user,df):

    if selected_user != 'overall':
        df = df[df['users'] == selected_user]

    user_heatmap = df.pivot_table(index='day_name', columns='period', values='messeges', aggfunc='count').fillna(0)

    return user_heatmap
