# Selenium and Browser Automation

[Back to the question-bank index](../README.md)

## What is Selenium?

**Answer**

Selenium is a browser-automation project commonly used for end-to-end web testing:

- **WebDriver** controls a browser through a standard automation API.
- **Selenium Grid** distributes tests across browser, operating-system, and machine combinations.
- **Selenium IDE** records and replays browser interactions for simpler workflows.

Selenium RC is obsolete and was replaced by WebDriver. Selenium integrates with test frameworks
such as JUnit, TestNG, NUnit, and pytest, but Selenium itself does not define the complete test
architecture, assertions, fixtures, reporting, or CI pipeline.

## Why should fixed sleeps normally be avoided in browser tests?

**Answer**

`Thread.sleep` always waits for the full duration. A short delay can make a test flaky when the page
is slow, while a long delay makes every successful run unnecessarily slow. Prefer an explicit wait
for a meaningful condition, such as an element becoming visible or clickable.

An implicit wait applies globally to element lookup. An explicit wait applies to a particular
condition. Mixing the two can create unpredictable total wait times, so teams generally standardize
on explicit waits for dynamic user interfaces. A fixed sleep can still be useful in a narrowly
diagnostic test, but it should not be the normal synchronization strategy.

## What is the difference between `findElement` and `findElements`?

**Answer**

- `findElement(locator)` returns the first matching `WebElement` and throws
  `NoSuchElementException` when there is no match.
- `findElements(locator)` returns every match as a list and returns an empty list when there is no
  match.

Use `findElements` when zero matches are a valid state or when every matching element is needed.

## What are XPath axes used for?

**Answer**

XPath axes select nodes relative to a context node. Common axes include `child`, `parent`,
`ancestor`, `descendant`, `following-sibling`, and `preceding-sibling`. They are useful when a stable
relationship exists but the target has no reliable ID or test attribute. Prefer simple, stable
locators such as semantic test IDs when the application can provide them; long DOM-dependent XPath
expressions are fragile during UI refactoring.

## Name common Selenium Java interfaces and locator types.

**Answer**

`WebDriver`, `WebElement`, `JavascriptExecutor`, and `TakesScreenshot` are commonly used interfaces.
`SearchContext` is the parent search abstraction implemented by `WebDriver` and `WebElement`.
`By` is a locator class rather than an interface; it creates locators such as `By.id`, `By.cssSelector`,
and `By.xpath`.

For a native HTML `<select>`, wrap the located element in Selenium's `Select` helper and choose by
visible text, value, or index. A custom JavaScript dropdown is not a native `<select>` and must be
handled by clicking its controls and waiting for its options.

## How would you automate a dropdown with Selenium WebDriver?

**Answer**

First inspect whether the control is a native HTML `<select>` or a custom component. For a native
control, locate it with a stable selector and use Selenium's `Select` helper:

```java
WebElement element = wait.until(
    ExpectedConditions.elementToBeClickable(By.id("travelClass"))
);
Select dropdown = new Select(element);
dropdown.selectByVisibleText("First Class");
```

For a custom dropdown, click the trigger, explicitly wait for the option list, then click the option
using a stable role, label, or test attribute. Do not assume a third-party travel site keeps the same
DOM or locator. Verify the selected value and keep external-site automation within its terms of use.

## Which Selenium exceptions are common, and what do they indicate?

**Answer**

- `NoSuchElementException`: no element matched the locator.
- `TimeoutException`: an explicit condition did not become true in time.
- `StaleElementReferenceException`: the DOM changed and a stored element reference is no longer valid.
- `ElementNotInteractableException`: the element exists but cannot currently receive the action.
- `ElementClickInterceptedException`: another element would receive the click.
- `NoSuchFrameException` or `NoSuchWindowException`: the requested browsing context does not exist.
- `InvalidSelectorException`: the CSS or XPath selector is invalid.
- `WebDriverException`: a broader driver, browser, or session failure.

The best response is not a blanket retry. Determine whether the locator, page state, synchronization,
or browser session is wrong, then retry only operations that are safe and expected to be transient.

## References

- [Selenium documentation](https://www.selenium.dev/documentation/)
- [Selenium waits](https://www.selenium.dev/documentation/webdriver/waits/)
- [Selenium Java API](https://www.selenium.dev/selenium/docs/api/java/)
