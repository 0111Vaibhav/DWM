# Data Binning & Smoothing in Python

## 📌 Overview
This Python program performs **data binning and smoothing** using **Equi-Depth and Equi-Width binning methods**. It then applies **smoothing techniques** to replace bin values using:
1️⃣ **Mean Smoothing**  
2️⃣ **Median Smoothing**  
3️⃣ **Boundary Smoothing**  

## 🚀 Features
- Supports **Equi-Depth** and **Equi-Width** binning.
- Offers three different **smoothing methods**.
- Handles **user input dynamically**.
- Provides a **clear output** showing before & after binning.

## 🔧 How It Works
1. The user inputs:  
   - The **number of bins**  
   - The **binning method**:  
     - `'D'` → Equi-Depth Binning  
     - `'W'` → Equi-Width Binning  
   - The **smoothing method**:  
     - `'X'` → Mean Smoothing  
     - `'M'` → Median Smoothing  
     - `'B'` → Boundary Smoothing  

2. The program **sorts** the data (if necessary) and **divides it into bins**.
3. It **smooths the bins** using the chosen method.
4. The results (bins before & after smoothing) are printed.

## 📜 Program Structure
### 1️⃣ `makeEquiDepthBin(data, numOfBin)`
- Divides data into **bins with equal number of elements**.

### 2️⃣ `makeEquiWidthBin(data, numOfBin)`
- Divides data into **bins with equal range**.

### 3️⃣ `binByMean(data, numOfBin, method)`
- Replaces all values in each bin with the **bin’s mean**.

### 4️⃣ `binByMedian(data, numOfBin, method)`
- Replaces all values in each bin with the **bin’s median**.

### 5️⃣ `binByBoundary(data, numOfBin, method)`
- Replaces values with the **nearest boundary value** (min or max of the bin).

## 🖥️ Usage Example
```sh
$ python practical1.py
Enter no. of bins: 3
Enter method for Binning:
'D' for EquiDepth 
'W' for EquiWidth
D
Enter parameter for Binning:
'X' for Mean 
'M' for Median 
'B' for Boundary
X

Original Data: [5, 10, 11, 13, 35, 50, 55, 75, 92, 100, 204, 215]

Bins Before Smoothing:
[5, 10, 11, 13]
[35, 50, 55, 75]
[92, 100, 204, 215]

Bins After Smoothing:
[9.75, 9.75, 9.75, 9.75]
[53.75, 53.75, 53.75, 53.75]
[152.75, 152.75, 152.75, 152.75]

Smoothed Data: [9.75, 9.75, 9.75, 9.75, 53.75, 53.75, 53.75, 53.75, 152.75, 152.75, 152.75, 152.75]
