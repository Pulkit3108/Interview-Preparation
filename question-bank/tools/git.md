# Git and Version Control

Version-control models, history integration, synchronization, and branching strategy.

[Back to the question-bank index](../README.md)

## What is the difference between centralized and distributed version control?

**Answer**

A centralized version-control system has one authoritative server repository, and clients commonly
depend on that server for history operations. Subversion is a typical example.

In a distributed version-control system such as Git, each clone normally contains the repository's
history. Developers can inspect history, create commits, and manage branches locally, then exchange
commits with remotes. A hosting server can still be organizationally authoritative, but it is not the
only copy of the repository data.

## What is the difference between merge, rebase, and squash in Git?

**Answer**

- **Merge** combines histories and, when a fast-forward is not possible, can create a merge commit
  with multiple parents. Existing commits keep their identities.
- **Rebase** copies a sequence of commits onto a new base, producing new commit IDs. It can create a
  linear history but should not be used casually on published commits that others depend on.
- **Squash** combines the changes represented by several commits into fewer commits. Interactive
  rebase can squash local commits; some hosting platforms can also squash while merging a pull
  request.

These operations can produce a similar final file tree while preserving different history. Choose
based on the team's collaboration and audit requirements, not appearance alone.

## What is the difference between `git fetch` and `git pull`?

**Answer**

`git fetch` downloads refs and objects and updates remote-tracking refs without integrating them into
the current branch. It lets you inspect incoming history first.

`git pull` fetches and then integrates the selected upstream into the current branch. Depending on
options and configuration, integration may use merge, rebase, or fast-forward-only behavior. For
predictable automation, state the intended mode explicitly, such as `git pull --ff-only`.

## What is a branching strategy?

**Answer**

A branching strategy defines how a team isolates work, integrates changes, releases software, and
applies urgent fixes. Common models include:

- **trunk-based development:** small, frequent integrations into one primary branch, often protected
  by feature flags and automated checks;
- **GitHub Flow:** short-lived branches merged into a deployable primary branch through review; and
- **Git Flow:** additional long-lived development and release branches, which can suit scheduled
  releases but adds integration overhead.

The appropriate choice depends on release cadence, deployment automation, support obligations, and
team size. Regardless of model, protect important branches, require relevant checks, keep branches
short-lived where practical, and document how hotfixes return to every maintained line.

## References

- [Git fetch](https://git-scm.com/docs/git-fetch)
- [Git pull](https://git-scm.com/docs/git-pull)
- [Git merge](https://git-scm.com/docs/git-merge)
- [Git rebase](https://git-scm.com/docs/git-rebase)
