<h1> Order Priority Prediction Using Catboost </h1>

<h2>Overview</h2>
<p>
This project is a ML-powered web application built using Streamlit that predicts Order Priority from e-commerce order data. The application allows users to upload a CSV file, generate predictions using CatBoost model, visualize insights through interactive dashboards, and download prediction outputs.
</p>

<h2>Features</h2>

<h3>🐈 CatBoost Model</h3>
<ul>
    <li>A gradient boosting algorithm that handles categorical features efficiently and often provides strong performance on structured datasets.</li>
    <li>Predicts Order Priority using CatBoost</li>
    <li>Displays prediction results</li>
    <li>Interactive dashboard with KPIs and visualizations</li>
    <li>Download predictions as CSV</li>
</ul>

<h2>📊 Dashboard Analytics</h2>

<h3>Key Performance Indicators (KPIs)</h3>
<ul>
    <li>Total Orders</li>
    <li>Unique Priority Levels</li>
    <li>Most Common Priority</li>
    <li>Least Frequent Priority</li>
</ul>

<h3>Visualizations</h3>
<ul>
    <li>Count of Orders by Priority (Bar Chart)</li>
    <li>Priority Distribution (Pie Chart)</li>
    <li>Priority vs Region (Stacked Bar)</li>
    <li>Category vs Priority (Heatmap)</li>
</ul>

<h2>Technologies Used</h2>

<ul>
    <li>Python</li>
    <li>Streamlit</li>
    <li>Pandas</li>
    <li>NumPy</li>
    <li>Matplotlib</li>
    <li>Seaborn</li>
    <li>Scikit-learn</li>
    <li>CatBoost</li>
</ul>

<h2>Installation Instructions </h2>

<ol>
<li>
        Download all the files from the GitHub repository:
        <br>
        <a href="https://github.com/jayant-kadam/order-priority-prediction-using-catboost">
            GitHub Repository
        </a>
</li>

<li>Create a project folder and copy all downloaded files into it.</li>

<li>Run the <strong>app.py</strong> file using your preferred IDE.</li>

<li>
        Upload the <strong>priority_test</strong> CSV file and the model will predict
        Order Priority and generate an interactive dashboard.
</li>

<li>Input data must be provided in <strong>.csv</strong> format.</li>

<li>
        The input CSV file must contain the following columns:
        <p>
ROW ID, Order ID, Order Date, Ship Date, Ship Mode, Customer ID, Customer Name, Segment, City, State, Country, Market,
Region, Product ID, Category, Sub-Category, Product Name, Sales, Quantity, Discount, Shipping Cost, Profit, Order Year,
Order Month, Order Day, Ship Year, Ship Month, Ship Day, Delivery Time, Cost
        </p>
</li>
</ol>
<h2>Author</h2>

<p>
<strong>Jayant Kadam</strong><br>
Data Analyst<br>
https://www.linkedin.com/in/jayantkadam/
</p>
