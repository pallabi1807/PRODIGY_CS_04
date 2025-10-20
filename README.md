# 🧩 Basic Keylogger Program 

## 🎯 Aim  
Create a basic keylogger program that records and logs keystrokes. Focus on logging the keys pressed and saving them to a file.  
**Note:** Ethical considerations and permissions are crucial for projects involving keyloggers.

---

## 🧠 Objective  
- To understand how keyboard input events can be captured programmatically using Python and Tkinter.  
- To log and store keystrokes in a structured format (text file) for educational or authorized monitoring purposes.  
- To emphasize the **ethical**, **legal**, and **privacy** aspects of using keyloggers responsibly.  
- To demonstrate proper logging, timestamping, and secure file-handling techniques.  

---

## 🏢 Internship Task  
This project is part of the **Prodigy InfoTech Internship Program (Cybersecurity Domain)**.  
It was developed as a practical task to explore **ethical monitoring tools** and understand how keylogging mechanisms work in cybersecurity contexts.

---

## ⚙️ Implementation Details  
- **UI framework:** `tkinter` (Python standard library) — the app shows a visible window and a text box for typing.  
- **Log file:** `keypress_log` (file is created automatically).  
- **Timestamping:** All keystrokes are timestamped in UTC (ISO-8601 format).  
- **Scope:** The keylogger records only while the Tkinter window is focused (no system-wide/global hooks).  
- **Stop / Control:** The UI shows status and provides buttons to clear the log or open the logs folder.

---

## 🚀 Features  
- Real-time keystroke capture while app is focused  
- Timestamped logging in `keypress_log.txt`  
- Visible UI that indicates logging status (not hidden)  
- Clean file writes with flushing/fsync to reduce data loss  
- Cross-platform behavior for opening the logs folder (Windows/macOS/Linux)  

---

## 🔄 Algorithm / Logic  
1. Create the `logs` directory if it does not exist.  
2. When a key is pressed while the Tkinter window is focused, format an ISO-8601 UTC timestamp and the key info.  
3. Append the timestamped record to `keypress_log.txt` (flush + fsync).  
4. Show the last pressed key and timestamp in the UI status bar.  
5. Provide controls to clear the log file or open the log folder.

---

## 🧩 Program Behavior (summary)  
- The application binds to `<Key>` events using `root.bind_all("<Key>", on_key)`.  
- It only logs keys while the window is focused — a guard check is performed inside the handler.  
- The `clear` button removes the log file, and the `Open Logs Folder` button opens the folder in the OS file browser.

---

## 📄 Sample Output (`logs/keloogerlog.txt`)
2025-10-20T12:00:05Z keysym=h char='h'
2025-10-20T12:00:06Z keysym=e char='e'
2025-10-20T12:00:06Z keysym=l char='l'
2025-10-20T12:00:07Z keysym=l char='l'
2025-10-20T12:00:07Z keysym=o char='o'


---

## ⚠️ Ethical Warning  
This program is **strictly for educational purposes** and **must only be used with full, informed consent** of the user whose keyboard input is being recorded. Unauthorized keylogging is **illegal** and unethical.  
- Avoid logging passwords, PINs, or other sensitive fields.  
- Secure logs (restrict file permissions) and delete them after testing.  
- Comply with local laws and institutional policies.

---

## 📘 Project Justification  
This project supports learning about:
- How input capture works at the application level,
- Logging best practices (timestamping, safe writes),
- Ethical responsibilities and detection/mitigation of malicious keyloggers.

---

## 🧾 Conclusion & Future Scope  
- The project demonstrates a safe, visible, in-app keylogger used for authorized testing and learning.  
- Future improvements: add encrypted log storage, log rotation, an explicit consent dialog, or anonymized analytics instead of raw keystrokes.

---

## 👩‍💻 Author  
**Pallabi Poria**  
MCA Student | Cybersecurity Enthusiast  
Task completed under **Prodigy InfoTech Internship**
