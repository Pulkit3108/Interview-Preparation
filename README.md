# Interview Preparation Question Bank

A structured, growing collection of software-engineering interview questions, concise answers,
coding prompts, and behavioral preparation guidance.

The material is organized by subject instead of by interview or company, so one canonical answer
can be improved over time without maintaining repeated copies.

## Start Here

- [Browse the complete question bank](question-bank/README.md)
- [Learn how to add or improve questions](CONTRIBUTING.md)
- Start with [behavioral interviews](question-bank/behavioral/behavioral-interviews.md),
  [Java](question-bank/languages/java.md),
  [Spring and Spring Boot](question-bank/backend/spring.md), or
  [system design](question-bank/architecture/system-design.md).

## Coverage

| Area | Topics |
| --- | --- |
| Behavioral | Recruiter conversations, self-introduction, career decisions, teamwork, and STAR stories |
| Languages | Java, JavaScript, C#, and C++ fundamentals plus coding exercises |
| Data structures | Core structures, algorithms, complexity, and implementation exercises |
| Frontend | HTML/CSS, Angular, legacy AngularJS, React, and web analytics |
| Backend | Spring Boot, Spring Data/JPA, REST, Node.js, and .NET |
| Data | SQL, NoSQL, database internals, and data-processing systems |
| Architecture | Low-level design, system design, microservices, resilience, and scalability |
| Infrastructure | Cloud, containers, Kubernetes, Kafka, networking, CI/CD, and observability |
| Developer tools | Git, command-line utilities, Maven, and Gradle |
| Testing | Test design, Java mocking, Selenium, and browser automation |

## How To Use It

1. Pick a topic from the [question-bank index](question-bank/README.md).
2. Answer each question aloud before expanding on the written answer.
3. Add a concrete example, trade-off, or failure mode where appropriate.
4. For behavioral prompts, replace placeholders with truthful examples from your own experience.
5. Recheck version-sensitive framework and platform behavior against the linked official source.

## Content Principles

- Keep one canonical entry for the same concept within a topic.
- Prefer short, interview-ready explanations over encyclopedic notes.
- Separate facts from recommendations and explicitly state important trade-offs.
- Use generic placeholders instead of names, employers, compensation figures, or other personal data.
- Mark version-sensitive behavior and prefer official documentation as the source.
- Preserve runnable code in fenced blocks with the correct language identifier.

This repository is a study aid, not a substitute for testing code or consulting current official
documentation for production decisions.

## Validation

Run the dependency-free repository check after changing content or navigation:

```bash
python3 scripts/validate.py
```
