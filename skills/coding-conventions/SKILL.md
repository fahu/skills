---
name: coding-conventions
description: Apply coding conventions when writing, editing, or reviewing code. Require multiline if statements with explicit block bodies, including guard clauses and early returns.
---

# Coding Conventions

## Multiline if statements

Never write an `if` statement with its body on the same line, even when the
body contains only one statement or is enclosed in braces. This includes
guard clauses, early returns, and `else if` branches.

In languages that use braces, always enclose the body in braces, put the body
on separate indented lines, and put the closing brace on a separate line.
In other languages, use the language's normal block syntax with the body on
separate lines. Follow the surrounding code's indentation style.

Do not write:

```javascript
if (!session) return null;
```

Write:

```javascript
if (!session) {
    return null;
}
```
