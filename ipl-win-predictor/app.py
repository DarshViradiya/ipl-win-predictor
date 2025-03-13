import streamlit as st
import pickle
import pandas as pd

teams=['Royal Challengers Bangalore', 'Kings XI Punjab', 'Delhi Capitals',
       'Mumbai Indians', 'Kolkata Knight Riders', 'Rajasthan Royals',
       'Sunrisers Hyderabad', 'Chennai Super Kings',
       'Lucknow Super Giants', 'Gujarat Titans']

cities=['Bangalore', 'Chandigarh', 'Delhi', 'Mumbai', 'Kolkata', 'Jaipur',
       'Hyderabad', 'Chennai', 'Cape Town', 'Port Elizabeth', 'Durban',
       'Centurion', 'East London', 'Johannesburg', 'Kimberley',
       'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
       'Kochi', 'Indore', 'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi',
       'Abu Dhabi', 'Rajkot', 'Kanpur', 'Bengaluru', 'Dubai',
       'Sharjah', 'Navi Mumbai', 'Lucknow', 'Guwahati', 'Mohali']

pipe=pickle.load(open('pipe.pkl', 'rb'))

st.title('IPL Win Predictor')

col1,col2=st.columns(2)
with col1:
    batting_team=st.selectbox('Select the Batting team', sorted(teams))
with col2:
    bowling_team=st.selectbox('Select the Bowling team', sorted(teams))

selected_city=st.selectbox('Select the Host City', sorted(cities))

target=st.number_input('Target')

col3,col4,col5,col6=st.columns(4)

with col3:
       score=st.number_input('Score of Batting Team')
with col4:
       overs=st.number_input('Number of Overs Completed')
with col5:
       balls=st.number_input('Number of Balls in the Over Completed')
with col6:
       wickets=st.number_input('Wickets Fallen')

if st.button('Predict Probability'):
       runs_left=target-score
       balls_left=120-(overs*6+balls)
       wickets_left=10-wickets
       crr=score*6/(6*overs+balls)
       rrr=runs_left*6/balls_left

       input_df=pd.DataFrame({'batting_team':[batting_team],'bowling_team':[bowling_team],'city':[selected_city],'runs_left':[runs_left],'balls_left':[balls_left],'wickets_left':[wickets_left],'target':[target],'crr':[crr],'rrr':[rrr]},)

       result=pipe.predict_proba(input_df)
       loss=result[0][0]
       win=result[0][1]
       st.header(batting_team+"-"+str(round(win*100))+"%")
       st.header(bowling_team + "-" + str(round(loss * 100)) + "%")