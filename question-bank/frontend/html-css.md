# HTML and CSS

Semantic HTML, layout, styling, browser behavior, accessibility, and responsive design.

[Back to the question-bank index](../README.md)

## What is the difference between block-level and inline elements in HTML?

**Answer**

Block-Level Elements: Used for larger sections of content, such as paragraphs, headings, lists, and sections. They help in creating the overall structure of the webpage.
Characteristics:
Width and Height: Block-level elements respect the width and height properties. By default, they take up the full width of their container.
Margin and Padding: Margins and padding can be applied on all four sides (top, right, bottom, left) and will affect the layout as expected.
Display Property: The default display property for block-level elements is block.
Positioning: Block-level elements can be positioned using CSS properties like position, top, right, bottom, left, float, and clear.
Examples: <div>, <p>, <h1> to <h6>, <ul>, <ol>, <table>, <header>, <footer>, <section>, <article>, and <nav>.
Inline Elements: Used for smaller pieces of content within block-level elements, such as links, emphasized text, and images. They help format and style specific parts of the content without disrupting the flow.
Characteristics:
Width and Height: Inline elements do not respect the width and height properties. They take up only as much width as necessary to fit their content.
Margin and Padding: Margins and padding can be applied, but only the horizontal (left and right) margins and padding will affect the layout. Vertical (top and bottom) margins and padding will not push other elements away.
Display Property: The default display property for inline elements is inline.
Positioning: Inline elements can be positioned using position, but they do not respond to float and clear properties in the same way block-level elements do.
Examples: <span>, <a>, <img>, <strong>, <b>, <em>, <i>, <code>, <br>, and <input>.

## What is z-index?

**Answer**

z-index Property: Controls the stacking order of elements along the z-axis.
Positioning Context: Works on elements with position set to relative, absolute, fixed, or sticky.
Stacking Context: Formed when an element is positioned and has a z-index value other than auto.
Default Value: auto, meaning the element follows the default stacking order.
Integer Values: Accepts both positive and negative integer values.
Nested Stacking Contexts: Stacking contexts can be nested, and z-index values are relative within their respective contexts.

## What is the difference between display: none and visibility: hidden?

**Answer**

Effect on Layout:
display: none: Element is removed from the document flow.
visibility: hidden: Element remains in the document flow.
Space Occupied:
display: none: Does not occupy any space.
visibility: hidden: Occupies space.
Rendering:
display: none: Element and its children are not rendered.
visibility: hidden: Element and its children are rendered but not visible.
Use Cases:
display: none: Hiding elements without affecting layout.
visibility: hidden: Hiding elements while preserving layout.

## How do you display an image without using the <img> tag?

**Answer**

HTML: A <div> element with a class of image-container is used to hold the image.
CSS: The .image-container class is styled to set the background-image property to the URL of the image. The background-size: cover property ensures that the image covers the entire container, and background-position: center centers the image within the container.

## What is the use of flex and grid in CSS?

**Answer**

Flexbox (Flexible Box Layout) is designed for one-dimensional layouts, either in a row or a column. It is useful for distributing space and aligning items within a container.
Grid (CSS Grid Layout) is designed for two-dimensional layouts, allowing you to control both rows and columns. It is useful for creating complex layouts with precise control over the placement of items.

## How to align 2 divs horizontally?

**Answer**

Put both the divs in a parent div and use display: flex; on that parent div.
Flexbox makes elements horizontal by default when you set the display property of the container to flex. This is because the default value of the flex-direction property is row, which arranges the child elements in a horizontal line.

## How will you ensure responsiveness in your web application?

**Answer**

Responsiveness: The ability of a website or web application to adapt its layout, content, and functionality to different screen sizes, orientations, and devices.
Responsive Frameworks: Use frameworks like Bootstrap or libraries like Material-UI for built-in responsive components.
CSS Media Queries: Apply different styles based on screen size and device characteristics.
Flexbox and CSS Grid: Use modern layout models for flexible and responsive layouts.
Responsive Images: Provide different image sizes for different screen resolutions.
Viewport Meta Tag: Ensure correct rendering on different devices.
Test Responsiveness: Use developer tools and online services to test responsiveness.
Responsive Units: Use relative units like percentages, em, rem, and viewport units.
Mobile-First Design: Design for mobile devices first and enhance for larger screens.

## What is Material UI?

**Answer**

Material-UI (MUI): A React component library that implements Google's Material Design guidelines, providing pre-built, customizable, and accessible UI components.
Installation: Install the core package and optional icons package using npm or yarn.
Usage: Import and use Material-UI components in your React application, and customize the theme to match your branding.
Components: Offers a wide range of components such as buttons, cards, dialogs, menus, and more, all built with responsive design and accessibility in mind.

