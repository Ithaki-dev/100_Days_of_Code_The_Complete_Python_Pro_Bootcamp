# 💰 Amazon Price Tracker

A Python-based automated price monitoring tool that tracks Amazon product prices and sends email alerts when prices drop below your specified threshold. Never miss a deal again!

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Web Scraping](https://img.shields.io/badge/Web%20Scraping-BeautifulSoup-orange)
![Email](https://img.shields.io/badge/Email-SMTP-green)
![Amazon](https://img.shields.io/badge/Amazon-Price%20Tracker-yellow)

## 🌟 Features

### 📊 Price Monitoring
- **Real-time Price Tracking**: Scrapes current prices from Amazon product pages
- **Customizable Thresholds**: Set your desired price alert level
- **Automated Checking**: Can be scheduled to run periodically
- **Price History**: Track price changes over time

### 📧 Smart Notifications
- **Email Alerts**: Instant notifications when prices drop
- **Gmail Integration**: Secure SMTP email sending via Gmail
- **Custom Messages**: Personalized alert messages with current price
- **Multiple Recipients**: Send alerts to multiple email addresses

### 🛡️ Robust Scraping
- **Browser Mimicking**: Uses realistic User-Agent headers to avoid blocking
- **Anti-Detection**: Implements best practices for web scraping
- **Error Handling**: Graceful handling of network issues and page changes
- **Flexible Parsing**: Adaptable to Amazon's page structure changes

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Gmail account (for sending email alerts)
- Gmail App Password (for secure authentication)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/amazon-price-tracker.git
   cd amazon-price-tracker
   ```

2. **Create and activate virtual environment:**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

### Gmail Setup

1. **Enable 2-Factor Authentication:**
   - Go to [Google Account Security](https://myaccount.google.com/security)
   - Enable 2-Step Verification

2. **Generate App Password:**
   - Go to Google Account settings
   - Security → 2-Step Verification → App passwords
   - Select "Mail" and generate a 16-character password
   - Save this password for the `.env` file

3. **Create environment file:**
   ```bash
   # Create .env file in project root
   touch .env
   ```

4. **Add your credentials to .env:**
   ```env
   MY_EMAIL=your_gmail@gmail.com
   PASSWORD=your_16_character_app_password
   TO_EMAIL=recipient@email.com
   ```

### Configuration

1. **Set your target product:**
   - Replace the Amazon URL in `main.py` with your desired product
   - Update the price threshold in the main execution block

2. **Test the setup:**
   ```bash
   python main.py
   ```

## 📋 Usage Guide

### Basic Usage

1. **Run the tracker:**
   ```bash
   python main.py
   ```

2. **Expected output:**
   ```
   Current price: $89.99
   Price Drop Alert sent!
   ```
   OR
   ```
   Current price: $120.50
   Price is above the threshold, the current price is: 120.5
   ```

### Advanced Usage

#### Custom Price Threshold
```python
# In main.py, modify the threshold
if price and price < 75:  # Alert when price drops below $75
    send_email(price)
```

#### Multiple Products
```python
products = [
    {
        "url": "https://www.amazon.com/dp/PRODUCT1",
        "threshold": 100,
        "name": "Product 1"
    },
    {
        "url": "https://www.amazon.com/dp/PRODUCT2", 
        "threshold": 50,
        "name": "Product 2"
    }
]

for product in products:
    price = find_price(product["url"])
    if price and price < product["threshold"]:
        send_email(price, product["name"])
```

#### Scheduled Monitoring
```bash
# Using cron (Linux/macOS) - check every hour
0 * * * * /path/to/venv/bin/python /path/to/main.py

# Using Task Scheduler (Windows)
# Create a task that runs main.py at your desired interval
```

## 🛠️ Technical Details

### Dependencies

```python
import requests              # HTTP requests for web scraping
import smtplib               # Email sending functionality
import os                    # Environment variable access
from dotenv import load_dotenv  # Environment file management
from bs4 import BeautifulSoup   # HTML parsing
from pprint import pprint       # Debug output formatting
```

### Core Functions

#### 1. Price Scraping
```python
def find_price():
    """Fetches current price from Amazon product page"""
    # Uses anti-detection headers
    # Parses HTML with BeautifulSoup
    # Extracts price from specific elements
    # Returns float value or None
```

#### 2. Email Notifications
```python
def send_email(price):
    """Sends price alert via Gmail SMTP"""
    # Connects to Gmail SMTP server
    # Authenticates with app password
    # Sends formatted price alert
```

### File Structure

```
day_47_price_tracker/
├── main.py              # Main application script
├── .env                 # Environment variables (create this)
├── requirements.txt     # Python dependencies
├── README.md           # Project documentation
└── logs/               # Optional: store price history
    └── price_log.txt
```

## 🔧 Configuration Options

### Environment Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `MY_EMAIL` | Your Gmail address | `your.email@gmail.com` |
| `PASSWORD` | Gmail app password | `abcd efgh ijkl mnop` |
| `TO_EMAIL` | Alert recipient email | `alerts@email.com` |

### Customizable Parameters

#### Price Threshold
```python
PRICE_THRESHOLD = 100  # Alert when price drops below $100
```

#### Product URL
```python
PRODUCT_URL = "https://www.amazon.com/dp/YOUR_PRODUCT_ID"
```

#### Email Template
```python
subject = "Price Drop Alert!"
body = f"The price has dropped to ${price}! Time to buy!"
```

## 🎯 How It Works

### 1. Web Scraping Process
```
Amazon Product Page → HTTP Request → HTML Response → BeautifulSoup Parser → Price Extraction
```

### 2. Price Comparison Logic
```
Current Price → Compare with Threshold → If Lower → Send Email Alert
```

### 3. Email Alert Flow
```
Price Drop Detected → Format Message → SMTP Connection → Send Email → Close Connection
```

### Amazon Page Structure
The scraper targets specific CSS classes:
- **Price Element**: `span.a-price-whole`
- **Index Selection**: Uses the 3rd element (index 2) from the found elements
- **Price Cleaning**: Removes commas and converts to float

## 🐛 Troubleshooting

### Common Issues

#### 1. Price Not Found
```
Price not found
```
**Causes:**
- Amazon changed their page structure
- Product page layout differs from expected
- Page didn't load properly

**Solutions:**
- Inspect the Amazon page and update CSS selectors
- Check if the product URL is correct
- Verify internet connection

#### 2. Email Authentication Failed
```
SMTPAuthenticationError: Username and Password not accepted
```
**Solutions:**
- Verify Gmail app password is correct (16 characters)
- Ensure 2-Factor Authentication is enabled
- Check email address in `.env` file
- Try generating a new app password

#### 3. Blocked by Amazon
```
HTTP 503 or 403 errors
```
**Solutions:**
- Add delays between requests
- Rotate User-Agent strings
- Use proxy servers
- Implement session management

#### 4. Environment Variables Not Loaded
```
AttributeError: 'NoneType' object has no attribute
```
**Solutions:**
- Ensure `.env` file exists in project root
- Check variable names match exactly
- Verify `load_dotenv()` is called before accessing variables

## 🔒 Security & Privacy

### Data Protection
- **No Data Storage**: Prices are processed in memory only
- **Secure Authentication**: Uses Gmail app passwords
- **Environment Variables**: Credentials stored securely in `.env`
- **No Tracking**: No user data collection or storage

### Best Practices
- **Rate Limiting**: Implement delays between requests
- **User-Agent Rotation**: Vary request headers
- **Error Handling**: Graceful failure management
- **Logging**: Optional price history logging

## 🚀 Advanced Features

### Price History Logging
```python
import datetime
import json

def log_price(price, product_name):
    log_entry = {
        "timestamp": datetime.datetime.now().isoformat(),
        "product": product_name,
        "price": price
    }
    with open("price_history.json", "a") as f:
        json.dump(log_entry, f)
        f.write("\n")
```

### Multiple Price Thresholds
```python
THRESHOLDS = {
    "urgent": 80,    # Immediate buy
    "good": 100,     # Good deal
    "watch": 120     # Keep watching
}
```

### Webhook Integration
```python
import requests

def send_webhook(price, product_name):
    webhook_url = "https://hooks.slack.com/your-webhook"
    payload = {
        "text": f"Price alert: {product_name} is now ${price}!"
    }
    requests.post(webhook_url, json=payload)
```

## 📊 Monitoring & Analytics

### Price Tracking Dashboard
```python
import matplotlib.pyplot as plt
import pandas as pd

def plot_price_history():
    df = pd.read_json("price_history.json", lines=True)
    plt.plot(df['timestamp'], df['price'])
    plt.title('Price History')
    plt.xlabel('Date')
    plt.ylabel('Price ($)')
    plt.show()
```

### Statistics
```python
def price_statistics():
    df = pd.read_json("price_history.json", lines=True)
    return {
        "average": df['price'].mean(),
        "lowest": df['price'].min(),
        "highest": df['price'].max(),
        "current": df['price'].iloc[-1]
    }
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines
- Follow PEP 8 style guidelines
- Add docstrings for all functions
- Include error handling
- Test with different Amazon products
- Respect robots.txt and rate limits

## 📈 Future Enhancements

- [ ] **Web Interface**: Create a web dashboard for monitoring multiple products
- [ ] **Database Storage**: Store price history in SQLite/PostgreSQL
- [ ] **Multiple Retailers**: Support for other e-commerce sites
- [ ] **Mobile Notifications**: Push notifications via mobile apps
- [ ] **Price Prediction**: ML models for price trend prediction
- [ ] **Bulk Monitoring**: Monitor hundreds of products simultaneously
- [ ] **API Integration**: RESTful API for external integrations
- [ ] **Docker Support**: Containerized deployment
- [ ] **Cloud Deployment**: Deploy on AWS/Heroku with scheduled tasks
- [ ] **Advanced Alerts**: SMS, Slack, Discord notifications

## 📝 Legal Considerations

### Terms of Service
- **Respect robots.txt**: Follow website crawling guidelines
- **Rate Limiting**: Don't overload servers with requests
- **Personal Use**: Intended for personal price monitoring only
- **No Commercial Use**: Don't use for commercial scraping operations

### Disclaimer
This tool is for educational and personal use only. Users are responsible for:
- Complying with Amazon's Terms of Service
- Respecting website rate limits
- Using scraped data ethically
- Maintaining account security

## 📞 Support

If you encounter issues:

1. Check the [Troubleshooting](#🐛-troubleshooting) section
2. Verify your [Gmail setup](#gmail-setup)
3. Test with a simple Amazon product URL
4. Create an issue with detailed error messages

## 🎓 Learning Objectives

This project demonstrates:
- **Web Scraping**: Data extraction from dynamic websites
- **HTTP Requests**: Working with headers and sessions
- **Email Automation**: SMTP protocol and Gmail integration
- **Environment Management**: Secure credential storage
- **Error Handling**: Robust exception management
- **Data Processing**: String manipulation and type conversion
- **Automation**: Scheduled task execution

---

**Start tracking your favorite products today!** 💰📊

*This project is part of Day 47 of the 100 Days of Code: The Complete Python Pro Bootcamp.*
