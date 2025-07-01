# Genlayerlabs

**Auto Join and Connect**

---

## About The Project

Genlayerlabs is an automation script designed to automatically join and connect to the Genlayer Labs platform. This tool simplifies the process of interacting with the platform by automating user actions such as joining quests or events and connecting wallets.

---

## Features

- Automatically navigates to the Genlayer Labs platform
- Automates the join process
- Automates wallet connection (manual wallet approval required)
- Headless browser support for automation environments

---

## Getting Started

### Prerequisites

- Python 3.6 or higher
- Pyppeteer for browser automation

### Installation

1. Clone the repository:

   ```
   git clone https://github.com/Luizfelippe00966/Genlayerlabs.git
   cd Genlayerlabs
   ```

2. Install dependencies:

   ```
   pip install pyppeteer
   ```

---

## Usage

Run the automation script:

```
python auto_join_connect.py
```

This will launch a Chromium browser, navigate to the Genlayer Labs platform, and perform automated join and connect actions.

> **Note:** Wallet connection and transaction approvals require manual confirmation in your wallet extension popup.

---

## Customization

- Update CSS selectors in the script to match any changes in the Genlayer Labs UI.
- Adjust wait times depending on network speed and transaction confirmation times.
- Extend the script to support additional features as needed.

---

## Contributing

Contributions are welcome! Please open issues or submit pull requests for bug fixes, improvements, or new features.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
