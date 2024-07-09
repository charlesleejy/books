# Chapter 8: Inventory

### Overview
- **Purpose**: To provide a comprehensive guide to designing dimensional models for inventory management in a data warehouse.
- **Scope**: Includes the design of inventory fact tables, dimensions, handling of slowly changing dimensions, and a case study to illustrate practical application.

### 8.1 Inventory Periodic Snapshot
- **Definition**: A fact table that captures the state of inventory at regular intervals (e.g., daily, weekly).
- **Grain**: The finest level of detail for each inventory snapshot, typically one row per product per store per day.
- **Key Measures**:
  - **Inventory Quantity**: Number of units on hand at the snapshot time.
  - **Inventory Value**: Total value of the inventory on hand.
  - **Reorder Point**: Threshold quantity that triggers a reorder.
  - **Days of Supply**: Estimated number of days inventory will last based on current sales rate.

- **Foreign Keys**:
  - **Product Key**: Links to the Product Dimension.
  - **Store Key**: Links to the Store Dimension.
  - **Time Key**: Links to the Time Dimension.

### 8.2 Inventory Transactions
- **Definition**: A fact table that captures detailed inventory movements (e.g., receipts, shipments, returns, adjustments).
- **Grain**: The finest level of detail for each inventory transaction, typically one row per transaction line item.
- **Key Measures**:
  - **Quantity In**: Number of units received into inventory.
  - **Quantity Out**: Number of units shipped out or sold.
  - **Transaction Value**: Monetary value of the inventory movement.
  - **Transaction Cost**: Cost associated with the transaction (e.g., shipping, handling).

- **Foreign Keys**:
  - **Product Key**: Links to the Product Dimension.
  - **Store Key**: Links to the Store Dimension.
  - **Time Key**: Links to the Time Dimension.
  - **Transaction Type Key**: Links to the Transaction Type Dimension.

### 8.3 Warehouse Dimension
- **Definition**: Contains descriptive information about each warehouse or storage location.
- **Key Attributes**:
  - **Warehouse Key**: Surrogate key.
  - **Warehouse Name**: Name of the warehouse.
  - **Warehouse Location**: Geographic details including address, city, state, and postal code.
  - **Warehouse Size**: Size of the warehouse, typically in square feet.
  - **Warehouse Type**: Type of warehouse (e.g., regional distribution center, central warehouse).

### 8.4 Handling Changing Dimensions
- **Slowly Changing Dimensions (SCD)**:
  - **Type 1**: Overwrite old data with new data (e.g., updating warehouse manager).
  - **Type 2**: Add a new row for each change, preserving historical data (e.g., tracking changes in warehouse location).
  - **Type 3**: Add a new column to capture the change (e.g., tracking previous and current warehouse types).

### 8.5 Inventory Adjustment Fact Table
- **Purpose**: Captures inventory adjustments due to various reasons (e.g., inventory count discrepancies, damage).
- **Grain**: One row per adjustment transaction.
- **Key Measures**:
  - **Adjustment Quantity**: Number of units adjusted.
  - **Adjustment Value**: Monetary value of the adjustment.
  - **Reason Code**: Code indicating the reason for the adjustment.

- **Foreign Keys**:
  - **Product Key**: Links to the Product Dimension.
  - **Store Key**: Links to the Store Dimension.
  - **Time Key**: Links to the Time Dimension.
  - **Adjustment Type Key**: Links to the Adjustment Type Dimension.

### 8.6 Case Study: Retail Inventory Management
- **Background**: A retail company needs to manage and analyze its inventory levels, transactions, and adjustments.
- **Requirements Gathering**:
  - **Stakeholders**: Inventory managers, store managers, finance team.
  - **Key Questions**:
    - What inventory metrics are critical for decision-making?
    - How are inventory transactions and adjustments tracked?
    - What dimensions are necessary for detailed analysis?

- **Findings**:
  - **Metrics**: Inventory levels, inventory value, reorder points, transaction quantities, adjustment quantities.
  - **Dimensions**: Time, Product, Store, Warehouse, Transaction Type, Adjustment Type.

- **Dimensional Model Design**:
  - **Fact Tables**: Inventory periodic snapshot fact table, inventory transactions fact table, inventory adjustment fact table.
  - **Dimensions**: Time, Product, Store, Warehouse, Transaction Type, Adjustment Type.
  - **Grain**: Daily inventory snapshots and detailed transaction/adjustment records.

- **Implementation**:
  - **Inventory Periodic Snapshot Fact Table**: Captures daily inventory levels and values.
  - **Inventory Transactions Fact Table**: Captures detailed inventory movements.
  - **Inventory Adjustment Fact Table**: Captures inventory adjustments.
  - **Warehouse Dimension**: Includes attributes such as warehouse name, location, and size.
  - **Product Dimension**: Includes attributes such as product name, category, and supplier.
  - **Time Dimension**: Captures daily, monthly, and yearly time attributes.

- **Outcome**:
  - **Actionable Insights**: Enabled the company to analyze inventory trends, manage stock levels, and identify discrepancies.
  - **Business Benefits**: Improved inventory management, reduced stockouts, and optimized reorder processes.

### Summary
- **Key Takeaways**:
  - Designing effective dimensional models for inventory management involves defining the grain, identifying key measures, and developing comprehensive dimension tables.
  - Handling changing dimensions and using inventory adjustment fact tables can significantly enhance data analysis and inventory control.
  - Real-world case studies illustrate the practical application of these concepts in retail environments.

These detailed notes provide a comprehensive overview of Chapter 8, covering the design of inventory periodic snapshot and transaction fact tables, warehouse dimensions, handling changing dimensions, and a case study on retail inventory management.