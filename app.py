import streamlit as st
import pandas as pd
import preprocess
import helper
import matplotlib.pyplot as plt
import seaborn as sns

st.sidebar.title("Whatsapp Analyzer")

file_uploader=st.sidebar.file_uploader("upload chat file")
if file_uploader is not None:
    bytes_data = file_uploader.getvalue()
    data=bytes_data.decode("utf-8")
    df=preprocess.preprocessor(data)
    user_list=df['users'].unique().tolist()
    user_list.remove("group_notification")
    user_list.insert(0,"overall")
    selected_user=st.sidebar.selectbox(
        "Choose a User",user_list)
    if st.sidebar.button('Analysis'):
        st.title("Stats")
        total_msg,total_media,total_link=helper.msg_counter(selected_user,df)
        col1, col2, col3 = st.columns(3)

        with col1:
            st.header("Total Messages")
            st.header(total_msg)

        with col2:
            st.header("Media shared")
            st.header(total_media)

        with col3:
            st.header("Link shared")
            st.header(total_link)
        
        st.title("Busy Users")
        col1, col2 = st.columns(2)
        with col1:
            x,df1=helper.Busy_user(df)
            fig,ax=plt.subplots()
            ax.bar(x.index,x.values)
            plt.xticks(rotation='vertical')
            st.pyplot(fig)

        with col2:
            st.dataframe(df1)
        
        st.title("Wordcloud")
        df_wc = helper.create_wordcloud(selected_user,df)
        fig,ax = plt.subplots()
        ax.imshow(df_wc)
        st.pyplot(fig)

        # most common words
        most_common_df = helper.most_common_words(selected_user,df)

        fig,ax = plt.subplots()

        ax.barh(most_common_df[0],most_common_df[1])
        plt.xticks(rotation='vertical')

        st.title('Most commmon words')
        st.pyplot(fig)
        # emoji analysis
        emoji_df = helper.emoji_helper(selected_user,df)
        st.title("Emoji Analysis")
        col1,col2 = st.columns(2)

        with col1:
            st.dataframe(emoji_df)
        with col2:
            fig,ax = plt.subplots()
            ax.pie(emoji_df['count'].head(),labels=emoji_df['emoji'].head(),autopct="%0.2f")
            st.pyplot(fig)

        st.title("Monthly Timeline")
        timeline = helper.monthly_timeline(selected_user,df)
        fig,ax = plt.subplots()
        ax.plot(timeline['time'], timeline['messeges'],color='green')
        plt.xticks(rotation='vertical')
        st.pyplot(fig)

        st.title("Daily Timeline")
        daily_timeline = helper.daily_timeline(selected_user, df)
        fig, ax = plt.subplots()
        ax.plot(daily_timeline['only_date'], daily_timeline['messeges'], color='black')
        plt.xticks(rotation='vertical')
        st.pyplot(fig)

        st.title('Activity Map')
        col1,col2 = st.columns(2)

        with col1:
            st.header("Most busy day")
            busy_day = helper.week_activity_map(selected_user,df)
            fig,ax = plt.subplots()
            ax.bar(busy_day.index,busy_day.values,color='purple')
            plt.xticks(rotation='vertical')
            st.pyplot(fig)
        with col2:
            st.header("Most busy month")
            busy_month = helper.month_activity_map(selected_user, df)
            fig, ax = plt.subplots()
            ax.bar(busy_month.index, busy_month.values,color='orange')
            plt.xticks(rotation='vertical')
            st.pyplot(fig)

        st.title("Weekly Activity Map")
        user_heatmap = helper.activity_heatmap(selected_user,df)
        fig,ax = plt.subplots()
        ax = sns.heatmap(user_heatmap)
        st.pyplot(fig)
