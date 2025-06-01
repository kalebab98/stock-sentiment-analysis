@st.cache_data
def load_data():
    import requests
    from io import StringIO

    file_id = "1oQP1TnpbBxCV9dc8d9obWqwuzxkl2qc3"
    url = f"https://drive.google.com/uc?export=download&id={file_id}"

    response = requests.get(url)
    response.raise_for_status()

    raw_csv = response.text

    st.write("Raw CSV preview:\n", raw_csv[:500])  # show first 500 chars in your Streamlit app

    csv_data = StringIO(raw_csv)

    # Try reading without parse_dates first to inspect columns
    df = pd.read_csv(csv_data)

    st.write("Columns in CSV:", df.columns.tolist())

    # Then parse dates if 'date' column exists
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'])
    else:
        st.error("'date' column not found in CSV!")

    return df
