# Virus-photo_marge

### **📌 ব্যবহারের নিয়ম ও প্রয়োজনীয় প্যাকেজসমূহ**  

আপনার **Termux**-এ এই **টুলটি চালানোর জন্য** কিছু **প্যাকেজ ইনস্টল** করতে হবে। **ধাপে ধাপে** সেটআপ ও রান করার প্রক্রিয়া নিচে দেওয়া হলো।  

---

### **✅ ১. প্রয়োজনীয় প্যাকেজ ইনস্টল করুন**
আপনার **Termux**-এ নিচের কমান্ডগুলো রান করুন:

```bash
pkg update && pkg upgrade -y
pkg install python -y
pkg install zip -y
pkg install unzip -y
pkg install cat -y
```

---

### **✅ ২. টুলস ক্লোন করা**
**টারমাক্স এর মধ্যে ক্লোন করতে নিচের কমান্ড ব্যবহার করুন**

```bash
git clone https://github.com/RH0099/Virus-photo_marge.git
```

---

### **✅ ৩. স্ক্রিপ্ট রান করুন**
এখন স্ক্রিপ্টটি চালানোর জন্য নিচের কমান্ড দিন:

```bash
cd Virus-photo_marge

```
---

### **✅ ৩. স্ক্রিপ্ট রান করুন**
এখন স্ক্রিপ্টটি চালানোর জন্য নিচের কমান্ড দিন:

```bash
python virus.py
```
---

### **📌 ফাইল লুকানোর ধাপ:**
1. **প্রথমে একটি ছবি ফাইল (যেমন: `photo.jpg`) নির্বাচন করুন**  
2. **তারপর যে ফাইল লুকাতে চান (যেমন: `virus.bat`) তা নির্বাচন করুন**  
3. **নতুন ফাইলের নাম দিন (যেমন: `hidden_photo.jpg`)**  
4. **প্রসেস শেষ হলে, নতুন `hidden_photo.jpg` তৈরি হবে**  
5. **যদি এটি Windows-এ খোলা হয়, তাহলে লুকানো `.bat` ফাইল রান হবে।**

---

#### **✅ একটি নরমাল ফাইল লুকাতে:**  
```
python File-hide.py
```
📂 **Image file name (e.g. photo.jpg):** `my_photo.jpg`  
📂 **File to hide (e.g. secret.bat):** `my_script.bat`  
📂 **Output image name (e.g. hidden_photo.jpg):** `final_photo.jpg`


######***<~{{RH}}~>***######

### **📌 টুলস রান করার পরে কিভাবে ফটো সিলেক্ট করবেন?**  

আপনার টার্মিনালে যখন নিচের অপশন আসবে:  

```
📂 Image file name (e.g. photo.png):
📂 File to hide (e.g. file.bat):
📂 Output image name (e.g. final_photo.png):
```
তখন আপনি যে ফটো ব্যবহার করতে চান, তার **নাম এবং লোকেশন ঠিকমতো দিতে হবে।**  

---

### **🔥 উদাহরণ:**
#### **👉 যদি ফাইলগুলি Termux-এর `storage/shared` ফোল্ডারে থাকে:**
আপনার ফটো ও `.bat` ফাইল `storage/shared` ফোল্ডারে থাকলে, টার্মিনালে টাইপ করুন:  
```
📂 Image file name (e.g. photo.png): /data/data/com.termux/files/home/storage/shared/photo.png
📂 File to hide (e.g. file.bat): /data/data/com.termux/files/home/storage/shared/file.bat
📂 Output image name (e.g. final_photo.png): /data/data/com.termux/files/home/storage/shared/final_photo.png
```
> ⚠ **Termux-এর ফাইল এক্সেস পাওয়ার জন্য প্রথমে এই কমান্ড দিন:**
```
termux-setup-storage
```

---

### **🔹 কিভাবে জানবেন কোন ফটো কোথায় আছে?**
1. **Termux-এ ফাইল লোকেশন দেখতে `ls` কমান্ড দিন:**  
   ```
   ls /data/data/com.termux/files/home/storage/shared
   ```
   এতে `photo.png` এবং `file.bat` ফাইল আছে কি না দেখতে পারবেন।
   
2. **ফটো অন্য জায়গায় থাকলে, সেই লোকেশন দিয়ে দিন।**  
   - Example:  
     ```
     /sdcard/DCIM/photo.png
     /sdcard/Download/file.bat
     ```

---

### **💡 সংক্ষেপে:**  
✅ **যে ফটো ও `.bat` ফাইল ব্যবহার করতে চান, তার সঠিক লোকেশন লিখুন।**  
✅ **Termux-এর `storage/shared` ফোল্ডারে রাখলে সহজ হবে।**  
✅ **ফটো কোথায় আছে দেখতে `ls` কমান্ড ব্যবহার করুন।**  
✅ **`termux-setup-storage` কমান্ড দিয়ে ফাইল এক্সেস অনুমতি দিন।**  
---

### **✅ Windows-এ রান করার নিয়ম**
আপনার তৈরি করা **`final_photo.jpg`** Windows-এ **ক্লিক করলে ব্যাচ স্ক্রিপ্ট অটো রান হবে** এবং আপনার **.bat ফাইলের কোড এক্সিকিউট হবে।**

---

### **⚠️ গুরুত্বপূর্ণ নোট**  
✅ **শুধুমাত্র নিজের Windows সিস্টেমে টেস্ট করুন।**  
✅ **শিক্ষামূলক উদ্দেশ্যে ব্যবহার করুন।**  
✅ **অন্যদের ক্ষতি করার জন্য ব্যবহার করবেন না।**  

এখন আপনি এটি **Termux** থেকে ব্যবহার করতে পারবেন! 🚀
