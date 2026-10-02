# 1111. Maximum Nesting Depth of Two Valid Parentheses Strings

**Difficulty:** Medium

## Problem

A string is a valid parentheses string (VPS) if and only if it consists of `"("` and `")"` characters only, and:

- It is the empty string.
- It can be written as `AB` (`A` concatenated with `B`), where `A` and `B` are VPSs.
- It can be written as `(A)`, where `A` is a VPS.

We define the nesting depth of a VPS `S` as follows:

- `depth("") = 0`
- `depth(A + B) = max(depth(A), depth(B))`
- `depth("(" + A + ")") = 1 + depth(A)`

For example:

```text
""          → depth = 0
"()"        → depth = 1
"()()"      → depth = 1
"()(())"    → depth = 2
