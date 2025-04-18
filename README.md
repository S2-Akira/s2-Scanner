# 🔍 Open Port Scanner

A simple and effective Python-based port scanner that scans for open TCP ports on a target host. Built for educational and ethical use only.

## 🚀 Features

- Fast, multi-threaded scanning
- Customizable port ranges
- Easy-to-read output
- Lightweight and dependency-free
- Cross-platform (macOS, Linux, Windows)

## 🛠️ Technologies Used

- Python 3
- `socket` module
- `threading` module

## 📦 Requirements

- Python 3.6 or higher

## 📥 Installation

Clone the repo:

```bash
git clone https://github.com/yourusername/open-port-scanner.git
cd open-port-scanner
(Optional) Create a virtual environment:

bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
⚙️ Usage
bash
Copy
Edit
python scanner.py --host 192.168.1.1 --start 1 --end 1024 --threads 100
Arguments

Argument	Description
--host	Target IP or domain
--start	Start of port range (default: 1)
--end	End of port range (default: 65535)
--threads	Number of threads (default: 100)
Example:

bash
Copy
Edit
python scanner.py --host scanme.nmap.org --start 20 --end 100
⚠️ Disclaimer
This tool is for educational and authorized testing only. Scanning hosts without permission is illegal and unethical. Always get proper authorization before using this tool.

🧑‍💻 Author
Your Name

📄 License
This project is licensed under the MIT License — see the LICENSE file for details.

yaml
Copy
Edit

---

Let me know if you'd like:
- A sample `LICENSE` file (MIT)
- To turn this into a real GitHub repository setup
- To add emojis/styling for a cooler vibe 😎
