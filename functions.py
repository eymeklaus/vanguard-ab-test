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

def age_group_f(x):
    if x < 30:
        return "young"
    elif 30 <= x <= 60:
        return "adult"
    else:
        return "senior"
    
# 2. Logic to check each group
def check_journey_f(group):
    actual_steps = group['process_step'].tolist()
    actual_statuses = group['process_status'].tolist()
    
    # Check if sequence is exactly the ideal path AND all statuses are 'correct'
    return (actual_steps == ideal_path) and all(s == 'correct' for s in actual_statuses)

def check_any_completion_f(group):
    """
    Checks if 'confirm' exists in the user's journey.
    """
    actual_steps = group['process_step'].tolist()
    
    # Standard Completion: Did they ever reach the end?
    return 'confirm' in actual_steps

def get_user_error_flags_f(group_series):
    """
    Processes the sequence of steps for a client and returns error flags.
    """
    # Map to ranks internally
    ranks = group_series.map(step_ranks).dropna().tolist()
    
    has_backwards = False
    
    if len(ranks) >= 2:
        # Calculate differences (e.g., 2-1 = 1, 1-2 = -1)
        diffs = [ranks[i] - ranks[i-1] for i in range(1, len(ranks))]
        has_backwards = any(d < 0 for d in diffs)
        
    return pd.Series([has_backwards])

# 3. Now run the aggregation
def aggregate_client_kpis_f(group):
    completed = 'confirm' in group['process_step'].values
    
    # Force numeric and drop NaNs for the math
    ranks = pd.to_numeric(group['step_rank'], errors='coerce').dropna().tolist()
    
    backwards = False
    is_global = False
    
    if len(ranks) >= 2:
        diffs = [ranks[i] - ranks[i-1] for i in range(1, len(ranks))]
        backwards = any(d < 0 for d in diffs)
        is_global = (ranks == [1, 2, 3, 4, 5])
    
    # We use .get() or check existence to be extra safe
    avg_time = 0
    if 'seconds_spent' in group.columns:
        avg_time = group['seconds_spent'].mean()

    return pd.Series({
        'variation': group['variation'].iloc[0],
        'is_completed': int(completed),
        'is_global_success': int(is_global),
        'has_backwards_error': int(backwards),
        'avg_time_per_step': round(avg_time, 2) if pd.notnull(avg_time) else 0
    })