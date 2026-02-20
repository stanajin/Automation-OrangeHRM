# Automation-OrangeHRM | POM-Based Testing Framework

## Project Overview
A professional test automation framework for OrangeHRM using Page Object Model (POM) design pattern, built with Playwright, Pytest, and supporting API/Database testing.

## Architecture

### Page Object Model Design
- **BasePage**: Foundation class with common methods (click, fill, navigate, etc.)
- **Specific Pages**: LoginPage, DashboardPage (inherit from BasePage)
- **Tests**: Clean test files using page objects without direct selectors

### Technology Stack
- **Playwright**: Browser automation (async/await support)
- **Pytest**: Test framework with fixtures and markers
- **Requests**: API testing
- **MySQL**: Database testing and validation
- **Allure**: Test reporting
- **Python-dotenv**: Secure credentials management

## Key Features
1. **POM Pattern**: Maintainable, reusable page objects
2. **Async Testing**: pytest-asyncio with Playwright
3. **Reusable Fixtures**: Browser, page, database, API client fixtures
4. **Logging**: File and console logging with timestamps
5. **Environment Config**: .env-based configuration
6. **Test Markers**: @pytest.mark.ui, @pytest.mark.api, @pytest.mark.database
7. **Allure Reports**: Beautiful HTML reports

## Project Structure
```
config/          → Configuration and environment variables
pages/           → Page Object Models (BasePage, LoginPage, DashboardPage)
tests/           → Test suites organized by type (ui, api, database)
utils/           → Shared utilities (logger, database, API client)
reports/         → Test results, logs, and screenshots
```

## Development Guidelines
1. Always use Page Objects for UI tests (no hardcoded selectors in tests)
2. Inherit from BasePage to reuse common methods
3. Mark tests with appropriate decorators (@pytest.mark.ui, etc.)
4. Use fixtures from conftest.py for setup/teardown
5. Add logging for better debugging
6. Keep locators private (_LOCATOR_NAME) or public (LOCATOR_NAME)
7. Use async/await for Playwright tests

## Running Tests
- All: `pytest`
- UI only: `pytest -m ui`
- API only: `pytest -m api`
- Database only: `pytest -m database`
- With report: `pytest --alluredir=reports/allure-results && allure serve reports/allure-results`
