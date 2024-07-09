# Chapter 9: Procurement

### Overview
- **Purpose**: To guide the design of dimensional models for procurement processes within a data warehouse, emphasizing key components and techniques for effective procurement data analysis.
- **Scope**: Includes the design of procurement fact tables, supplier dimensions, handling of slowly changing dimensions, and a case study to illustrate practical application.

### 9.1 Purchase Orders Fact Table
- **Definition**: A central fact table capturing the details of purchase orders.
- **Grain**: The finest level of detail captured for each purchase order line item, typically one row per purchase order line item.
- **Key Measures**:
  - **Order Quantity**: Number of units ordered.
  - **Order Amount**: Total monetary value of the order line item.
  - **Discount Amount**: Any discount applied to the order.
  - **Tax Amount**: Tax applied to the order line item.
  - **Extended Price**: Total price after discounts and taxes.

- **Foreign Keys**:
  - **Product Key**: Links to the Product Dimension.
  - **Supplier Key**: Links to the Supplier Dimension.
  - **Purchase Order Key**: Links to the Purchase Order Dimension.
  - **Time Key**: Links to the Time Dimension.

### 9.2 Supplier Dimension
- **Definition**: Contains descriptive information about suppliers.
- **Key Attributes**:
  - **Supplier Key**: Surrogate key.
  - **Supplier Name**: Name of the supplier.
  - **Supplier Type**: Type of supplier (e.g., manufacturer, distributor).
  - **Supplier Location**: Geographic details including address, city, state, and postal code.
  - **Contact Information**: Contact details of the supplier, including phone number and email.
  - **Supplier Rating**: Performance rating of the supplier.

### 9.3 Purchase Order Dimension
- **Definition**: Contains descriptive information about purchase orders.
- **Key Attributes**:
  - **Purchase Order Key**: Surrogate key.
  - **Purchase Order Number**: Unique identifier for the purchase order.
  - **Purchase Order Date**: Date when the purchase order was created.
  - **Purchase Order Status**: Status of the purchase order (e.g., pending, approved, received).
  - **Buyer**: Name or identifier of the buyer who created the purchase order.

### 9.4 Time Dimension
- **Definition**: Contains temporal information for each purchase order.
- **Key Attributes**:
  - **Time Key**: Surrogate key.
  - **Date**: Full date of the transaction.
  - **Day of Week**: Day of the week.
  - **Month**: Month of the transaction.
  - **Quarter**: Quarter in which the transaction occurred.
  - **Year**: Year of the transaction.
  - **Fiscal Period**: Fiscal period for financial reporting.
  - **Holiday Indicator**: Indicates whether the date is a holiday.

### 9.5 Handling Changing Dimensions
- **Slowly Changing Dimensions (SCD)**:
  - **Type 1**: Overwrite old data with new data (e.g., updating supplier contact information).
  - **Type 2**: Add a new row for each change, preserving historical data (e.g., tracking changes in supplier rating).
  - **Type 3**: Add a new column to capture the change (e.g., tracking previous and current supplier types).

### 9.6 Procurement Line Item Fact Table
- **Purpose**: Captures the detailed line items of procurement transactions.
- **Grain**: One row per line item in a procurement transaction.
- **Key Measures**:
  - **Quantity Ordered**: Number of units ordered.
  - **Unit Price**: Price per unit.
  - **Line Item Total**: Total amount for the line item (Quantity Ordered * Unit Price).
  - **Discount Amount**: Discount applied to the line item.
  - **Net Amount**: Line Item Total after applying discounts.

- **Foreign Keys**:
  - **Product Key**: Links to the Product Dimension.
  - **Supplier Key**: Links to the Supplier Dimension.
  - **Purchase Order Key**: Links to the Purchase Order Dimension.
  - **Time Key**: Links to the Time Dimension.

### 9.7 Case Study: Procurement for a Manufacturing Company
- **Background**: A manufacturing company needs to manage and analyze its procurement processes, including purchase orders, supplier performance, and procurement costs.
- **Requirements Gathering**:
  - **Stakeholders**: Procurement managers, finance team, supply chain managers.
  - **Key Questions**:
    - What procurement metrics are critical for decision-making?
    - How are purchase orders and supplier performance tracked?
    - What dimensions are necessary for detailed analysis?

- **Findings**:
  - **Metrics**: Order quantities, order amounts, discounts, tax amounts, supplier ratings, procurement costs.
  - **Dimensions**: Time, Product, Supplier, Purchase Order.

- **Dimensional Model Design**:
  - **Fact Tables**: Purchase orders fact table, procurement line item fact table.
  - **Dimensions**: Time, Product, Supplier, Purchase Order.
  - **Grain**: Detailed line items for each procurement transaction.

- **Implementation**:
  - **Purchase Orders Fact Table**: Captures detailed purchase order transactions.
  - **Procurement Line Item Fact Table**: Captures individual line items within purchase orders.
  - **Supplier Dimension**: Includes attributes such as supplier name, type, location, and rating.
  - **Purchase Order Dimension**: Includes attributes such as purchase order number, date, and status.
  - **Time Dimension**: Captures daily, monthly, and yearly time attributes.

- **Outcome**:
  - **Actionable Insights**: Enabled the company to analyze procurement trends, manage supplier performance, and optimize procurement costs.
  - **Business Benefits**: Improved procurement efficiency, reduced costs, and enhanced supplier relationships.

### Summary
- **Key Takeaways**:
  - Designing effective dimensional models for procurement involves defining the grain, identifying key measures, and developing comprehensive dimension tables.
  - Handling changing dimensions and using procurement line item fact tables can significantly enhance data analysis and procurement management.
  - Real-world case studies illustrate the practical application of these concepts in manufacturing and other procurement-intensive industries.

These detailed notes provide a comprehensive overview of Chapter 9, covering the design of procurement fact tables, supplier dimensions, handling changing dimensions, and a case study on procurement for a manufacturing company.