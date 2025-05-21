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
        # Login/Sign-in page
        if "logged_in" not in st.session_state:
            st.session_state.logged_in = False

        if not st.session_state.logged_in:
            st.title("Welcome to IntelliPlan")
            st.text_input("Enter your nickname", key="nickname")
            if st.button("Login"):
            if st.session_state.nickname:
                st.session_state.logged_in = True
                st.success(f"Hello, {st.session_state.nickname}!")
        else:
            # Display nickname on top-right
            st.markdown(
            f"""
            <style>
            .top-right {{
                position: fixed;
                top: 10px;
                right: 10px;
                background-color: #f0f0f0;
                padding: 5px 10px;
                border-radius: 5px;
                font-weight: bold;
            }}
            </style>
            <div class="top-right">Hello, {st.session_state.nickname}!</div>
            """,
            unsafe_allow_html=True,
            )

            # Additional inputs for exams and preferences
            st.sidebar.header("Additional Details")
            exams = st.sidebar.text_area("Enter Exam Names (comma-separated)")
            study_preference = st.sidebar.radio("Preferred Study Time", ["Morning", "Night"])
            lunch_break = st.sidebar.time_input("Lunch Break Time")

            # Upload syllabus or manual entry
            st.sidebar.header("Syllabus Upload")
            syllabus_file = st.sidebar.file_uploader("Upload Syllabus File (optional)")
            manual_syllabus = st.sidebar.text_area("Or Enter Syllabus Topics (comma-separated)")

            # Generate detailed study plan
            if st.sidebar.button("Generate Detailed Plan"):
            try:
                today = datetime.now()
                days_left = (datetime.combine(exam_date, datetime.min.time()) - today).days

                if days_left <= 0:
                st.error("Exam date must be in the future!")
                else:
                topics_list = []
                if syllabus_file:
                    topics_list = syllabus_file.read().decode("utf-8").splitlines()
                elif manual_syllabus:
                    topics_list = [topic.strip() for topic in manual_syllabus.split(',') if topic.strip()]

                if not topics_list:
                    st.error("No topics provided!")
                else:
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

                    # Display the study plan with progress bars
                    st.success("Detailed Study Plan Generated!")
                    for day_plan in study_plan:
                    st.write(f"**Date:** {day_plan['date']}")
                    st.write(f"**Topics:** {', '.join(day_plan['topics'])}")
                    st.write(f"**Hours:** {day_plan['hours']}")
                    for topic in day_plan['topics']:
                        st.checkbox(f"Mark as done: {topic}")
                    st.write("---")

            except Exception as e:
                st.error(f"Error: {str(e)}")
