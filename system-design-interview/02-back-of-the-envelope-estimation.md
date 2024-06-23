### Chapter 2: Back-of-the-envelope Estimation

#### Introduction
The chapter introduces back-of-the-envelope estimation, an essential skill in system design interviews. This type of estimation helps quickly gauge the feasibility and scale of a system by making educated guesses about key parameters. It involves making rough calculations to understand system constraints, capacities, and requirements.

#### Importance of Back-of-the-envelope Estimation
- **Quick Assessment**: Enables rapid assessment of a system’s requirements without detailed analysis.
- **Feasibility Check**: Helps determine if a proposed design is feasible within given constraints.
- **Communication Tool**: Provides a means to communicate ideas and assumptions effectively during discussions.
- **Preparation for Interviews**: Essential for system design interviews, where interviewers expect candidates to demonstrate this skill.

#### Key Components of Estimation
1. **Traffic Estimation**:
   - **Number of Users**: Estimate the total number of users for the system.
   - **Active Users**: Determine the percentage of daily active users (DAU).
   - **Requests per User**: Estimate the number of requests each active user makes per day.

2. **Storage Estimation**:
   - **Data per Request**: Calculate the average data size per request.
   - **Data Retention**: Determine how long the data needs to be stored.
   - **Total Storage**: Multiply data per request by the number of requests and the retention period to get total storage needs.

3. **Bandwidth Estimation**:
   - **Data Transfer per Request**: Estimate the amount of data transferred per request.
   - **Total Data Transfer**: Multiply data transfer per request by the total number of requests to get the bandwidth requirement.

4. **Memory Estimation**:
   - **Working Set Size**: Determine the amount of data actively used in memory.
   - **Cache Requirements**: Estimate the memory required for caching frequently accessed data.

5. **CPU Estimation**:
   - **CPU Time per Request**: Estimate the CPU time needed to process each request.
   - **Total CPU Requirements**: Multiply CPU time per request by the total number of requests to get total CPU needs.

#### Example Walkthrough
The chapter provides a detailed example to illustrate the estimation process. Here's a summarized version:

1. **Estimating Traffic for a Social Media Platform**:
   - **Number of Users**: 10 million registered users.
   - **Active Users**: 10% of users are active daily (1 million DAU).
   - **Requests per User**: Each active user makes 50 requests per day.
   - **Total Requests**: 1 million users * 50 requests = 50 million requests per day.

2. **Estimating Storage Requirements**:
   - **Data per Request**: Each request generates 1 KB of data.
   - **Total Data per Day**: 50 million requests * 1 KB = 50 GB per day.
   - **Data Retention**: Data is retained for 1 year (365 days).
   - **Total Storage**: 50 GB/day * 365 days = 18.25 TB.

3. **Estimating Bandwidth Requirements**:
   - **Data Transfer per Request**: 1 KB/request.
   - **Total Data Transfer**: 50 million requests * 1 KB = 50 GB per day.

4. **Estimating Memory Requirements**:
   - **Working Set Size**: Active data in memory is 10% of daily data (5 GB).
   - **Cache Requirements**: 5 GB of memory for caching.

5. **Estimating CPU Requirements**:
   - **CPU Time per Request**: 10 milliseconds per request.
   - **Total CPU Time**: 50 million requests * 10 ms = 500,000 seconds = approximately 139 CPU hours per day.

#### Tips and Best Practices
- **Simplify Assumptions**: Make reasonable and simple assumptions to facilitate quick calculations.
- **Sanity Checks**: Cross-check estimates with known benchmarks or real-world data to validate them.
- **Iterative Approach**: Refine estimates as more information becomes available.
- **Communicate Clearly**: Clearly state assumptions and calculations when presenting estimates.
- **Use Powers of Ten**: Simplify calculations by using powers of ten for rough estimates.

#### Conclusion
Back-of-the-envelope estimation is a critical skill for system designers, enabling quick, rough calculations to assess system requirements and feasibility. By mastering this skill, designers can make informed decisions, communicate effectively, and excel in system design interviews.