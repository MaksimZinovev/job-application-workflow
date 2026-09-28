# Completeness rubric

Score the sweep: were all occurrences of the pattern found and
handled? One coverage score per pattern row. This is separate from
how well each fix was written (that is the quality rubric).

| Level | What it means |
|-------|---------------|
| none | No sweep was made; only the obvious occurrences were handled |
| partial | Some occurrences found, known areas left unchecked |
| most | Full sweep made; one or two possible occurrences left unjustified |
| all | Every occurrence was found and either fixed or justified with a quote; greppable triggers at zero remaining |

Scoring notes:

- A row can be coverage all and quality poor (everything found,
  badly fixed), or quality excellent and coverage partial (one
  perfect fix, occurrences missed). Both scores must meet the
  rule's minimums to close the row.
- To claim all, say how you swept: every paragraph, every heading,
  every list item, or the trigger list if the rule has one. The
  checker recounts greppable triggers against your claim.
- A greppable trigger cannot be justified away. Fix it, or the
  coverage cannot be all. Justifying with a quote applies to
  occurrences no trigger list can find.
- An honest partial with a stated plan beats a false all.