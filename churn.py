import pandas as pd
import numpy as np

print("=" * 55)
print("   CUSTOMER CHURN ANALYSIS — TASK 2")
print("=" * 55)

# Step 1: Create customer dataset
data = {
    'customer_id': [1,2,3,4,5,6,7,8,9,10,
                    11,12,13,14,15,16,17,18,19,20],
    'name': ['Alice','Bob','Carol','David','Emma',
             'Frank','Grace','Henry','Irene','James',
             'Kate','Leo','Mia','Nick','Olivia',
             'Paul','Quinn','Rose','Sam','Tina'],
    'age': [25,45,32,52,28,38,41,29,55,33,
            47,31,26,43,37,50,29,34,48,27],
    'subscription_plan': ['Basic','Premium','Basic','Premium','Basic',
                          'Standard','Premium','Basic','Standard','Premium',
                          'Basic','Standard','Basic','Premium','Standard',
                          'Premium','Basic','Standard','Premium','Basic'],
    'monthly_charges': [29,99,29,99,29,59,99,29,59,99,
                        29,59,29,99,59,99,29,59,99,29],
    'tenure_months': [2,36,4,48,1,24,60,3,12,42,
                      5,18,2,54,30,45,1,22,38,3],
    'support_calls': [5,1,4,0,6,2,1,5,3,0,
                      6,2,7,0,1,1,8,2,0,5],
    'last_login_days': [45,5,30,3,60,10,2,50,15,4,
                        55,12,70,1,8,6,65,9,3,40],
    'churned': [1,0,1,0,1,0,0,1,0,0,
                1,0,1,0,0,0,1,0,0,1]
}

df = pd.DataFrame(data)
print(f"\n✅ Dataset loaded: {df.shape[0]} customers, {df.shape[1]} columns")

# Step 2: Basic stats
print("\n--- CHURN OVERVIEW ---")
total = len(df)
churned = df['churned'].sum()
active = total - churned
churn_rate = (churned / total * 100).round(2)

print(f"Total Customers : {total}")
print(f"Churned         : {churned}")
print(f"Active          : {active}")
print(f"Churn Rate      : {churn_rate}%")

# Step 3: Churn by subscription plan
print("\n--- CHURN BY SUBSCRIPTION PLAN ---")
plan_churn = df.groupby('subscription_plan')['churned'].agg(['sum','count'])
plan_churn.columns = ['Churned', 'Total']
plan_churn['Churn Rate %'] = (plan_churn['Churned'] / plan_churn['Total'] * 100).round(2)
print(plan_churn.to_string())

# Step 4: Avg stats - churned vs active
print("\n--- CHURNED vs ACTIVE CUSTOMERS ---")
comparison = df.groupby('churned')[['age','monthly_charges',
                                    'tenure_months','support_calls',
                                    'last_login_days']].mean().round(2)
comparison.index = ['Active', 'Churned']
print(comparison.to_string())

# Step 5: High risk customers
print("\n--- HIGH RISK CUSTOMERS (likely to churn) ---")
high_risk = df[
    (df['churned'] == 0) &
    (df['support_calls'] >= 3) |
    (df['last_login_days'] >= 20) &
    (df['tenure_months'] <= 6)
]
print(high_risk[['customer_id','name','subscription_plan',
                  'support_calls','last_login_days','tenure_months']].to_string(index=False))

# Step 6: Retention suggestions
print("\n--- RETENTION SUGGESTIONS ---")
print("1. Basic plan customers churn most — offer discounts or upgrades")
print("2. High support calls = frustration — improve customer support")
print("3. Inactive 30+ days customers — send re-engagement emails")
print("4. New customers (tenure < 6 months) — need onboarding support")
print("5. Premium customers rarely churn — reward their loyalty")

# Step 7: Save results
df.to_csv('churn_analysis.csv', index=False)
print("\n✅ Saved to churn_analysis.csv!")
print("\n🎉 Customer Churn Analysis — COMPLETE!")