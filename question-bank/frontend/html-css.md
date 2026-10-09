# HTML and CSS

Semantic HTML, layout, styling, browser behavior, accessibility, and responsive design.

[Back to the question-bank index](../README.md)

## What is the difference between block-level and inline elements in HTML?

**Answer**

In normal flow, a block box starts on a new line and usually expands to the available inline width.
Examples include `<div>`, `<p>`, headings, and semantic sectioning elements.

An inline box participates in a line of text and normally occupies only the space its content needs.
Examples include `<span>`, `<a>`, `<strong>`, and `<code>`. Width and height do not size a
non-replaced inline box in the same way they size a block box, and vertical margins do not move
surrounding lines apart.

These are default CSS display behaviors, not permanent properties of an HTML tag. CSS can change an
element to `block`, `inline`, `inline-block`, `flex`, or another display type. Some replaced inline
elements, such as images, also have intrinsic dimensions and different sizing behavior.

## What is z-index?

**Answer**

`z-index` controls an element's stack level within its **stacking context**. A high value inside one
stacking context cannot escape that context and appear above an element in a higher parent context.

It applies to positioned elements and also to flex and grid items. Many properties can create a new
stacking context, including positioned elements with a non-`auto` `z-index`, `opacity` below `1`,
certain transforms, and `isolation: isolate`. When `z-index` seems ineffective, inspect the ancestor
stacking contexts instead of continually increasing the number.

## What is the difference between display: none and visibility: hidden?

**Answer**

- `display: none` prevents the element from generating boxes, so it occupies no layout space.
- `visibility: hidden` keeps the element's box in layout but does not paint it.

Both normally remove the hidden content from keyboard interaction and the accessibility tree, though
assistive-technology behavior should be tested for the target browser combination. If content should
be visually hidden but remain available to screen readers, use a tested visually-hidden CSS pattern
instead of either property.

## How do you display an image without using the `<img>` tag?

**Answer**

Use a CSS background image when the image is decorative:

```css
.hero {
  min-height: 20rem;
  background: center / cover no-repeat url("hero.webp");
}
```

A CSS background has no native alternative-text semantics. If the image conveys content, use
`<img alt="...">` or `<picture>` instead so it remains accessible and participates in responsive
image loading.

## What is the use of flex and grid in CSS?

**Answer**

Flexbox is primarily one-dimensional: it lays items out along a row or column and distributes or
aligns space along those axes. It is well suited to navigation bars, toolbars, and component-level
alignment.

Grid is two-dimensional: it defines rows and columns and places items within that structure. It is
well suited to page layouts and components whose row and column alignment must coordinate. They can
be nested and used together.

## How do you align two elements horizontally?

**Answer**

Place them in a flex container. The default `flex-direction` is `row`:

```css
.row {
  display: flex;
  align-items: center;
  gap: 1rem;
}
```

Use `justify-content` for alignment along the row and `align-items` for the cross axis. Grid may be a
better fit when the elements must align with a larger column structure.

## How will you ensure responsiveness in your web application?

**Answer**

- Include a viewport meta tag and start with a usable narrow-screen layout.
- Prefer intrinsic layouts with Flexbox, Grid, `min()`, `max()`, `clamp()`, and relative units rather
  than fixed device widths.
- Add media or container queries where the content actually needs a layout change.
- Use responsive images with `srcset`, `sizes`, or `<picture>` and reserve image dimensions to limit
  layout shift.
- Preserve readable line lengths, touch-target sizes, keyboard access, zoom, and reduced-motion
  preferences.
- Test real content at narrow, wide, zoomed, landscape, and high-density configurations rather than
  checking only a few named devices.

## What is Material UI?

**Answer**

MUI is a React component library whose default design system follows Material Design. It provides
components, theming, styling utilities, and optional icon packages.

Using a component library improves consistency and can provide useful accessibility behavior, but it
does not make an application automatically accessible. Teams must still use correct labels and
semantics, manage focus, choose sufficient contrast, and test keyboard and assistive-technology
behavior after customization.

## What are CSS precompilers?

**Answer**

CSS preprocessors compile an extended stylesheet language into CSS. Sass, Less, and Stylus provide
features such as variables, mixins, functions, modules, and programmatic transformations.

Modern CSS now supports custom properties, nesting, and other features that once required a
preprocessor, but preprocessors remain useful for build-time computation and reusable abstractions.
Keep nesting shallow and avoid generating selectors or output that are difficult to inspect.

## What is SCSS?

**Answer**

SCSS is the CSS-compatible syntax of Sass. Sass compiles SCSS variables, mixins, functions, modules,
and control constructs into ordinary CSS. SCSS uses braces and semicolons, unlike Sass's indented
syntax.

Prefer the Sass module system (`@use` and `@forward`) over legacy `@import`, and use native CSS
custom properties when a value must change at runtime.

## How do you write common CSS in SCSS?

**Answer**

Extract repeated declarations into a mixin, pass the varying values as parameters, and organize
shared code into modules:

```scss
@mixin focus-ring($color) {
  outline: 0.2rem solid $color;
  outline-offset: 0.2rem;
}

.button:focus-visible {
  @include focus-ring(#2457d6);
}
```

Use placeholders and `@extend` carefully because they can generate coupled selectors. Reuse should
improve the compiled CSS and its maintenance, not merely reduce the number of source lines.

## What are mixins and plugins?

**Answer**

A **mixin** is a source-language abstraction, such as a Sass block that emits declarations wherever
it is included and may accept parameters.

A **plugin** extends a tool's processing pipeline. For example, PostCSS plugins can add vendor
prefixes, transform newer syntax for selected browser targets, or minify the generated CSS. A mixin
is invoked by stylesheet source; a plugin transforms the stylesheet as part of the build.

## What is Bootstrap?

**Answer**

Bootstrap is a frontend toolkit that provides a responsive grid, utility classes, styled components,
and JavaScript behavior for components such as modals and dropdowns. Its Sass variables and build
can be customized.

It can accelerate consistent UI development, but teams should avoid shipping unused components,
understand its generated markup and JavaScript, and verify accessibility after customization.

## How can you optimize CSS files?

**Answer**

Measure before optimizing, then address the largest costs:

- remove unused rules carefully, including classes generated dynamically at runtime;
- minify production output and serve it with Brotli or gzip compression;
- use content-hashed filenames with long-lived cache headers;
- avoid large frameworks or icon sets when only a small portion is used;
- split styles by route or component when it improves first-load cost without causing excessive
  requests or flashes of unstyled content;
- consider small, measured critical CSS for render-blocking paths; and
- inspect coverage, transfer size, render timing, and real-user performance after the change.

Combining every stylesheet is not universally faster under modern HTTP, and selector micro-
optimization is rarely the first priority. Preserve cascade order and test visual regressions when
changing bundling or removing CSS.

## References

- [MDN: normal flow](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Introduction)
- [MDN: stacking context](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_positioned_layout/Stacking_context)
- [MDN: responsive images](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Responsive_images)
- [Sass documentation](https://sass-lang.com/documentation/)
