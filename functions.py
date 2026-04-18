def clean_sex_column_f(x):
    if pd.isna(x):
        return "unknown"
    if x in ["F"]:
        return "female"
    elif x in ["M"]:
        return "male"
    elif x in ["U", "X"]:
        return "unknown"
    else:
        return "unknown"
    
def check_row_f(row):
    current = row['process_step']
    actual_next = row['process_order']
    expected = expected_next.get(current)
    
    # repeated
    if current == actual_next:
        return "repeated"
    
    # correct
    if expected == actual_next:
        return "correct"
    
    # handle last step (confirm → NaN)
    if expected is None and pd.isna(actual_next):
        return "correct"
    
    return "error"