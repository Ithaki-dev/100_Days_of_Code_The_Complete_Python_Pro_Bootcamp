# 📡 Internet Speed Complaint Bot

An automated tool that monitors your internet speed and automatically tweets complaints to your ISP when speeds fall below contracted levels. Fight for the internet speed you're paying for!

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Selenium](https://img.shields.io/badge/Selenium-4.0+-green)
![Twitter](https://img.shields.io/badge/Twitter-Automation-1DA1F2)
![Consumer Rights](https://img.shields.io/badge/Consumer-Rights-red)

## 🎯 Purpose

Hold your Internet Service Provider (ISP) accountable by automatically monitoring your internet speed and publicly documenting when they fail to deliver the speeds you're paying for.

### Why This Matters
- **Consumer Protection**: Document ISP performance failures
- **Public Accountability**: Create transparency around service quality
- **Data Collection**: Build evidence for contract disputes
- **Automated Advocacy**: Let technology fight for your rights

## 🌟 Features

### 🚀 Speed Testing
- **Automated Speed Tests**: Uses Speedtest.net for reliable measurements
- **Contract Comparison**: Compares results against your contracted speeds
- **Multiple Metrics**: Monitors both download and upload speeds
- **Threshold Detection**: Automatically identifies subpar performance

### 🐦 Social Media Integration
- **Automated Tweeting**: Posts complaints when speeds are inadequate
- **Public Documentation**: Creates a public record of service issues
- **ISP Tagging**: Direct public communication with your service provider
- **Multilingual Support**: Tweets in Spanish (easily customizable)

### 🤖 Full Automation
- **End-to-End Process**: From speed test to tweet posting
- **Selenium WebDriver**: Robust browser automation
- **Error Handling**: Graceful failure management
- **Scheduled Execution**: Can be set up to run at intervals

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Firefox browser
- GeckoDriver (Firefox WebDriver)
- Twitter account
- Internet connection (obviously! 😄)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/internet-speed-complaint-bot.git
   cd internet-speed-complaint-bot
   ```

2. **Create virtual environment:**
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

4. **Install GeckoDriver:**
   ```bash
   # Using conda
   conda install -c conda-forge geckodriver

   # Or download from: https://github.com/mozilla/geckodriver/releases
   ```

### Configuration

1. **Update your contract speeds:**
   ```python
   # In main.py
   my_contract_download_speed = 100  # Your contracted download speed in Mbps
   my_contract_upload_speed = 50     # Your contracted upload speed in Mbps
   ```

2. **Add your Twitter credentials:**
   ```python
   # Replace these lines with your actual credentials
   email_field.send_keys('your_email@example.com')
   username_field.send_keys('your_twitter_username')
   password_field.send_keys('your_twitter_password')
   ```

3. **Customize your tweet message:**
   ```python
   # Modify the tweet text (currently in Spanish)
   tweet_text = f"My download speed is {download_speed} Mbps, which is less than my contracted speed of {my_contract_download_speed} Mbps @YourISP #InternetSpeed"
   ```

## 📋 Usage Guide

### Basic Usage

1. **Run the bot:**
   ```bash
   python main.py
   ```

2. **Watch the automation:**
   - Browser opens and navigates to Speedtest.net
   - Speed test runs automatically (takes about 60 seconds)
   - Results are extracted and compared to your contract
   - If speeds are below threshold, Twitter login occurs
   - Complaint tweet is posted automatically

### Example Output
```
Download speed: 45.2 Mbps
Upload speed: 8.7 Mbps
Speed below contract threshold - posting complaint tweet...
Tweet posted successfully!
```

### Scheduled Automation

#### Using Cron (Linux/macOS)
```bash
# Check every hour
0 * * * * /path/to/venv/bin/python /path/to/main.py

# Check every 6 hours
0 */6 * * * /path/to/venv/bin/python /path/to/main.py
```

#### Using Task Scheduler (Windows)
1. Open Task Scheduler
2. Create Basic Task
3. Set trigger (daily, hourly, etc.)
4. Set action to run your Python script

## 🛠️ Technical Details

### Core Components

#### 1. Speed Testing Module
```python
# Automated speed test execution
driver.get("https://www.speedtest.net/")
go_button = driver.find_element(By.CLASS_NAME, "start-text")
go_button.click()
sleep(60)  # Wait for test completion
```

#### 2. Data Extraction
```python
# Extract speed measurements
download_speed = driver.find_element(By.CLASS_NAME, "download-speed").text
upload_speed = driver.find_element(By.CLASS_NAME, "upload-speed").text
download_speed = float(download_speed)
upload_speed = float(upload_speed)
```

#### 3. Twitter Automation
```python
# Automated tweet posting
if int(download_speed) < my_contract_download_speed:
    tweet = driver.find_element(By.CSS_SELECTOR, '[data-testid="tweetTextarea_0"]')
    tweet.send_keys(complaint_message)
    tweet_button.click()
```

### File Structure

```
day_51_twitter_bot/
├── main.py              # Main automation script
├── requirements.txt     # Python dependencies
├── config.py           # Configuration settings
├── README.md           # Project documentation
├── logs/
│   └── speed_tests.log # Speed test history
└── screenshots/
    └── evidence/       # Screenshot evidence
```

## 🔧 Configuration Options

### Contract Settings
```python
class InternetContract:
    def __init__(self):
        self.download_speed = 100    # Mbps
        self.upload_speed = 50       # Mbps
        self.provider_name = "@YourISP"
        self.tolerance = 0.8         # 80% of contracted speed
```

### Tweet Templates
```python
TWEET_TEMPLATES = {
    'english': "My internet speed is {speed} Mbps, below my contracted {contract} Mbps. {provider} #InternetSpeed #ConsumerRights",
    'spanish': "Mi velocidad de internet es {speed} Mbps, por debajo de mi contrato de {contract} Mbps. {provider} #VelocidadInternet",
    'custom': "Your custom tweet template here"
}
```

## 📊 Advanced Features

### Speed Test Logging
```python
import json
from datetime import datetime

def log_speed_test(download, upload, passed_contract):
    log_entry = {
        'timestamp': datetime.now().isoformat(),
        'download_speed': download,
        'upload_speed': upload,
        'contract_met': passed_contract,
        'tweet_posted': not passed_contract
    }
    
    with open('speed_test_log.json', 'a') as f:
        json.dump(log_entry, f)
        f.write('\n')
```

### Screenshot Evidence
```python
def capture_speed_test_evidence():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    screenshot_path = f"evidence/speedtest_{timestamp}.png"
    driver.save_screenshot(screenshot_path)
    return screenshot_path
```

### Enhanced Error Handling
```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def robust_element_click(driver, locator, timeout=10):
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()
        return True
    except Exception as e:
        print(f"Element interaction failed: {e}")
        return False
```

## 🐛 Troubleshooting

### Common Issues

#### 1. Speed Test Not Starting
```
Element 'start-text' not found
```
**Solutions:**
- Check if Speedtest.net UI has changed
- Update CSS selectors
- Increase wait times
- Clear browser cache

#### 2. Twitter Login Issues
```
Login failed or elements not found
```
**Solutions:**
- Verify Twitter credentials
- Check for 2FA (disable temporarily)
- Update Twitter element selectors
- Handle rate limiting

#### 3. Speed Values Not Extracted
```
ValueError: could not convert string to float
```
**Solutions:**
- Inspect Speedtest.net result page
- Update speed extraction selectors
- Handle different number formats
- Add data validation

#### 4. GeckoDriver Issues
```
WebDriverException: 'geckodriver' executable needs to be in PATH
```
**Solutions:**
- Install geckodriver: `conda install -c conda-forge geckodriver`
- Add to PATH manually
- Specify driver path in code

### Debug Mode
```python
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def debug_speed_test():
    logger.debug("Starting speed test...")
    # Add debug prints throughout the process
```

## 🔒 Security & Privacy

### Credential Management
```python
import os
from dotenv import load_dotenv

load_dotenv()

# Use environment variables instead of hardcoded credentials
twitter_email = os.getenv('TWITTER_EMAIL')
twitter_username = os.getenv('TWITTER_USERNAME')
twitter_password = os.getenv('TWITTER_PASSWORD')
```

### Environment File (.env)
```env
TWITTER_EMAIL=your_email@example.com
TWITTER_USERNAME=your_username
TWITTER_PASSWORD=your_secure_password
CONTRACT_DOWNLOAD_SPEED=100
CONTRACT_UPLOAD_SPEED=50
ISP_TWITTER_HANDLE=@YourISP
```

### Privacy Considerations
- **Public Tweets**: Complaints will be visible to everyone
- **Speed Data**: Consider if you want to share exact speeds
- **ISP Relations**: May affect customer service interactions
- **Legal**: Ensure compliance with local consumer protection laws

## 📈 Data Analytics

### Speed Test History Analysis
```python
import pandas as pd
import matplotlib.pyplot as plt

def analyze_speed_history():
    df = pd.read_json('speed_test_log.json', lines=True)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    
    # Plot speed trends
    plt.figure(figsize=(12, 6))
    plt.plot(df['timestamp'], df['download_speed'], label='Download Speed')
    plt.axhline(y=my_contract_download_speed, color='r', linestyle='--', label='Contract Speed')
    plt.title('Internet Speed Over Time')
    plt.legend()
    plt.show()
```

### Performance Metrics
```python
def calculate_contract_compliance():
    df = pd.read_json('speed_test_log.json', lines=True)
    compliance_rate = df['contract_met'].mean() * 100
    average_speed = df['download_speed'].mean()
    
    print(f"Contract compliance: {compliance_rate:.1f}%")
    print(f"Average speed: {average_speed:.1f} Mbps")
    print(f"Speed variance: {df['download_speed'].std():.1f} Mbps")
```

## ⚖️ Legal Considerations

### Consumer Rights
- **Service Level Agreements**: Document contract violations
- **Evidence Collection**: Maintain records for disputes
- **Regulatory Complaints**: Data for filing with regulators
- **Public Accountability**: Transparency in service delivery

### Terms of Service
- **Twitter ToS**: Ensure compliance with automation policies
- **Speedtest.net**: Respect their usage terms
- **ISP Contracts**: Understand your service agreement

### Best Practices
- **Accurate Reporting**: Only complain about legitimate issues
- **Professional Tone**: Keep tweets factual and respectful
- **Documentation**: Maintain logs for potential legal needs
- **Rate Limiting**: Don't spam or abuse the automation

## 🚀 Enhanced Features

### Multi-ISP Support
```python
ISP_HANDLES = {
    'comcast': '@comcast',
    'verizon': '@verizon',
    'att': '@att',
    'spectrum': '@getspectrum'
}
```

### Speed Test Alternatives
```python
def run_multiple_speed_tests():
    """Run tests on multiple platforms for verification"""
    platforms = [
        'https://www.speedtest.net/',
        'https://fast.com/',
        'https://speedof.me/'
    ]
    # Implement multiple testing for accuracy
```

### Notification Systems
```python
import smtplib
from email.mime.text import MIMEText

def send_email_alert(speed_data):
    """Send email notification about speed issues"""
    msg = MIMEText(f"Internet speed dropped to {speed_data['download']} Mbps")
    # Email implementation
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines
- Follow consumer advocacy principles
- Ensure accuracy in speed reporting
- Add comprehensive error handling
- Include tests for critical functions
- Document configuration options

## 📚 Resources

### Consumer Rights
- [FCC Speed Test](https://www.fcc.gov/consumer-guides/broadband-speed-guide)
- [Consumer Broadband Test](https://www.measurementlab.net/)
- [File ISP Complaints](https://consumercomplaints.fcc.gov/)

### Technical Resources
- [Selenium Documentation](https://selenium-python.readthedocs.io/)
- [Twitter Developer Docs](https://developer.twitter.com/)
- [Speed Test APIs](https://www.speedtest.net/apps/cli)

## 📞 Support

For technical issues:
1. Check the troubleshooting section
2. Verify element selectors are current
3. Test internet connection manually
4. Review browser console for errors

For consumer rights questions:
- Contact your local consumer protection agency
- File complaints with telecommunications regulators
- Consult with consumer advocacy groups

## 🎓 Learning Objectives

This project demonstrates:
- **Consumer Advocacy**: Using technology for consumer rights
- **Web Automation**: Advanced Selenium WebDriver usage
- **Data Collection**: Automated monitoring and logging
- **Social Media Automation**: Programmatic posting
- **Error Handling**: Robust automation practices
- **Scheduling**: Task automation and cron jobs

---

**Fight for the internet speed you deserve!** 📡⚡

*This project is part of Day 51 of the 100 Days of Code: The Complete Python Pro Bootcamp - Consumer Advocacy Automation.*
