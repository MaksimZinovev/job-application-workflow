# Why every wiki write says "Auto-fixed 1 issue(s)"

Context: when an agent writes .md files into the wiki during a
run, each write comes back with "Auto-fixed 1 issue(s)
(markdownlint:1)" and a warning to re-read the file. Run 14 hit
it on every write: 5 step_0 checks, 9 step_1 checks, scoring.md.

```shell
 write -> markdownlint --fix (pi-autoformat extension)
   |                    |
 no final            ends with
 newline             newline
   |                    |
   v                    v
 byte added on disk   clean write,
 "Auto-fixed 1"       no noise
```

Q: Where does it come from?
A: Global pi extension @gotgenes/pi-autoformat, listed in
   ~/.pi/agent/settings.json. Every project gets it.
Q: What makes it fire?
A: Every write or edit. "Exactly 1 issue, every file" is the
   MD047 signature: no newline at end of file.
Q: Turn it off?
A: No. It guards a real bug: editing from memory after the disk
   copy changed. End files with a newline and it goes silent.
Lesson: fix the writer, not the guard.
