import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

location_path = "C:/Users/Jesse/Desktop/ATM_Project/atm_location.csv"
cash_needs_path = "C:/Users/Jesse/Desktop/ATM_Project/atm_cash_needs.csv"

location_df = pd.read_csv(location_path)
cash_needs_df = pd.read_csv(cash_needs_path)

plt.figure(figsize=(10,6))
ax = sns.barplot(data=location_df, x='location_type', y='total_withdrawals', palette='coolwarm')

# Annotate atm_count on top of each bar
for i, bar in enumerate(ax.patches):
    atm_count = location_df.groupby('location_type')['atm_count'].sum().iloc[i]
    ax.text(
        bar.get_x() + bar.get_width() / 2,   # center of bar
        bar.get_height(),                    # height of bar
        f"ATMs: {atm_count}",                # label
        ha='center', va='bottom', fontsize=9, color='black'
    )

plt.title('Average ATM Utilization by Location Type')
plt.xlabel('Location Type')
plt.ylabel('Average Withdrawals per ATM')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# fig, ax1 = plt.subplots(figsize=(10,6))

# # Barplot for withdrawals
# sns.barplot(data=location_df, x='location_type', y='total_withdrawals',
#             palette='coolwarm', ax=ax1)
# ax1.set_ylabel('Average Withdrawals per ATM')

# # Second axis for ATM count
# ax2 = ax1.twinx()
# sns.pointplot(data=location_df, x='location_type', y='atm_count',
#               color='black', marker='o', ax=ax2)
# ax2.set_ylabel('ATM Count')

# plt.title('ATM Utilization and Count by Location Type')
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()


# plt.figure(figsize=(10,6))
# sns.barplot(data=location_df, x='location_type', y='total_withdrawals', palette='coolwarm')
# plt.title('Average ATM Utilization by Location Type')
# plt.xlabel('Location Type')
# plt.ylabel('Average Withdrawals per ATM')
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()