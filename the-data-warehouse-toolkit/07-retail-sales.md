# Chapter 7: Retail Sales

### Overview
- **Purpose**: To provide a detailed approach to designing dimensional models for retail sales, covering the key components and techniques for building effective retail data warehouses.
- **Scope**: Includes the design of sales fact tables, product, store, and time dimensions, as well as best practices and a case study to illustrate practical application.

### 7.1 Sales Fact Table
- **Definition**: Central fact table capturing the details of each sales transaction.
- **Grain**: The finest level of detail captured for each sale, typically one row per transaction line item.
- **Key Measures**:
  - **Sales Amount**: Total revenue from the sale.
  - **Quantity Sold**: Number of units sold.
  - **Discount Amount**: Any discount applied to the sale.
  - **Cost of Goods Sold (COGS)**: Cost associated with the items sold.
  - **Profit**: Calculated as Sales Amount minus COGS and Discount Amount.

- **Foreign Keys**:
  - **Product Key**: Links to the Product Dimension.
  - **Store Key**: Links to the Store Dimension.
  - **Customer Key**: Links to the Customer Dimension (if tracked).
  - **Time Key**: Links to the Time Dimension.
  - **Promotion Key**: Links to the Promotion Dimension (if applicable).

### 7.2 Product Dimension
- **Definition**: Contains descriptive information about products sold.
- **Key Attributes**:
  - **Product Key**: Surrogate key.
  - **Product Name**: Descriptive name of the product.
  - **Product Category**: Category to which the product belongs.
  - **Product Subcategory**: More specific classification within a category.
  - **Brand**: Brand of the product.
  - **SKU (Stock Keeping Unit)**: Unique identifier for the product.
  - **Supplier**: Information about the product supplier.
  - **Unit Price**: Standard price per unit.
  - **Package Size**: Description of the packaging (e.g., 12 oz bottle).

### 7.3 Store Dimension
- **Definition**: Contains descriptive information about each store.
- **Key Attributes**:
  - **Store Key**: Surrogate key.
  - **Store Name**: Name of the store.
  - **Store Type**: Type of store (e.g., retail, outlet, online).
  - **Store Location**: Geographic location details including address, city, state, and postal code.
  - **Region**: Larger geographic classification, such as region or market.
  - **Store Size**: Size of the store, typically in square feet.
  - **Store Manager**: Name or identifier of the store manager.
  - **Opening Date**: Date the store opened.

### 7.4 Time Dimension
- **Definition**: Contains temporal information for each transaction.
- **Key Attributes**:
  - **Time Key**: Surrogate key.
  - **Date**: Full date of the transaction.
  - **Day of Week**: Day of the week.
  - **Month**: Month of the transaction.
  - **Quarter**: Quarter in which the transaction occurred.
  - **Year**: Year of the transaction.
  - **Fiscal Period**: Fiscal period for financial reporting.
  - **Holiday Indicator**: Indicates whether the date is a holiday.

### 7.5 Designing the Retail Sales Schema
- **Star Schema**:
  - Central sales fact table surrounded by related dimensions (Product, Store, Time, Customer).
  - Simplified queries and enhanced performance due to fewer joins.

- **Snowflake Schema**:
  - Normalized dimension tables (e.g., Product Dimension split into Product, Category, and Supplier tables).
  - Reduces redundancy but increases complexity and join operations.

### 7.6 Handling Changing Dimensions
- **Slowly Changing Dimensions (SCD)**:
  - **Type 1**: Overwrite old data with new data (e.g., updating product price).
  - **Type 2**: Add a new row for each change, preserving historical data (e.g., tracking changes in store manager).
  - **Type 3**: Add a new column to capture the change (e.g., tracking previous and current product categories).

### 7.7 Aggregated Fact Tables
- **Purpose**: Improve query performance by storing precomputed summaries.
- **Types**:
  - **Daily Sales Summary**: Aggregate daily sales data by store and product.
  - **Monthly Sales Summary**: Aggregate monthly sales data by region and product category.

### 7.8 Case Study: Retail Inventory Management
- **Background**: A retail company needs to analyze sales, inventory levels, and product performance.
- **Requirements Gathering**:
  - **Stakeholders**: Sales managers, inventory managers, product managers.
  - **Key Questions**:
    - What sales metrics are critical for decision-making?
    - How are inventory levels tracked and managed?
    - What dimensions are necessary for detailed analysis?

- **Findings**:
  - **Metrics**: Total sales, units sold, inventory levels, stockouts, reorder points.
  - **Dimensions**: Time, Product, Store, Supplier.

- **Dimensional Model Design**:
  - **Fact Tables**: Sales fact table, Inventory fact table.
  - **Dimensions**: Time, Product, Store, Supplier.
  - **Grain**: Daily sales transactions and daily inventory levels.

- **Implementation**:
  - **Sales Fact Table**: Captures detailed sales transactions.
  - **Inventory Fact Table**: Captures daily inventory snapshots.
  - **Product Dimension**: Includes attributes such as product name, category, and supplier.
  - **Store Dimension**: Includes attributes such as store name, type, and location.
  - **Time Dimension**: Captures daily, monthly, and yearly time attributes.

- **Outcome**:
  - **Actionable Insights**: Enabled the company to analyze sales trends, optimize inventory levels, and evaluate product performance.
  - **Business Benefits**: Improved inventory management, increased sales, and enhanced customer satisfaction.

### Summary
- **Key Takeaways**:
  - Designing effective dimensional models for retail sales involves defining the grain, identifying key measures, and developing comprehensive dimension tables.
  - Handling changing dimensions and using aggregated fact tables can significantly enhance query performance and data analysis.
  - Real-world case studies illustrate the practical application of these concepts in retail environments.

These detailed notes provide a comprehensive overview of Chapter 7, covering the design of sales fact tables, product, store, and time dimensions, handling changing dimensions, and a case study on retail inventory management.