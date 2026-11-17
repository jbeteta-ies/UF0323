# GitHub Issue Context Contract

GitHub Manager must use this contract when supplying a private GitHub issue to
Supervisor and Planner.

The goal is to provide complete issue context without requiring Planner to
access GitHub directly.

## Required structure

### ISSUE

- Number
- Title
- State
- URL
- Milestone
- Labels

### BODY

Include the complete issue body.

Do not paraphrase acceptance criteria, deliverables, exclusions or workflow
requirements.

### COMMENTS

Include comments in chronological order.

For each comment provide:

- author;
- timestamp when available;
- complete text when it contains requirements, decisions, corrections or
  acceptance information.

Purely administrative comments may be summarized.

### DECISIONS FROM COMMENTS

List only explicit decisions already made in comments that materially affect
planning or implementation.

Do not infer new decisions.

If none, write `None`.

### OPEN QUESTIONS / BLOCKERS

List unresolved issue-level questions visible in the issue or comments.

If none, write `None`.

### RETRIEVAL STATUS

One of:

- `COMPLETE`
- `INCOMPLETE`
- `FAILED`

If not `COMPLETE`, explain exactly what could not be retrieved.

## Rules

- Use authenticated `gh` for private repositories.
- Do not use unauthenticated web fetching as a substitute.
- Do not omit comments that change scope or acceptance criteria.
- Do not transform the issue into a plan; planning belongs to Planner.
- Keep the packet complete but avoid unrelated repository information.
