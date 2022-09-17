import streamlit as st
import pandas as pd
import seaborn as sns 
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score

# make container 
header = st.container()
datasets = st.container()
features = st.container()
model_trainings = st.container()

with header:
    st.title("Kashti ki app")
    st.text("In this Project we will work on kashti dataset")

with datasets:
    st.header("Kashti doob gaye")
    st.text("In this Project we will work on kashti dataset")
    # import dataset
    df = sns.load_dataset('titanic')
    df = df.dropna()
    st.write(df.head(10))
    st.subheader("Arey ooh Sambha kitna admi they !!!")
    st.bar_chart(df['sex'].value_counts())

    # other plot
    st.subheader("Meri class Meri Marzi")
    st.bar_chart(df['class'].value_counts())

with features:
    st.header("These are our app features")
    st.text("In this Project we have lot of Features")
    st.markdown('1. **Feature 1.** Dont stare on Girls')
    st.markdown('2. **Feature 2.** Dont stare on Girls')
    st.markdown('3. **Feature 3.** Dont stare on Girls')
 
with model_trainings:
    st.header("Kashti walo ka kya bane ga ")        
    st.text("In this Project we will train our model")
#    making colunmns 
    input, display = st.columns(2)

    #  phela col selcertion points
    maximium_depth = input.slider("How many people do you know?", min_value=10 , max_value=100,value=20, step=5)

    #  n estimators
    estimators =  input.selectbox("How many tree should be there in  a RF? ",options=[50,100,200,300,'NO limit'])

    #  adding list of featiures
    input.write(df.columns)

    # inut features from user
    input_features = input.text_input('which feature w should use??')


#   Machine learning Model
    model = RandomForestRegressor(max_depth=maximium_depth,n_estimators=estimators)
    # condition for No limit
if estimators == 'NO limit':
    model = RandomForestRegressor(max_depth=maximium_depth)
else:
    model = RandomForestRegressor(max_depth=maximium_depth,n_estimators=estimators)    

#   Define X and Y 
x = df[[input_features]]
y = df[['fare']]

# fit our model
model.fit(x,y)
pred = model.predict(y)

#  Display Metrics
display.subheader("Mean absolute error of the model is: ")
display.write(mean_absolute_error(y,pred))
display.subheader("Mean Squared error of the model is: ")
display.write(mean_squared_error(y,pred))
display.subheader("R Score  of the model is: ")
display.write(r2_score(y,pred))