## What are CSS precompilers?

**Answer**

CSS Precompilers: Tools that extend the capabilities of standard CSS by adding features such as variables, nesting, mixins, functions, and more.
Common Precompilers:
Sass: Offers SCSS and Sass syntax, with features like variables, nesting, mixins, functions, inheritance, partials, and imports.
LESS: Similar to CSS with additional features like variables, nesting, mixins, functions, and imports.
Stylus: Flexible syntax with features like variables, nesting, mixins, functions, and imports.
Key Features:
Variables: Store values for reuse.
Nesting: Nest CSS selectors for better readability.
Mixins: Create reusable chunks of CSS.
Functions: Create custom functions that return values.
Partials and Imports: Split CSS into multiple files and import them.
Inheritance: Share CSS properties between selectors.

## What is SCSS?

**Answer**

SCSS (Sassy CSS): A syntax of Sass that extends the capabilities of standard CSS by adding features such as variables, nesting, mixins, functions, and more.
Key Features:
Variables: Store values for reuse.
Nesting: Nest CSS selectors for better readability.
Mixins: Create reusable chunks of CSS.
Functions: Create custom functions that return values.
Partials and Imports: Split CSS into multiple files and import them.
Inheritance: Share CSS properties between selectors.
Operators: Perform mathematical operations directly in stylesheets.

## How do you write common CSS in SCSS?

**Answer**

Variables: Store values for reuse.
Mixins: Create reusable chunks of CSS.
Partials and Imports: Split CSS into multiple files and import them.
Nesting: Nest CSS selectors for better readability.
Inheritance: Share CSS properties between selectors.

## What are mixins and plugins?

**Answer**

Mixins:
Definition: Reusable chunks of CSS code that can include properties and accept parameters.
Use Case: Avoid code duplication, enhance maintainability, and centralize common styles.
Plugins:
Definition: Extensions or add-ons that provide additional functionality to a software application, such as a CSS preprocessor or build tool.
Use Case: Extend functionality, automate tasks, and customize behavior.
Example (PostCSS with Autoprefixer and CSSNano):

## What is Bootstrap?

**Answer**

Bootstrap: A popular open-source front-end framework for developing responsive and mobile-first websites.
Key Features:
Responsive Grid System: Create responsive layouts with a flexible grid system.
Pre-styled Components: Use a wide range of pre-styled components like buttons, forms, navbars, and modals.
JavaScript Plugins: Add interactivity with JavaScript plugins like modals, tooltips, and carousels.
Customization: Override default styles or generate a custom build.
Cross-browser Compatibility: Works seamlessly across modern browsers and devices.
Documentation and Community: Extensive documentation and a large community for support.

## How can you optimize CSS files?

**Answer**

Minification:
Remove Unnecessary Characters: Use minification tools (e.g., CSSNano, UglifyCSS) to remove whitespace, comments, and other unnecessary characters from CSS files, reducing their size.
Combine CSS Files:
Reduce HTTP Requests: Combine multiple CSS files into a single file to reduce the number of HTTP requests, which can improve load times.
Remove Unused CSS:
Clean Up Styles: Use tools like PurifyCSS, UnCSS, or the Coverage tab in Chrome DevTools to identify and remove unused CSS rules, reducing the file size.
Use CSS Preprocessors:
Leverage Preprocessors: Use CSS preprocessors like Sass or Less to write more maintainable and modular CSS. Preprocessors can help you organize your styles and reduce redundancy.
Optimize CSS Delivery:
Inline Critical CSS: Inline the critical CSS required for above-the-fold content directly into the HTML to reduce render-blocking and improve perceived load times.
Load CSS Asynchronously: Use the media attribute or JavaScript to load non-critical CSS asynchronously, preventing it from blocking the rendering of the page.
Use Shorthand Properties:
Simplify Code: Use shorthand properties (e.g., margin, padding, border) to reduce the amount of CSS code and improve readability.
Leverage Browser Caching:
Set Cache Headers: Configure your server to set appropriate cache headers for CSS files, allowing browsers to cache them and reduce the need to re-download them on subsequent visits.
Use Modern CSS Features:
CSS Variables: Use CSS variables to reduce redundancy and improve maintainability.
Flexbox and Grid: Use modern layout techniques like Flexbox and CSS Grid to simplify complex layouts and reduce the need for additional CSS.
Optimize Selectors:
Efficient Selectors: Use efficient CSS selectors to minimize the impact on rendering performance. Avoid overly complex or deeply nested selectors.
Gzip Compression:
Enable Compression: Enable Gzip or Brotli compression on your server to reduce the size of CSS files sent to the browser.
