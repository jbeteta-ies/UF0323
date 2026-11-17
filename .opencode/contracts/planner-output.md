# Planner Output Contract

The Planner must return a concise but directly executable implementation specification.

Do not include long source excerpts or raw research unless necessary to explain a blocker.

## Required structure

### STATUS

One of:

- `READY`
- `NEEDS_CLARIFICATION`
- `BLOCKED`

### ISSUE

- Issue number/title.
- One-sentence objective.

### SOURCES CONSULTED

List only the files or authoritative sources actually used.

For each source, state its purpose in a short phrase.

### SCOPE

State what the implementation will change.

### FILES

For every file expected to be created or modified:

- path;
- action: `CREATE`, `MODIFY`, or `DELETE`;
- required changes/content.

If the exact path cannot yet be known, explain why.

### READ_SCOPE FOR IMPLEMENTER

List the minimum files Implementer is allowed/expected to read.

Do not use broad repository-wide scope unless justified.

### IMPLEMENTATION SPECIFICATION

Provide ordered implementation steps.

Each step must describe an observable change, not merely an intention.

Resolve important curricular, pedagogical and architectural decisions here rather than leaving them for Implementer.

### REQUIRED CONTENT

List mandatory sections, fields, concepts, tables or other required elements when applicable.

### EXCLUSIONS

Explicitly list work that must not be performed.

### CLOSED DECISIONS

List important decisions already settled by the issue, project rules, sources, or planning process.

Implementer must not reinterpret these decisions.

### ACCEPTANCE CRITERIA

Use a checklist of observable pass/fail conditions.

Every material requirement from the issue must map to at least one acceptance criterion.

### VALIDATION

List commands/checks/reviews required after implementation.

Mark each as:

- `MANDATORY`
- `CONDITIONAL`

For conditional checks, state the trigger.

### RISKS / BLOCKERS

List only unresolved matters that could affect implementation.

If none, write `None`.

### SUPERVISOR SUMMARY

Provide a compact summary for Supervisor containing:

- what will change;
- why;
- key decisions;
- key exclusions;
- any risk requiring attention;
- recommendation: `APPROVE_FOR_HG1`, `REVISE_PLAN`, or `BLOCK`.

The Supervisor should normally be able to review the plan from this section plus the acceptance criteria without re-reading source material.
