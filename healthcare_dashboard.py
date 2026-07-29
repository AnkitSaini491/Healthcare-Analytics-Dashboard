import pandas as pd
import matplotlib.pyplot as plt

# ==========================================
# HEALTHCARE ANALYTICS DATA
# ==========================================

healthcare = {

    "Month":[
        "Jan","Feb","Mar","Apr","May","Jun",
        "Jul","Aug","Sep","Oct","Nov","Dec"
    ],

    "Patients":[
        850,920,980,1050,1120,1180,
        1240,1300,1360,1420,1490,1550
    ],

    "Admissions":[
        780,840,900,960,1020,1080,
        1140,1200,1260,1320,1380,1450
    ],

    "Recovered":[
        720,780,840,900,960,1020,
        1080,1140,1200,1260,1320,1390
    ],

    "Emergency":[
        95,100,105,110,115,120,
        125,130,135,140,145,150
    ],

    "Revenue":[
        52000,55000,58000,61000,64000,67000,
        70000,73000,76000,79000,83000,87000
    ],

    "Satisfaction":[
        4.2,4.3,4.3,4.4,4.4,4.5,
        4.5,4.6,4.6,4.7,4.8,4.9
    ]
}

df = pd.DataFrame(healthcare)

# ==========================================
# KPI VALUES
# ==========================================

total_patients = df["Patients"].sum()
total_admissions = df["Admissions"].sum()
total_recovered = df["Recovered"].sum()
total_emergency = df["Emergency"].sum()

avg_revenue = df["Revenue"].mean()

recovery_rate = (
    total_recovered / total_admissions
) * 100

avg_satisfaction = df["Satisfaction"].mean()

# ==========================================
# DASHBOARD STYLE
# ==========================================

plt.style.use("dark_background")

fig = plt.figure(figsize=(20,12))
fig.patch.set_facecolor("#0B1020")

fig.suptitle(
    "HEALTHCARE ANALYTICS DASHBOARD",
    fontsize=28,
    color="white",
    fontweight="bold"
)

# ==========================================
# KPI CARDS
# ==========================================

plt.figtext(
0.02,0.90,
f"Patients\n{total_patients:,}",
fontsize=14,
bbox=dict(facecolor="#2563EB",boxstyle="round,pad=0.8")
)

plt.figtext(
0.18,0.90,
f"Admissions\n{total_admissions:,}",
fontsize=14,
bbox=dict(facecolor="#16A34A",boxstyle="round,pad=0.8")
)

plt.figtext(
0.35,0.90,
f"Recovery\n{recovery_rate:.1f}%",
fontsize=14,
bbox=dict(facecolor="#10B981",boxstyle="round,pad=0.8")
)

plt.figtext(
0.52,0.90,
f"Emergency\n{total_emergency:,}",
fontsize=14,
bbox=dict(facecolor="#DC2626",boxstyle="round,pad=0.8")
)

plt.figtext(
0.69,0.90,
f"Avg Revenue\n£{avg_revenue:,.0f}",
fontsize=14,
bbox=dict(facecolor="#F59E0B",boxstyle="round,pad=0.8")
)

plt.figtext(
0.85,0.90,
f"Satisfaction\n{avg_satisfaction:.1f} ⭐",
fontsize=14,
bbox=dict(facecolor="#8B5CF6",boxstyle="round,pad=0.8")
)

# ==========================================
# CHART 1 - MONTHLY PATIENTS
# ==========================================

ax1 = plt.subplot(3,2,1)

ax1.plot(
    df["Month"],
    df["Patients"],
    marker="o",
    linewidth=3,
    color="cyan"
)

ax1.fill_between(
    df["Month"],
    df["Patients"],
    color="cyan",
    alpha=0.30
)

ax1.set_title("Monthly Patient Visits")
ax1.set_ylabel("Patients")
ax1.grid(alpha=0.3)
ax1.tick_params(axis="x", rotation=45)
# ==========================================
# CHART 2 - MONTHLY HOSPITAL REVENUE
# ==========================================

ax2 = plt.subplot(3,2,2)

ax2.plot(
    df["Month"],
    df["Revenue"],
    marker="o",
    linewidth=3,
    color="gold"
)

ax2.fill_between(
    df["Month"],
    df["Revenue"],
    color="gold",
    alpha=0.30
)

ax2.set_title("Monthly Hospital Revenue")
ax2.set_ylabel("Revenue (£)")
ax2.grid(alpha=0.3)
ax2.tick_params(axis="x", rotation=45)


# ==========================================
# CHART 3 - DEPARTMENT-WISE PATIENTS
# ==========================================

department = pd.DataFrame({

    "Department":[
        "Cardiology",
        "Neurology",
        "Orthopedics",
        "Pediatrics",
        "General"
    ],

    "Patients":[
        2150,
        1780,
        1940,
        1650,
        2520
    ]
})

ax3 = plt.subplot(3,2,3)

ax3.bar(
    department["Department"],
    department["Patients"],
    color=[
        "#3B82F6",
        "#10B981",
        "#F59E0B",
        "#EF4444",
        "#8B5CF6"
    ]
)

ax3.set_title("Department-wise Patients")
ax3.set_ylabel("Patients")
ax3.grid(alpha=0.3)
ax3.tick_params(axis="x", rotation=25)


# ==========================================
# CHART 4 - RECOVERY VS ADMISSIONS
# ==========================================

ax4 = plt.subplot(3,2,4)

ax4.plot(
    df["Month"],
    df["Admissions"],
    marker="o",
    linewidth=3,
    color="deepskyblue"
)

ax4.plot(
    df["Month"],
    df["Recovered"],
    marker="o",
    linewidth=3,
    color="lime"
)

