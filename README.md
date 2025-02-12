# 📊 Data Binning and Smoothing in Python

## 🚀 Overview
This program implements **data binning** using **Equi-Depth and Equi-Width binning** techniques.  
It also supports **three different smoothing methods**:  
1️⃣ **Mean Binning**  
2️⃣ **Median Binning**  
3️⃣ **Boundary Binning**  

## 📥 User Input
The program asks the user to enter:  
- The number of bins  
- The binning method (`D` for Equi-Depth, `W` for Equi-Width)  
- The smoothing method (`X` for Mean, `M` for Median, `B` for Boundary)  

## 🛠️ How the Code Works
### **1️⃣ makeEquiDepthBin(data, numOfBin)**
- Divides the dataset into **equal-sized bins** (Equi-Depth Binning).  
- Each bin has approximately the **same number of elements**.

🔹 **Example:**
```python
data = [10, 20, 30, 40, 50, 60]
numOfBin = 2
# Output: [[10, 20, 30], [40, 50, 60]]
