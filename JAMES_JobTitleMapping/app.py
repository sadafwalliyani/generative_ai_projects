import streamlit as st
import requests

@st.cache_data
def get_top_relevant_normalized_job_titles(job_title, num_answers):
    # JAMES API endpoint for the top-N relevant normalized job titles
    api_endpoint = f'http://james-mapping.xyz/api/v1/related?job_title={job_title}&num_answers={num_answers}'

    try:
        # Send GET request to JAMES API
        response = requests.get(api_endpoint)

        if response.status_code == 200:
            # Successful API call
            response_data = response.json()
            normed_job_title_list = response_data.get("normed_job_title_list", [])

            if not normed_job_title_list:
                return ["No normalized titles found"]

            # Ensure that you have at least 10 results
            while len(normed_job_title_list) < 10:
                # Fetch more data until you have at least 10 results
                num_answers += 1
                api_endpoint = f'http://james-mapping.xyz/api/v1/related?job_title={job_title}&num_answers={num_answers}'
                response = requests.get(api_endpoint)
                response_data = response.json()
                new_titles = response_data.get("normed_job_title_list", [])
                normed_job_title_list.extend(new_titles)

            return normed_job_title_list
        else:
            # API call unsuccessful
            return [f'Error: {response.status_code}']
    except requests.exceptions.RequestException as e:
        return [f'Error: {e}']

def main():
    # Set page title
    st.set_page_config(page_title='JAMES API Demo', layout='centered')
    st.title('JAMES Job Title Mapping')

    # Job title input field
    job_title = st.text_input('Enter a job title')
    num_answers = st.number_input('Select Number of Answers', min_value=1, max_value=10, step=1, value=5)

    # Submit button for top-N relevant titles
    if st.button(f'Get Top {num_answers} Relevant Titles'):
        # Perform job title normalization using the top-N relevant titles
        top_normalized_titles = get_top_relevant_normalized_job_titles(job_title, num_answers)

        st.subheader(f'Top {num_answers} Relevant Titles:')
        for i, normed_job_title in enumerate(top_normalized_titles[:num_answers], 1):
            st.text(f'{i}: {normed_job_title}')

if __name__ == '__main__':
    main()