ax4.set_title("Admissions vs Recoveries")
ax4.set_ylabel("Patients")
ax4.legend(["Admissions","Recovered"])
ax4.grid(alpha=0.3)
ax4.tick_params(axis="x", rotation=45)


# ==========================================
# CHART 5 - AGE GROUP ANALYSIS
# ==========================================

age = pd.DataFrame({

    "Age Group":[
        "0-18",
        "19-35",
        "36-50",
        "51-65",
        "65+"
    ],

    "Patients":[
        980,
        1650,
        1850,
        1420,
        950
    ]
})

ax5 = plt.subplot(3,2,5)

ax5.bar(
    age["Age Group"],
    age["Patients"],
    color="orange"
)

ax5.set_title("Age Group Analysis")
ax5.set_ylabel("Patients")
ax5.grid(alpha=0.3)


# ==========================================
# CHART 6 - DISEASE DISTRIBUTION
# ==========================================

disease = pd.DataFrame({

    "Disease":[
        "Heart",
        "Diabetes",
        "Cancer",
        "Flu",
        "Other"
    ],

    "Cases":[
        22,
        26,
        14,
        18,
        20
    ]
})

ax6 = plt.subplot(3,2,6)

ax6.pie(
    disease["Cases"],
    labels=disease["Disease"],
    autopct="%1.1f%%",
    startangle=90
)

ax6.set_title("Disease Distribution")

plt.tight_layout(rect=[0,0,1,0.88])

# ==========================================
# CHART 7 - GENDER DISTRIBUTION
# ==========================================

gender = pd.DataFrame({

    "Gender":[
        "Male",
        "Female",
        "Children"
    ],

    "Patients":[
        4200,
        4600,
        1800
    ]
})

plt.figure(figsize=(8,5))
plt.style.use("dark_background")

plt.pie(
    gender["Patients"],
    labels=gender["Gender"],
    autopct="%1.1f%%",
    startangle=90,
    colors=["#3B82F6","#EC4899","#10B981"]
)

plt.title("Gender Distribution")

plt.tight_layout()
plt.show()


# ==========================================
# CHART 8 - BED OCCUPANCY
# ==========================================

beds = pd.DataFrame({

    "Department":[
        "Cardiology",
        "Neurology",
        "Orthopedics",
        "Pediatrics",
        "General"
    ],

    "Occupancy":[
        88,
        81,
        84,
        76,
        92
    ]
})

plt.figure(figsize=(10,5))
plt.style.use("dark_background")

plt.bar(
    beds["Department"],
    beds["Occupancy"],
    color="dodgerblue"
)

plt.title("Bed Occupancy Rate")
plt.ylabel("Occupancy (%)")
plt.ylim(0,100)
plt.grid(alpha=0.3)

plt.tight_layout()
plt.show()


# ==========================================
# CHART 9 - DOCTOR PERFORMANCE
# ==========================================

doctor = pd.DataFrame({

    "Doctor":[
        "Dr A",
        "Dr B",
        "Dr C",
        "Dr D",
        "Dr E"
    ],

    "Patients":[
        520,
        610,
        570,
        690,
        640
    ]
})

plt.figure(figsize=(10,5))
plt.style.use("dark_background")

plt.bar(
    doctor["Doctor"],
    doctor["Patients"],
    color="orange"
)

plt.title("Doctor Performance")
plt.ylabel("Patients Treated")
plt.grid(alpha=0.3)

plt.tight_layout()
plt.show()


# ==========================================
# CHART 10 - PATIENT SATISFACTION
# ==========================================

plt.figure(figsize=(10,5))
plt.style.use("dark_background")

plt.plot(
    df["Month"],
    df["Satisfaction"],
    marker="o",
    linewidth=3,
    color="lime"
)

plt.fill_between(
    df["Month"],
    df["Satisfaction"],
    color="lime",
    alpha=0.30
)

plt.title("Patient Satisfaction Trend")
plt.ylabel("Rating")
plt.ylim(4.0,5.0)
plt.grid(alpha=0.3)

plt.tight_layout()
plt.show()


# ==========================================
# SUMMARY REPORT
# ==========================================

best_month = df.loc[df["Recovered"].idxmax()]

print("="*65)
print("HEALTHCARE ANALYTICS SUMMARY")
print("="*65)

print(f"Total Patients           : {total_patients:,}")
print(f"Total Admissions         : {total_admissions:,}")
print(f"Recovered Patients       : {total_recovered:,}")
print(f"Emergency Cases          : {total_emergency:,}")
print(f"Recovery Rate            : {recovery_rate:.2f}%")
print(f"Average Revenue          : £{avg_revenue:,.2f}")
print(f"Average Satisfaction     : {avg_satisfaction:.2f} ⭐")

print(f"\nBest Recovery Month      : {best_month['Month']}")
print(f"Recovered Patients       : {best_month['Recovered']}")

print("="*65)


# ==========================================
# SAVE DASHBOARD
# ==========================================

fig.savefig(
    "healthcare_dashboard.png",
    dpi=300,
    bbox_inches="tight"
)

print("\nDashboard saved as healthcare_dashboard.png")


# ==========================================
# PROJECT DETAILS
# ==========================================

print("\nProject Name : Healthcare Analytics Dashboard")
print("Technology   : Python | Pandas | Matplotlib")
print("Domain       : Healthcare Analytics")
print("Status       : Dashboard Generated Successfully")


# ==========================================
# FOOTER
# ==========================================

plt.figtext(
    0.28,
    0.02,
    "Developed using Python | Pandas | Matplotlib",
    fontsize=11,
    color="white"
)

plt.show()
