# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import streamlit as st


add_sidebar= st.sidebar.selectbox('Category',('Profile','Education','Work experience','References'))
if add_sidebar=='Profile':
    st.write('Hello world!')
    st.header('Click this button')
    if st.button('Say Hello'):
        st.write('I am an aspiring Accounting and Finance professional with a Bachelor of Commerce (Finance) degree and ACCA certification. My academic background and professional qualifications have equipped me with strong financial analysis, accounting, and problem solving skills')
        st.write('Currently, I am gaining hands-on experience as an Investment Trainee at ASIGMA, where I assist with financial modelling, and market research. This role has further enhanced my understanding of the investment decisions, and data-driven decision-making processes.')
    else:
        st.write('I am not human')
if add_sidebar=='Education':
    col1,col2,col3= st.columns(3)
    with col1:
        st.markdown('**Year**')
    with col2:
        st.markdown('**School**')
    with col3:
        st.markdown('**Course**')
    with col1:
        st.write('2020 to 2024')
    with col2:
        st.write('Strathmore University')
    with col3:
        st.write('Bachelor of Commerce')
    with col1:
        st.write('2013-2018')
    with col2:
        st.write('Gayaza High School')
    with col3: 
        st.write('High School-Ordinary and Advanced Level')
if add_sidebar=='Work experience':
    col1,col2,col3=st.columns(3)
    with col1:
        st.markdown('**Year**')
    with col2:
        st.markdown('**Position**')
    with col3:
        st.markdown('**Institution**')
    with col1:
        st.write('August 2024-Present')
    with col2:
        st.write('Investment Trainee')
    with col3:
        st.write('ASIGMA')
    with col1:
        st.write('May 2024-July 2024')
    with col2:
        st.write('Finance Intern')
    with col3:
        st.write('ALTX East Africa')
    with col1:
        st.write('January 2023-March 2023')
    with col2:
        st.write('Accounting Intern')
    with col3:
        st.write('Equity Bank Uganda Limited')
    with col1:
        st.write('February 2021-March 2021')
    with col2:
        st.write('Volunteer')
    with col3:
        st.write('Dorna Centre for Autism, Uganda')
if add_sidebar=='References':
    col1,col2=st.columns(2)
    with col1:
        st.write('Ms. Kezia Asiimwe')
        st.write('Head of Finance')
        st.write('Equity Bank Uganda Limited')
        st.write('Email: kezia.asiimwe@equitybank.co.ug')
    with col2:
        st.write('Mrs Angelikka Gitau')
        st.write('Mentor')
        st.write('Strathmore University')
        st.write('Email:agitau@strathmore.edu')



        
    