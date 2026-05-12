# **Transforming User Experience: Vanguard A/B Test Results**
<img width="1620" height="900" alt="vanguard_image" src="https://github.com/user-attachments/assets/bebff061-1dcb-4f6b-a5c3-28dad826cc67" />

This repository contains the analysis of an A/B test conducted by Vanguard to evaluate the effectiveness of a redesigned user interface (UI). The new UI introduced modern design elements and in-context prompts to enhance the user experience. This project explores the experiment's results, focusing on user behavior, completion rates, and efficiency improvements.

## Context & Study Design
This test was conducted to address a major pain point: Vanguard clients often abandon an essential online process— not due to a lack of intent, but because the interface frustrates them. These moments of friction impact efficiency, client satisfaction, and long-term revenue.

### Experiment Overview:
- **Duration**: March 15, 2017 – June 20, 2017
- **Control Group**: Used Vanguard's traditional online process.
- **Test Group**: Experienced the redesigned, modern interface.
- **Process Flow**: An initial page, three steps, and a confirmation page.

**Objective**: Determine if the updated UI improves completion rates and enhances the user experience.
---

# 📁 Table of Contents
 
1. [📈 A/B Test Raw Data Exploration](#a-b-test-raw-data-exploration)  
2. [✅ Data Cleaning & Preprocessing](#data-cleaning--preprocessing)  
3. [🎨 Exploratory Data Analysis (EDA) Key Insights](#exploratory-data-analysis-eda-key-insights)  
4. [✨ KPI Insights](#kpi-insights)  
5. [📊 A/B Testing Statistical Analysis](#a-b-testing-statistical-analysis)  

---

# 📈 A/B Test Raw Data Exploration
The raw data consisted of three datasets capturing demographic, behavioral, and web interaction data:

1. **`df_demo` (Client Demographics and Behavior Data)**
   - Provides insights into client demographics, account details, and recent activity.
     - `client_id`: Unique client identifier
     - `clnt_tenure_yr`, `clnt_tenure_mnth`: Client tenure
     - `clnt_age`: Client age
     - `gendr`: Gender
     - `num_accts`: Number of accounts
     - `bal`: Account balance
     - `calls_6_mnth`, `logons_6_mnth`: Recent client activity

2. **`df_experiment_clients` (Experiment Group Data)**
   - Identifies which group (control or test) each client belongs to.
     - `client_id`: Unique client identifier
     - `variation`: Test or control group assignment

3. **`df_web_data_pt_1` and `df_web_data_pt_2` (Web Interaction Data)**
   - Captures client interactions with the online process.
     - `client_id`: Unique client identifier
     - `visitor_id`: Client-device identifier
     - `visit_id`: Web session identifier
     - `process_step`: Step in the online process
     - `date_time`: Timestamp of interaction

---

# ✅ Data Cleaning & Preprocessing

### 1. **Merging and Consolidation**
   - Unified `df_web_data_pt_1` and `df_web_data_pt_2` into a single DataFrame (called df_web) using `pd.concat()`.
   - Merged demographic and experiment data (`df_demo` and `df_experiment`) using an outer join on `client_id`.
   - Merged unified web_data and experiment dara (`df_web` and `df_experiment`) using an inner joint on `client_id`. 

### 2. **Handling Missing Values**
   - Dropped rows with missing `control_test` values (~57% of rows).
   - Dropped rows missing demographic and the rows with missing numeric values were filled with the median.
   - Assigned "U" (Unknown) to missing gender values.

### 3. **Standardizing and Cleaning Columns**
   - Renamed columns to follow a consistent format: lowercase, underscores instead of spaces.
   - Organized columns for usability.

### 4. **Removing Duplicates**
   - Identified and removed duplicate rows based on `visit_id`, `client_id`, `process_step`, and `date_time`.

### 5. **Data Type Adjustments**
   - Converted `date_time` to a datetime format.
   - Adjusted numeric columns to appropriate types.

### 6. **Enhancements and Segmentations**
   - **Process Step Sorting**:
     - Added numeric prefixes to `process_step` (e.g., `start` → `step_1`) to ensure proper sorting. 
     - Converted `process_step` into an ordered categorical column for analysis.
   - **Chronological sorting of sessions per client_id**:
     - Sorted the dataset by `client_id`, `visit_id`, `date_time`to identidy the "first" row(session)  
   - **Age Groups**:
     - Segmented clients into age groups (e.g. young/adult/senior).
   -**Adding Seconds per Step**:
     - Calculated the seconds spend between each step and

---

# 🎨 Exploratory Data Analysis (EDA) Key Insights

## **Demographics**
- The **average client age is 48 years**, with a wide range from **17 to 96 years**. The age distribution is similar between groups, with the majority of users between 30 and 60 years old asigned to the `adult`group.

- **Gender distribution is fairly even** and shows no impact on performance: **34% unknown**, **34% male**, **32% female**.

## **Account Relationships**
- Clients **typically hold 2 accounts** (75% of clients).
- The number of accounts ranges from **1 to a maximum of 7**.

## **Tenure**
- The average client has been with Vanguard for **12 years**, with a maximum tenure of **55 years**.
- The **distribution of tenure is identical** between control and test groups.

## **Digital Engagement**
- Clients log on an average of **6 times over 6 months**.
- **75% of clients log on 8 or fewer times**, with the **top quartile being highly active (9+ logons)**.

## **Support Needs**
- Clients make an average of **3 calls per 6 months**.
- **75% of clients make 5 or fewer calls**.
- There’s a **strong correlation between logons and calls (Pearson = 0.99)**, with **logons occurring roughly twice as often as calls** (mean: **6.13 vs. 3.09**).
- The distribution is **consistent across control and test groups**.

## **Step Progression Efficiency**
- **Test group users progress more consistently** About 32-33% of the activity happens at the start, but only 12-14% reaches the **confirm stage**.

## **Seconds Spent Per Step**
- **Test group users take slightly more time per step**. There is a **higher concentration of time spent** at the **confirm stage**.

---

# ✨ KPI Insights

#### 1. **Global Completion Rate**
   - **Definition**: The number of users who reached the ‘confirm’ step (whithout having backward errors) divided by the total number of users.
   - **Control**: 29.4%  
   - **Test**: 29.7%  
   - **Insight**: The Test group and the Control group shows shows the same rate in global completion showing the new UI does not create a user friendly experience, most the users completes the process with errors or repetitions.

#### 2. **Completion Rate**
   - **Definition**: The number of users who reached the ‘confirm’ step divided by the total number of users.
   - **Control**: 65.59%  
   - **Test**: 69.29%  
   - **Insight**: The Test group shows an increase in completion rate compared to the Control group, which indicates that the changes implemented in the Test version had a positive impact on user engagement and the likelihood of completing the process.

#### 3. **Average Time per Step (s)**
   - **Definition**: The average time spent by users on each process step, measured in seconds.
   - **Control**: 83.5 seconds  
   - **Test**: 84.1 seconds  
   - **Insight**: On average, users in the **Test group spend 13.84 seconds more per step than those in the Control group**. This increase is primarily driven by the confirm stage, where Test users spend significantly more time (**243.69s vs 168.73s**). While the Test group is actually faster in the initial start, step_2, and step_3 phases, the substantial time spent on the final step suggests that the new design may be encouraging deeper engagement or requiring more thorough review before completion.

#### 4. **Error Rate**
   - **Definition**: The percentage of users who move backward in the process, indicating errors or confusion.
   - **Control**: 61,3%  
   - **Test**: 56,5%  
   - **Insight**: The Control group has a higher error rate, this could be indicative that the new UI creates on average less friction compare with the control group. The Step 3 could be indicative of issues with the new interface or process flow, possibly creating confusion that leads to more errors, despite the higher completion rate.

#### 5. ** Overall Drop-Out Rate (Final Client Interaction) **
   - **Definition**: The percentage of users who left the process before reaching the last step (confirm).
   - **Control**: 41.87%  
   - **Test**: 32.68%  
   - **Insight**: The Test group demonstrates a lower drop-off rate, suggesting that users in the Test group are less likely to abandon the process. This reflects better retention, which could be attributed to the more engaging or user-friendly design in the Test group.


---


### **Overall Summary**  
- **Improved Process Completion**: The Test group shows higher completion rates and lower drop-offs, indicating that the changes introduced are generally favorable for user experience.
- **Enhanced Retention**: The Test group achieved a significantly lower drop-out rate of 32.68% compared to 41.87% in the Control group, indicating that users are more likely to stay in the funnel until the end.
- **Rise in Interaction Errors**: Despite higher completion, the Test group saw a slight increase in the error rate (54.70% vs. 53.21%), which may point to specific areas of confusion or friction within the new interface.
**Efficiency Trade-off:** The data reveals a trade-off where the Test design successfully drives more users to finish the process but requires more time and results in slightly more backward navigation compared to the Control version.


---


# 📊 A/B Testing Statistical Analysis (to be checked)  

This analysis evaluates the effectiveness of the new user interface (Test group) compared to the existing design (Control group) through statistical hypothesis testing.  

## 🔹 Key Objective: **Completion Rate Impact**  
The **primary goal** is to determine whether the **new UI significantly improves completion rates** while maintaining usability and business viability.  

## 📌 Key Hypothesis Tests  
### **1️⃣ Completion Rate Analysis (Primary Focus)**
#### **Standard Completion Rate Test (one-Proportion Z-Test)**
- **H₀**: Completion rate is the same in both groups 
- **H₁**: (Reject the null hypothesis, H1 accepted):Completion rate of test group is different that from the control group.  
- **Result**: The new design **significantly improves** completion rates (**p > 0.05**).

#### **2️⃣ Global Completion Rate Analysis (one-Proportion Z-Test)**
- **H₀**: Global Completion rate is the same in both groups 
- **H₁**: (Reject the null hypothesis, H1 accepted): Global Completion rate of test group is different that from the control group.  
- **Result**: Global Completion rate is the same in both groups (**p > 0.05**).

#### **3️⃣ Completion Rate vs. Business Threshold (two-Sided Z-Test)**
- Tests if the Test group’s **completion rate improvement meets/exceeds the 5% business viability threshold**.  
- **Result**: The Test group did not reach the 5% absolute (**p > 0.05**) increase required for business viability. From a purely data-driven perspective based on this specific threshold, the experiment did not meet the predefined success criteria for a full rollout.
  
### **4️⃣ Error Rate Analysis (User Backward Navigation)**
- **H₀**: No significant difference in error rates (users moving backward).  
- **H₁**: The error rates differ between control and test group. 
- **Result**: **No statistically significant difference** (**p > 0.05**), indicating usability remains stable.
- 
### **5️⃣ Average Time Spent by Step (T-Test)**
#### **Measured in Seconds**  
- **H₀**: The mean of time spend in User Interface (UI) is the same in both groups.  
- **H₁**: The mean of time spend in User Interface (UI) is different between the groups. 
- **Result**: **Statistical significant difference** (**p > 0.05**).  
  

## 💡 Key Takeaways  
✅ **Completion rates significantly improve** with the new UI.  
✅ The **improvement does not surpasses the 5% business viability threshold**, supporting adoption.  
✅ **Error rates remain stable**, meaning no usability concerns.   
✅ **Significant time spend on each step**, suggesting user engagement is affected.  

## 🚀 Conclusion  
The **new UI significantly improves completion rates** but currently **falls short of the 5% business viability threshold** due to usability friction and increased error rates in early process stages. While we cannot support an immediate full rollout, we recommend an iterative approach with step-by-step implementation and additional testing—including a learning curve evaluation across all client sessions and analysis of affluent client needs based on balance significance—to decrease friction before final deployment.

--- 

# 💻 Tech Stack 

## **Data Manipulation**  
- **pandas**: Data manipulation and analysis with DataFrames.  
- **numpy**: Scientific computing with multi-dimensional arrays.  
- **datetime**: Date and time handling.  

## **Visualization** 
 - **Tableau**: Static, animated, and interactive graphics.  
 
## **Statistical Analysis**  
- **statsmodels**: Statistical models and hypothesis testing.  
- **scipy.stats**: Statistical tests and distributions.  
- **scipy.stats.contingency**: Categorical variable association.  
- **statsmodels.stats.proportion**: Proportion hypothesis tests.  
- **scipy.stats.kurtosis**: Computes dataset kurtosis.  
- **scipy.stats.probplot**: Creates probability plots.  
- **scipy.stats.chi2_contingency**: Tests categorical independence.  

