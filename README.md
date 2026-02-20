# Automation-OrangeHRM | POM-Based Testing Framework

A comprehensive test automation framework for OrangeHRM using **Page Object Model (POM)** design pattern with Playwright, API testing, and Database testing.

## 📁 Project Structure

```
Automation-OrangeHRM/
├── config/                 # Configuration management
│   └── config.py          # Config class with environment variables
├── pages/                 # Page Object Models
│   ├── base_page.py       # Base page with common methods
│   ├── login_page.py      # Login page object
│   ├── dashboard_page.py  # Dashboard page object
│   └── __init__.py
├── tests/                 # Test suites
│   ├── ui/                # UI/Playwright tests
│   │   ├── test_login.py
│   │   └── test_dashboard.py
│   ├── api/               # API tests
│   │   └── test_api.py
│   ├── database/          # Database tests
│   │   └── test_database.py
│   ├── conftest.py        # Pytest fixtures and configuration
│   └── __init__.py
├── utils/                 # Utilities
│   ├── logger.py          # Logging configuration
│   ├── database.py        # Database connection handler
│   ├── api_client.py      # Reusable API client
│   └── __init__.py
├── reports/               # Test reports and logs
├── requirements.txt       # Python dependencies
├── pytest.ini            # Pytest configuration
├── .env                  # Environment variables (git ignored)
├── .gitignore           # Git ignore rules
└── README.md            # This file
```

## ✨ Key Features

- **Page Object Model (POM)**: Clean and maintainable test structure
- **Async/Await Support**: Using pytest-asyncio for async Playwright tests
- **Reusable Fixtures**: Conftest fixtures for browser, page, and authenticated sessions
- **API Testing**: Ready-to-use API client for endpoint testing
- **Database Testing**: MySQL integration for data validation
- **Allure Reports**: Beautiful test execution reports
- **Logging**: Comprehensive logging at file and console levels
- **Environment Configuration**: .env file support for secured credentials

## 🚀 Quick Start

### 1. Setup Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # macOS/Linux
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
playwright install  # Install browser binaries
```

### 3. Configure Environment
Update `.env` with your credentials:
```env
BASE_URL=https://opensource-demo.orangehrm.com
MYSQL_HOST=127.0.0.1
MYSQL_USER=root
MYSQL_PASSWORD=your_password
MYSQL_DATABASE=orangehrm
```

### 4. Run Tests

**All tests:**
```bash
pytest
```

**By marker:**
```bash
pytest -m ui              # UI tests only
pytest -m api             # API tests only
pytest -m database        # Database tests only
pytest -m smoke           # Smoke tests
```

**With Allure report:**
```bash
pytest --alluredir=reports/allure-results
allure serve reports/allure-results
```

**Specific test file:**
```bash
pytest tests/ui/test_login.py -v
```

## 📝 Page Object Model (POM) Pattern

### BasePage
All page objects inherit from `BasePage` which provides common methods:
- `navigate_to(url)` - Navigate to URL
- `click(locator)` - Click element
- `fill(locator, text)` - Fill input
- `get_text(locator)` - Get text from element
- `wait_for_element(locator)` - Wait for element visibility
- `take_screenshot(filename)` - Take screenshot

### Example: LoginPage
```python
class LoginPage(BasePage):
    USERNAME_INPUT = "//input[@name='username']"
    PASSWORD_INPUT = "//input[@name='password']"
    LOGIN_BUTTON = "//button[@type='submit']"
    
    async def login(self, username: str, password: str):
        await self.enter_username(username)
        await self.enter_password(password)
        await self.click_login()
```

### Using in Tests
```python
async def test_login(page, login_page):
    await page.goto(Config.BASE_URL)
    await login_page.login("Admin", "admin123")
    assert "/dashboard" in page.url
```

## 🔧 Available Fixtures

From `conftest.py`:

- **`browser`** - Playwright browser instance
- **`page`** - Playwright page instance
- **`login_page`** - LoginPage object
- **`dashboard_page`** - DashboardPage object
- **`authenticated_page`** - Pre-authenticated page (logged in)
- **`authenticated_dashboard`** - Pre-authenticated dashboard
- **`db_connection`** - Database connection
- **`api_client`** - API client instance

## 📊 Test Markers

Use pytest markers to organize tests:
```python
@pytest.mark.ui
async def test_login():
    pass

@pytest.mark.api
def test_api_endpoint():
    pass

@pytest.mark.database
def test_db_query():
    pass

@pytest.mark.smoke
def test_critical_flow():
    pass
```

## 🗄️ Database Testing

Connect to database and execute queries:
```python
def test_user_data(db_connection):
    results = db_connection.fetch_query(
        "SELECT * FROM EmployeeTable WHERE emp_id = 1"
    )
    assert len(results) > 0
```

## 🌐 API Testing

Make API requests:
```python
def test_api_get(api_client):
    response = api_client.get("/employees")
    assert response.status_code == 200
```

## 📋 Logging

Automatic logging in:
- Console output (`INFO` level)
- File: `reports/logs/test_YYYYMMDD_HHMMSS.log` (`DEBUG` level)

```python
from utils.logger import get_logger

logger = get_logger(__name__)
logger.info("Test step")
logger.error("Error message")
```

## 🔐 Environment Variables

The `.env` file is **git-ignored** for security. Never commit credentials:
```env
HEADLESS=True
BROWSER_TYPE=chromium
BASE_URL=https://opensource-demo.orangehrm.com
MYSQL_HOST=127.0.0.1
MYSQL_PORT=3306
MYSQL_USER=root
MYSQL_PASSWORD=your_password
MYSQL_DATABASE=orangehrm
API_BASE_URL=https://opensource-demo.orangehrm.com/api
API_TIMEOUT=30
```

## 📈 Allure Reports

Generate and view detailed reports:
```bash
# Generate report
pytest --alluredir=reports/allure-results

# View report
allure serve reports/allure-results
```

## 🛠️ Adding New Tests

1. **Create Page Object** (if UI test):
   ```python
   # pages/employees_page.py
   class EmployeesPage(BasePage):
       EMPLOYEE_LIST = "//table[@id='employee-list']"
   ```

2. **Create Test File**:
   ```python
   # tests/ui/test_employees.py
   @pytest.mark.ui
   async def test_employee_search(page, employees_page):
       pass
   ```

3. **Run Test**:
   ```bash
   pytest tests/ui/test_employees.py -v
   ```

## 📞 Support

For issues or questions:
1. Check the console logs
2. Review test logs in `reports/logs/`
3. Check generated screenshots in `reports/screenshots/`

## 📄 License

This project is for educational purposes.
