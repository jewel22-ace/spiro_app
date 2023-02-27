import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st



from Spiro_package import Spiro
Spiro=Spiro()
from Spiro_package import Spiro_feature
Spiro_feature=Spiro_feature()


st.set_page_config(page_title="Spiro App", page_icon="assest/wind.png", layout="centered"
  , initial_sidebar_state="auto", menu_items=None)
col1, mid, col2 = st.columns([1,1,20])
with col1:
    st.image('assest/wind.png', width=70)
with col2:
    st.header("Spiro App")






st.write("COPD and Asthma Detection Made Easy with Machine Learning: A Revolutionary Health Monitoring System. Our application will utilize various machine learning algorithms to analyze the patient's cough and breath sounds, along with other relevant patient history data, to accurately diagnose COPD and Asthma. The application will also have a user-friendly interface for clinicians to input patient data and view the diagnosis results.")
url = "https://github.com/jewel22-ace"
st.write("Created by [Mosaif Ali](%s)." % url)


st.header("Choose a Data File.")

uploaded_file = st.file_uploader("File Selector.")
try :
  if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    #st.line_chart(df,x='DataPoints',y='Data')
    if not df.empty:
      st.subheader('Raw Data.')
      st.line_chart(df,x='DataPoints',y='Data')
      st.metric(label="Sample Rate", value=str(Spiro.sample_rate(df['Data'].tolist())))
      st.subheader('Spiro Jobs.')
      option = st.selectbox(
    'Choose Spiro Jobs to Perform.',
    ('------', 'Filter Data', 'Extract Wavelets', 'Extract features'))
      if option == '------' :
        pass
      elif option == 'Filter Data' :
        st.subheader('Filtered Data')
        filtered_df=Spiro.filter_data(df['Data'])
        st.line_chart(filtered_df)
      elif option == 'Extract Wavelets' :
        w=Spiro.extract_wavelet(df['Data'])
        st.subheader('Extracted Wavelets.')
        col1, col2, col3, col4 ,col5 = st.columns(5)
        with col1 :
          wave1=st.checkbox("Wavelet 1.")
        with col2 :
          wave2=st.checkbox("Wavelet 2.")
        with col3 :
          wave3=st.checkbox("Wavelet 3.")
        with col4 :
          wave4=st.checkbox("Wavelet 4.")
        with col5 :
          wave5=st.checkbox("Wavelet 5.")
        
        if wave1 :
          st.caption('Wavelet 1')

          p,n=Spiro_feature.sig_continuance(w[0])

          peak=Spiro_feature.sig_consecutive_positive_peak_distance(w[0])

          peak_neg=Spiro_feature.sig_consecutive_negative_peak_distance(w[0])

          dist=Spiro_feature.sig_difference_largest_positive_peaks(w[0])

          dist_neg=Spiro_feature.sig_difference_largest_negative_peaks(w[0])

          p_p=Spiro_feature.sig_positive_plateau_sustain_time(w[0])

          p_n=Spiro_feature.sig_negative_plateau_sustain_time(w[0])

          zero=Spiro_feature.sig_zero_hitting(w[0])

          flatline=Spiro_feature.sig_flatline(w[0])

          m = {'Metrics': ['Positive_sustain', 'Negative_sustain', 'Consecutive_Positive_Peak_Distance', 
                    'Consecutive_Negative_Peak_Distance','Difference_largest_positive_peaks',
                    'Difference_largest_negative_peaks','Positive_plateau_sustain_time',
                    'Negative_plateau_sustain_time','Zero_hitting','Flatline'
                    ],
          'Value': [p,n,peak,peak_neg,dist,dist_neg,p_p,p_n,zero,flatline]}
          d = pd.DataFrame(m)
          st.dataframe(d,use_container_width=True)

          st.line_chart(w[0])
        if wave2 :
          st.caption('Wavelet 2')

          p,n=Spiro_feature.sig_continuance(w[1])

          peak=Spiro_feature.sig_consecutive_positive_peak_distance(w[1])

          peak_neg=Spiro_feature.sig_consecutive_negative_peak_distance(w[1])

          dist=Spiro_feature.sig_difference_largest_positive_peaks(w[1])

          dist_neg=Spiro_feature.sig_difference_largest_negative_peaks(w[1])

          p_p=Spiro_feature.sig_positive_plateau_sustain_time(w[1])

          p_n=Spiro_feature.sig_negative_plateau_sustain_time(w[1])

          zero=Spiro_feature.sig_zero_hitting(w[1])

          flatline=Spiro_feature.sig_flatline(w[1])

          m = {'Metrics': ['Positive_sustain', 'Negative_sustain', 'Consecutive_Positive_Peak_Distance', 
                    'Consecutive_Negative_Peak_Distance','Difference_largest_positive_peaks',
                    'Difference_largest_negative_peaks','Positive_plateau_sustain_time',
                    'Negative_plateau_sustain_time','Zero_hitting','Flatline'
                    ],
          'Value': [p,n,peak,peak_neg,dist,dist_neg,p_p,p_n,zero,flatline]}
          d = pd.DataFrame(m)
          st.dataframe(d,use_container_width=True)

          st.line_chart(w[1])
        if wave3 :
          st.caption('Wavelet 3')

          p,n=Spiro_feature.sig_continuance(w[2])

          peak=Spiro_feature.sig_consecutive_positive_peak_distance(w[2])

          peak_neg=Spiro_feature.sig_consecutive_negative_peak_distance(w[2])

          dist=Spiro_feature.sig_difference_largest_positive_peaks(w[2])

          dist_neg=Spiro_feature.sig_difference_largest_negative_peaks(w[2])

          p_p=Spiro_feature.sig_positive_plateau_sustain_time(w[2])

          p_n=Spiro_feature.sig_negative_plateau_sustain_time(w[2])

          zero=Spiro_feature.sig_zero_hitting(w[2])

          flatline=Spiro_feature.sig_flatline(w[2])

          m = {'Metrics': ['Positive_sustain', 'Negative_sustain', 'Consecutive_Positive_Peak_Distance', 
                    'Consecutive_Negative_Peak_Distance','Difference_largest_positive_peaks',
                    'Difference_largest_negative_peaks','Positive_plateau_sustain_time',
                    'Negative_plateau_sustain_time','Zero_hitting','Flatline'
                    ],
          'Value': [p,n,peak,peak_neg,dist,dist_neg,p_p,p_n,zero,flatline]}
          d = pd.DataFrame(m)
          st.dataframe(d,use_container_width=True)

          st.line_chart(w[2])
        if wave4 :
          st.caption('Wavelet 4')

          p,n=Spiro_feature.sig_continuance(w[3])

          peak=Spiro_feature.sig_consecutive_positive_peak_distance(w[3])

          peak_neg=Spiro_feature.sig_consecutive_negative_peak_distance(w[3])

          dist=Spiro_feature.sig_difference_largest_positive_peaks(w[3])

          dist_neg=Spiro_feature.sig_difference_largest_negative_peaks(w[3])

          p_p=Spiro_feature.sig_positive_plateau_sustain_time(w[3])

          p_n=Spiro_feature.sig_negative_plateau_sustain_time(w[3])

          zero=Spiro_feature.sig_zero_hitting(w[3])

          flatline=Spiro_feature.sig_flatline(w[3])

          m = {'Metrics': ['Positive_sustain', 'Negative_sustain', 'Consecutive_Positive_Peak_Distance', 
                    'Consecutive_Negative_Peak_Distance','Difference_largest_positive_peaks',
                    'Difference_largest_negative_peaks','Positive_plateau_sustain_time',
                    'Negative_plateau_sustain_time','Zero_hitting','Flatline'
                    ],
          'Value': [p,n,peak,peak_neg,dist,dist_neg,p_p,p_n,zero,flatline]}
          d = pd.DataFrame(m)
          st.dataframe(d,use_container_width=True)

          st.line_chart(w[3])
        if wave5 :
          st.caption('Wavelet 5')

          p,n=Spiro_feature.sig_continuance(w[4])

          peak=Spiro_feature.sig_consecutive_positive_peak_distance(w[4])

          peak_neg=Spiro_feature.sig_consecutive_negative_peak_distance(w[4])

          dist=Spiro_feature.sig_difference_largest_positive_peaks(w[4])

          dist_neg=Spiro_feature.sig_difference_largest_negative_peaks(w[4])

          p_p=Spiro_feature.sig_positive_plateau_sustain_time(w[4])

          p_n=Spiro_feature.sig_negative_plateau_sustain_time(w[4])

          zero=Spiro_feature.sig_zero_hitting(w[4])

          flatline=Spiro_feature.sig_flatline(w[4])

          m = {'Metrics': ['Positive_sustain', 'Negative_sustain', 'Consecutive_Positive_Peak_Distance', 
                    'Consecutive_Negative_Peak_Distance','Difference_largest_positive_peaks',
                    'Difference_largest_negative_peaks','Positive_plateau_sustain_time',
                    'Negative_plateau_sustain_time','Zero_hitting','Flatline'
                    ],
          'Value': [p,n,peak,peak_neg,dist,dist_neg,p_p,p_n,zero,flatline]}
          d = pd.DataFrame(m)
          st.dataframe(d,use_container_width=True)

          st.line_chart(w[4])

      elif option == 'Extract features' :
        pass



except Exception as e :
  st.error(str(e))




  