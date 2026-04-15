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