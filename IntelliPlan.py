import streamlit as st
from datetime import datetime, timedelta

# Streamlit app
st.title("IntelliPlan - Study Plan Generator")

# Input fields
st.sidebar.header("Input Details")
exam_date = st.sidebar.date_input("Exam Date", min_value=datetime.now().date())
daily_hours = st.sidebar.number_input("Daily Study Hours", min_value=1, step=1)
important_topics = st.sidebar.text_area("Important Topics (comma-separated)")

# Generate study plan
if st.sidebar.button("Generate Plan"):
    try:
        today = datetime.now()
        days_left = (datetime.combine(exam_date, datetime.min.time()) - today).days

        if days_left <= 0:
            st.error("Exam date must be in the future!")
        else:
            topics_list = [topic.strip() for topic in important_topics.split(',') if topic.strip()]
            study_plan = []
            topics_per_day = max(1, len(topics_list) // days_left)

            for day in range(days_left):
                date = today + timedelta(days=day)
                topics = topics_list[day * topics_per_day:(day + 1) * topics_per_day]
                study_plan.append({
                    'date': date.strftime('%Y-%m-%d'),
                    'topics': topics,
                    'hours': daily_hours
                })

            # Display the study plan
            st.success("Study Plan Generated!")
            for day_plan in study_plan:
                st.write(f"**Date:** {day_plan['date']}")
                st.write(f"**Topics:** {', '.join(day_plan['topics'])}")
                st.write(f"**Hours:** {day_plan['hours']}")
                st.write("---")

    except Exception as e:
        st.error(f"Error: {str(e)}")
