# CI/CD and Deployment

Continuous integration, delivery, deployment strategies, and Jenkins scheduling.

[Back to the question-bank index](../README.md)

## What are CI and CD, and which deployment strategies are common?

**Answer**

**Continuous integration** frequently integrates small changes and validates them with automated
builds, tests, and quality checks. **Continuous delivery** keeps validated changes releasable but may
retain a manual production decision. **Continuous deployment** automatically releases every change
that passes the required controls.

Common rollout techniques include:

- **rolling:** replace instances in batches;
- **blue-green:** prepare a parallel environment and switch traffic;
- **canary:** expose a new version to a small, measured traffic segment first;
- **feature flags:** separate code deployment from feature exposure; and
- **immutable replacement:** create new runtime units instead of modifying existing ones.

A/B testing is primarily an experimentation technique, not a safety-oriented deployment strategy.
The right rollout depends on capacity, state, database compatibility, traffic control, observability,
and rollback requirements.

## How would you upgrade an application without user-visible downtime?

**Answer**

Run old and new versions concurrently behind a load balancer and use a rolling, blue-green, or canary
rollout. The new version must pass readiness checks before receiving traffic, and terminating
instances must stop new work and drain existing requests.

Use expand-and-contract database migrations so both versions can operate during the transition.
Keep APIs and messages backward compatible, externalize session state where required, pre-warm
critical paths, monitor service-level indicators, and automate a rollback or traffic shift.

"Zero downtime" is an end-to-end property. A deployment mechanism alone cannot guarantee it if a
schema change, dependency, long-running job, or stateful connection is incompatible.

## How does a Jenkins cron expression schedule a Pipeline?

**Answer**

Jenkins uses five fields:

```text
MINUTE HOUR DAY-OF-MONTH MONTH DAY-OF-WEEK
```

In a Declarative Pipeline, `triggers { cron('H 2 * * 1-5') }` runs once around 02:00 on weekdays.
`H` is a stable hash derived from the job name and spreads jobs across a range to avoid a load spike;
it is not a new random value on every run.

Use `cron` when the schedule should trigger the build. Use `pollSCM` when Jenkins should check for
source changes and trigger only when changes exist.

## References

- [Jenkins Pipeline syntax and cron](https://www.jenkins.io/doc/book/pipeline/syntax/)
