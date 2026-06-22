import streamlit as st
# to build streamlit web apps in Python.

import pandas as pd
# to work with CSV data.

import matplotlib.pyplot as plt
# used for charts.

from joblib import load
# loads saved Python objects (like cat_cols).

from catboost import CatBoostClassifier, Pool
# CatBoostClassifier loads your trained classification model and Pool prepares data for CatBoost prediction.

# Wide layout for dashboard 
st.set_page_config(layout="wide")

# Load model and category columns
cat_cols = load("model/cat_cols.joblib")
model = CatBoostClassifier()
model.load_model("model/order_priority_model.cbm")

# Title
st.title("📦 Order Priority Prediction App")
st.write("""
Upload a CSV file to predict Order Priority and view the analytics dashboard.
""")

uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

if uploaded_file:

    # Load user CSV
    df = pd.read_csv(uploaded_file)
    st.write("### 🔍 Preview of Uploaded File")
    st.dataframe(df.head())

    # Ensure missing categorical columns exist
    for col in cat_cols:
        if col not in df.columns:
            df[col] = ""

    # Predict
    pool = Pool(df, cat_features=cat_cols)
    preds = model.predict(pool)
    df["Predicted_Order_Priority"] = preds.ravel()

    # Simple result table
    result = df[["Order ID", "Predicted_Order_Priority"]]

    st.write("### 📝 Prediction Results")
    st.dataframe(result)

    # ---------------------- COUNT PER PRIORITY TABLE ----------------------
    st.write("### 📘 Count Per Priority")

    # Distribution Data
    dist = result["Predicted_Order_Priority"].value_counts()

    count_df = dist.reset_index().rename(
    columns={"index": "Priority", "Predicted_Order_Priority": "Count"})

    st.dataframe(count_df)


    # ---------------------- DASHBOARD SECTION ----------------------

    st.write("---")
    st.header("📊 Prediction Dashboard")



    # ---------------- KPI ROW 1 ----------------
    kpi1, kpi2, kpi3, kpi4 = st.columns(4)

    with kpi1:
     st.metric("Total Orders", len(result))

    with kpi2:
     st.metric("Unique Priority Levels", result["Predicted_Order_Priority"].nunique())

    with kpi3:
     st.metric("Most Common Priority", result["Predicted_Order_Priority"].mode()[0])

    with kpi4:
     st.metric("Least Frequent Priority", dist.idxmin())



    # ---------------------- CHART SECTION ----------------------
    chart_col1, chart_col2 = st.columns(2)

    # BAR CHART
    with chart_col1:
        st.subheader("📊 Bar Chart")
        fig1, ax1 = plt.subplots()
        ax1.bar(dist.index.astype(str), dist.values)
        ax1.set_xlabel("Priority Level")
        ax1.set_ylabel("Count")
        ax1.set_title("Order Priority Distribution")
        st.pyplot(fig1)

    # PIE CHART
    with chart_col2:
        st.subheader("🥧 Pie Chart")
        fig2, ax2 = plt.subplots()
        ax2.pie(dist.values, labels=dist.index.astype(str), autopct='%1.1f%%', startangle=90)
        ax2.set_title("Order Priority Share")
        st.pyplot(fig2)
    
    

    colA, colB = st.columns(2)

    # STACKED BAR CHART
    with colA:
        st.subheader("🏙 Region vs Priority (Stacked Bar)")
        if "Region" in df.columns:
            region_priority = pd.crosstab(df["Region"], df["Predicted_Order_Priority"])

            fig_sb, ax_sb = plt.subplots(figsize=(7, 5))
            region_priority.plot(kind="bar", stacked=True, ax=ax_sb)

            ax_sb.set_title("Region vs Order Priority")
            ax_sb.set_xlabel("Region")
            ax_sb.set_ylabel("Count")

            st.pyplot(fig_sb)
        else:
            st.warning("⚠ 'Region' column not found in uploaded file.")


    # HEATMAP
    with colB:
        st.subheader("🔥 Priority vs Category (Heatmap)")
        if "Category" in df.columns:
            heat_data = pd.crosstab(df["Predicted_Order_Priority"], df["Category"])

            fig_hm, ax_hm = plt.subplots(figsize=(7, 5))
            im = ax_hm.imshow(heat_data, cmap="viridis", aspect="auto")

            # Labels
            ax_hm.set_xticks(range(len(heat_data.columns)))
            ax_hm.set_xticklabels(heat_data.columns, rotation=45)
            ax_hm.set_yticks(range(len(heat_data.index)))
            ax_hm.set_yticklabels(heat_data.index)

            ax_hm.set_title("Priority vs Category Heatmap")
            ax_hm.set_xlabel("Category")
            ax_hm.set_ylabel("Priority")

            plt.colorbar(im, ax=ax_hm)
            st.pyplot(fig_hm)
        else:
            st.warning("⚠ 'Category' column not found in uploaded file.")



    # ---------------------- DOWNLOAD BUTTON ----------------------
    st.write("---")
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="⬇ Download Full CSV With Predictions",
        data=csv,
        file_name="predicted_orders.csv",
        mime="text/csv"
    )