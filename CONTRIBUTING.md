# Contributing

## Add A Question

Add the question to the most specific existing topic. Create a new file only when the subject is
large enough to have several questions and has no suitable owner.

Use this format:

```markdown
## What problem does this concept solve?

**Answer**

Give the direct answer first. Then explain the mechanism, trade-offs, and one short example when
they materially improve understanding.

**Further reading**

- [Official documentation](https://example.com)
```

Use fenced code blocks with a language identifier:

````markdown
```java
var result = service.findById(id);
```
````

## Quality Checklist

- Search the topic and neighboring topics before adding a question.
- Merge equivalent questions; keep distinct questions when their constraints or expected depth
  differ.
- Answer the question directly before listing details.
- Correct grammar without changing the technical meaning.
- Verify version-sensitive claims against current official documentation.
- State scope explicitly, such as Java version, framework generation, database dialect, or delivery
  guarantee.
- Explain important limits. For example, Kafka ordering is per partition, not global.
- Prefer examples that compile or queries that identify their SQL dialect.
- Do not include employer names, candidate names, private project details, salaries, email addresses,
  tokens, internal URLs, or confidential interview material.

## Behavioral Answers

Behavioral entries should provide a framework or generic sample, not a fabricated personal story.
Use placeholders such as `[role]`, `[situation]`, and `[result]` where candidates must supply their
own facts. Structure experience questions with STAR:

1. **Situation:** enough context to understand the problem;
2. **Task:** the candidate's responsibility;
3. **Action:** the specific decisions and actions taken;
4. **Result:** measurable outcome and lesson.

## Sources

Add official references when an answer is version-sensitive, security-sensitive, or easy to
misstate. A source supports the answer but does not replace it. Avoid copying large passages from
documentation.

Before submitting a change, run:

```bash
python3 scripts/validate.py
```
