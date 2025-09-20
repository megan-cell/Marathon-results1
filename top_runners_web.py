
import streamlit as st
import pandas as pd

df = pd.read_excel('top 100.xlsx', sheet_name='Sheet1', engine='openpyxl')
wdf = pd.read_excel('top 100 w.xlsx', sheet_name='Sheet1', engine='openpyxl')
st.title("Marathon Results Explorer")

gender = st.radio("Select gender:", ['Male', 'Female'])
if gender == 'Male':
    option = st.selectbox(
        "Choose an action:",
        [
            "Show top runners",
            "Show top runners with only their fastest results",
            "Filter by country with all performances",
            "Filter by country with top performance",
            "Top runners at specific courses",
            "Top performance by a runner"
        ]
    )

    if option == "Show top runners":
        top_n = st.number_input("How many top results would you like to see?", min_value=1, max_value=len(df), value=10)
        df_ranked = df[['Name', 'Time']].head(top_n).copy()
        df_ranked.insert(0, 'Rank', range(1, len(df_ranked) + 1))
        st.dataframe(df_ranked)

    elif option == "Show top runners with only their fastest results":
        filtered_df = df.drop_duplicates(subset='Name')
        top_n = st.number_input("How many top runners with only their fastest results?", min_value=1, max_value=len(filtered_df), value=10)
        df_ranked = filtered_df[['Name', 'Time']].head(top_n).copy()
        df_ranked.insert(0, 'Rank', range(1, len(df_ranked) + 1))
        st.dataframe(df_ranked)

    elif option == "Filter by country with all performances":
        country = st.text_input("Enter country code (e.g., GBR):")
        if country:
            filtered_df = df[df['Country'] == country][['Name', 'Time']].copy()
            filtered_df.insert(0, 'Rank', range(1, len(filtered_df) + 1))
            st.dataframe(filtered_df)

    elif option == "Filter by country with top performance":
        filtered_df = df.drop_duplicates(subset='Name')
        country = st.text_input("Enter country code (e.g., GBR):")
        if country:
            filtered_df = filtered_df[filtered_df['Country'] == country][['Name', 'Time']].copy()
            filtered_df.insert(0, 'Rank', range(1, len(filtered_df) + 1))
            st.dataframe(filtered_df)

    elif option == "Top runners at specific courses":
        course = st.text_input("Enter course name (e.g., London):")
        top_n = st.number_input("How many top runners at this course?", min_value=1, max_value=len(df), value=10)
        if course:
            filtered_df = df[df['Course'] == course][['Name', 'Time']].head(top_n).copy()
            filtered_df.insert(0, 'Rank', range(1, len(filtered_df) + 1))
            st.dataframe(filtered_df)

    elif option == "Top performance by a runner":
        name = st.text_input("Enter runner's full name (e.g., Eliud Kipchoge):")
        if name:
            filtered_df = df[df['Name'] == name][['Name', 'Time', 'Course', 'Date']].copy()
            filtered_df.insert(0, 'Rank', range(1, len(filtered_df) + 1))
            st.dataframe(filtered_df)
elif gender == 'Female':
    option = st.selectbox(
        "Choose an action:",
        [
            "Show top runners",
            "Show top runners with only their fastest results",
            "Filter by country with all performances",
            "Filter by country with top performance",
            "Top runners at specific courses",
            "Top performance by a runner"
        ]
    )

    if option == "Show top runners":
        top_n = st.number_input("How many top results would you like to see?", min_value=1, max_value=len(wdf), value=10)
        wdf_ranked = wdf[['Name', 'Time']].head(top_n).copy()
        wdf_ranked.insert(0, 'Rank', range(1, len(wdf_ranked) + 1))
        st.dataframe(wdf_ranked)

    elif option == "Show top runners with only their fastest results":
        filtered_df = wdf.drop_duplicates(subset='Name')
        top_n = st.number_input("How many top runners with only their fastest results?", min_value=1, max_value=len(filtered_df), value=10)
        wdf_ranked = filtered_df[['Name', 'Time']].head(top_n).copy()
        wdf_ranked.insert(0, 'Rank', range(1, len(wdf_ranked) + 1))
        st.dataframe(wdf_ranked)

    elif option == "Filter by country with all performances":
        country = st.text_input("Enter country code (e.g., GBR):")
        if country:
            filtered_df = wdf[wdf['Country'] == country][['Name', 'Time']].copy()
            filtered_df.insert(0, 'Rank', range(1, len(filtered_df) + 1))
            st.dataframe(filtered_df)

    elif option == "Filter by country with top performance":
        filtered_df = wdf.drop_duplicates(subset='Name')
        country = st.text_input("Enter country code (e.g., GBR):")
        if country:
            filtered_df = filtered_df[filtered_df['Country'] == country][['Name', 'Time']].copy()
            filtered_df.insert(0, 'Rank', range(1, len(filtered_df) + 1))
            st.dataframe(filtered_df)

    elif option == "Top runners at specific courses":
        course = st.text_input("Enter course name (e.g., London):")
        top_n = st.number_input("How many top runners at this course?", min_value=1, max_value=len(wdf), value=10)
        if course:
            filtered_df = wdf[wdf['Course'] == course][['Name', 'Time']].head(top_n).copy()
            filtered_df.insert(0, 'Rank', range(1, len(filtered_df) + 1))
            st.dataframe(filtered_df)

    elif option == "Top performance by a runner":
        name = st.text_input("Enter runner's full name (e.g., Paula Radcliffe):")
        if name:
            filtered_df = wdf[wdf['Name'] == name][['Name', 'Time', 'Course', 'Date']].copy()
            filtered_df.insert(0, 'Rank', range(1, len(filtered_df) + 1))
            st.dataframe(filtered_df)


