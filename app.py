import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from database import create_table, insert_data, view_data, update_data, delete_data
from model import predict_sales
from auth import create_user_table, add_user, login_user

# ---------------- SETUP ----------------
st.set_page_config(page_title="Sales Dashboard", layout="wide")

create_table()
create_user_table()

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# ---------------- BRANDING ----------------
col1, col2 = st.columns([1, 5])
with col1:
    st.image("logo.png", width=80)
with col2:
    st.title("Sales Analytics Dashboard")

# ---------------- LOGIN ----------------
if not st.session_state.logged_in:
    menu = ["Login", "Register"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Login":
        st.subheader("Login")
        u = st.text_input("Username")
        p = st.text_input("Password", type="password")

        if st.button("Login"):
            if login_user(u, p):
                st.session_state.logged_in = True
                st.success("Login successful")
                st.rerun()
            else:
                st.error("Invalid credentials")

    else:
        st.subheader("Register")
        u = st.text_input("Username")
        p = st.text_input("Password", type="password")

        if st.button("Register"):
            add_user(u, p)
            st.success("Account created")

# ---------------- MAIN APP ----------------
else:
    menu = ["Dashboard", "Add Data", "Manage Data", "Predict", "Logout"]
    choice = st.sidebar.selectbox("Menu", menu)

    data = view_data()

    if data:
        df = pd.DataFrame(data, columns=["ID", "Product", "Quantity", "Price", "Date"])
        df["Date"] = pd.to_datetime(df["Date"])
        df["Revenue"] = df["Quantity"] * df["Price"]
    else:
        df = pd.DataFrame(columns=["ID","Product","Quantity","Price","Date","Revenue"])

    # ---------------- DASHBOARD ----------------
    if choice == "Dashboard":
        st.subheader("Dashboard Overview")

        if not df.empty:

            # 🎯 FILTERS
            st.sidebar.subheader("Filters")
            product_filter = st.sidebar.multiselect("Select Product", df["Product"].unique())
            date_range = st.sidebar.date_input("Select Date Range", [])

            filtered_df = df.copy()

            if product_filter:
                filtered_df = filtered_df[filtered_df["Product"].isin(product_filter)]

            if len(date_range) == 2:
                filtered_df = filtered_df[
                    (filtered_df["Date"] >= pd.to_datetime(date_range[0])) &
                    (filtered_df["Date"] <= pd.to_datetime(date_range[1]))
                ]

            # 📦 KPI CARDS
            total_sales = int(filtered_df["Quantity"].sum())
            total_revenue = float(filtered_df["Revenue"].sum())
            avg_sales = round(filtered_df["Quantity"].mean(), 2)

            col1, col2, col3 = st.columns(3)

            col1.markdown(f"""
            <div style="padding:20px;background-color:#1f77b4;color:white;border-radius:10px">
            <h3>Total Sales</h3>
            <h2>{total_sales}</h2>
            </div>
            """, unsafe_allow_html=True)

            col2.markdown(f"""
            <div style="padding:20px;background-color:#2ca02c;color:white;border-radius:10px">
            <h3>Total Revenue</h3>
            <h2>₹{total_revenue}</h2>
            </div>
            """, unsafe_allow_html=True)

            col3.markdown(f"""
            <div style="padding:20px;background-color:#ff7f0e;color:white;border-radius:10px">
            <h3>Avg Sales</h3>
            <h2>{avg_sales}</h2>
            </div>
            """, unsafe_allow_html=True)

            # 📊 PRODUCT GRAPH
            st.subheader("Product-wise Sales")
            product_data = filtered_df.groupby("Product")["Quantity"].sum()

            plt.figure()
            product_data.plot(kind="bar")
            st.pyplot(plt)

            # 📥 EXPORT
            st.subheader("Export Data")
            if st.button("Download Excel"):
                filtered_df.to_excel("sales_export.xlsx", index=False)
                st.success("File saved as sales_export.xlsx")

        else:
            st.warning("No data available")

    # ---------------- ADD DATA ----------------
    elif choice == "Add Data":
        st.subheader("Add Data")

        product = st.text_input("Product")
        quantity = st.number_input("Quantity", min_value=1)
        price = st.number_input("Price", min_value=1.0)
        date = st.date_input("Date")

        if st.button("Add"):
            insert_data(product, quantity, price, str(date))
            st.success("Data added")

    # ---------------- MANAGE ----------------
    elif choice == "Manage Data":
        st.subheader("Manage Data")

        if not df.empty:
            st.dataframe(df)

            selected_id = st.selectbox("Select ID", df["ID"])
            row = df[df["ID"] == selected_id].iloc[0]

            product = st.text_input("Product", row["Product"])
            quantity = st.number_input("Quantity", value=int(row["Quantity"]))
            price = st.number_input("Price", value=float(row["Price"]))
            date = st.text_input("Date", str(row["Date"].date()))

            col1, col2 = st.columns(2)

            if col1.button("Update"):
                update_data(selected_id, product, quantity, price, date)
                st.success("Updated")
                st.rerun()

            if col2.button("Delete"):
                delete_data(selected_id)
                st.warning("Deleted")
                st.rerun()

    # ---------------- PREDICT ----------------
    elif choice == "Predict":
        st.subheader("Sales Prediction")

        if not df.empty:
            pred = predict_sales(data)
            st.success(f"Next Day Prediction: {pred}")
        else:
            st.warning("Not enough data")

    elif choice == "Logout":
        st.session_state.logged_in = False
        st.rerun()