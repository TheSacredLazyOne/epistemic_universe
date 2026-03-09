# Substack Node — Single Post Ingestion Spec

> Version: v0.1 — foundational
> Status: Spec — not yet implemented
> Scope: Single post ingestion, nabla generation, output structure
> Nothing here is final.

---

## Purpose

Ingest a single Substack post and produce a structured Markdown document
containing the original content, its nabla against the receiving node's
frame, engagement signals (likes, comments), and per-comment nabla.

This is the foundational unit. Everything else — full corpus ingestion,
git repo construction, training loops, Mastodon command channel integration
— builds on this unit working correctly.

---

## Input

A single Substack post URL, or a single entry object already parsed from
the RSS feed.

The script must be runnable in two modes:

```
python3 ingest_post.py <post_url>
python3 ingest_post.py --from-feed <substack_url> --offset 0
```

---

## Entry Metadata (Frontmatter)

Every ingested post produces a frontmatter block before the content:

```yaml
---
title: <post title>
date: <YYYY-MM-DD>
url: <canonical post URL>
type: post | note | podcast
access: full | truncated
like_count: <integer or null>
comment_count: <integer or null>
ingested: <ISO timestamp of ingestion>
node: <substack publication name>
---
```

**type** — determined by feed entry tags or content length heuristics:
- `post` — standard long-form entry
- `note` — short entry, typically under 300 words, no heading structure
- `podcast` — entry contains an enclosure with audio MIME type

**access** — determined at ingestion time:
- `full` — content length exceeds 500 words and does not end with a
  subscription CTA pattern
- `truncated` — content is short, ends with paywall pattern, or
  `<content:encoded>` is visibly a teaser

Truncated posts are ingested with what is available. The access field
names the gap. Nothing is silently absent.

**Paywall detection heuristic:**
```python
PAYWALL_PATTERNS = [
    "Subscribe to continue reading",
    "This post is for paid subscribers",
    "Subscribe to read the full post",
]
# If any pattern present in content, access = truncated
```

---

## Content Structure

### Post content

Full HTML converted to Markdown via `html2text`. Images are not
downloaded — image tags are converted to links back to the Substack
CDN URL. This keeps the document portable without local asset storage.

Heading levels in the original post are incremented by +1 so the
document structure is subordinate to the output document's own headings.
An `##` in the original becomes `###` in the output.

### Podcast handling

If `type: podcast`, the enclosure URL is extracted. Audio is fetched
and transcribed via MLX Whisper (local). Transcript is stored as the
post content. Original audio URL is preserved in frontmatter:

```yaml
audio_url: <mp3 url>
transcript_model: mlx-whisper-tiny | small | base
```

Transcription is optional at runtime via `--no-transcribe` flag. If
skipped, content is `[transcript not generated — audio at audio_url]`.

---

## Output Document Structure

The output is a single Markdown file per post, structured for clean
rendering in Obsidian (collapsible at heading level).

```markdown
---
[frontmatter block]
---

# Original Post

## [Post Title]

[post content — headings incremented +1]

---

# Nabla

[nabla output — see Nabla section below]

---

# Engagement

**Likes:** [like_count or —]

## Comments

### [comment_id]: [commenter_name] — [date]

[comment content]

#### Nabla

[comment nabla output]

---

### [comment_id]: [commenter_name] — [date]

[comment content]

#### Nabla

[comment nabla output]
```

---

## Nabla Generation

The nabla is the gradient between the receiving node's frame and the
incoming post. It is not a summary. It is a differential — where the
post aligns with the frame, where it introduces strain, where it names
something the frame has not yet named.

### Thought seed (prepended to model prompt)

```
You are computing a nabla — the gradient between an existing frame and
an incoming document.

The frame defines the receiving node's current positions and vocabulary.
The incoming document is effluence from an external node.

Your output has three parts only:

ALIGNMENT: Where the incoming document and the frame are saying the same
thing, possibly in different vocabulary. Be specific. Name the propositions
and the passages.

STRAIN: Where the incoming document and the frame are in tension. Not
contradiction necessarily — misfit. Where contact produces resistance.
Name what is being pressed on.

UNPREDICTED: What the incoming document contains that the frame has no
address for yet. Not wrong — just outside current vocabulary. These are
candidate nutrients.

Be concise. No preamble. No conclusion. Three sections only.
```

### Model

Local MLX model. Recommended starting point: **Phi-3 Mini (3.8B)**

Rationale: The nabla task is structured output generation against a
known schema, not deep reasoning. Phi-3 Mini produces reliable
structured output at low latency. Sufficient for alignment/strain/
unpredicted classification. Can be upgraded if the output quality
proves insufficient.

### Context construction

```
[thought seed]

--- FRAME ---
[frame content — propositions only, not proposals or library]

--- INCOMING ---
[post content]

--- END ---

Generate the nabla now.
```

Frame is injected once per session. Post content is injected per post.
Comment nabla reuses the same session with the comment as the incoming
document — cheaper than re-injecting the frame for each comment.

### Comment nabla

Same thought seed, same frame. Incoming document is the comment text.
Comment nabla is scoped — it measures the comment against the frame,
not against the post. The post is not re-injected. This keeps cost low
and keeps the gradient clean.

---

## Engagement Data

Substack's RSS feed does not include like counts or comment content.
These require the Substack API or web scraping.

**v0.1 scope:** Like count and comment content are fetched via the
Substack public API endpoint:

```
GET https://<publication>.substack.com/api/v1/posts/<post_slug>
```

This endpoint is publicly accessible for non-paywalled publications
without authentication. It returns like count and top-level comment
threads.

If the endpoint returns 403 or 404, engagement fields are set to `null`
and flagged in frontmatter:

```yaml
engagement_access: full | unavailable
```

Nothing is silently absent.

---

## Training Frequency

Training on ingested content should follow constraint contact, not a
schedule.

The appropriate trigger for a training run is the accumulation of
sufficient nabla divergence — enough unpredicted content has arrived
that the model's current weights are producing stale gradients. A
schedule-based approach (weekly, monthly) will train on noise as often
as signal.

Proposed mechanism: a divergence counter incremented with each ingested
post. When unpredicted content in the nabla output exceeds a threshold
across N posts, a training run is indicated. The threshold is a custody
decision — set by the custodian based on how fast the node's frame is
evolving.

Starting heuristic: **train after 20 posts with non-empty UNPREDICTED
sections.** Review after first run. The number is not the point — the
principle is that training is triggered by accumulated genuine novelty,
not elapsed time.

For the Mastodon command channel integration: the command channel posts
a training trigger when the divergence counter crosses threshold. The
custodian reviews the pending nabla set, confirms, and the training run
executes. The custodian does not need to count manually — the counter
is maintained in the repo as a file that increments with each ingestion.

---

## File Naming Convention

```
YYYY-MM-DD_<slug>.md
```

Where `<slug>` is the post URL slug, lowercased, hyphens preserved,
non-alphanumeric characters stripped.

Example:
```
2025-10-02_beyond-books-building-infrastructure-for-understanding.md
```

---

## Mastodon Command Channel Integration (not v0.1 — named for lineage)

The command channel posts a single Mastodon toot to the I-Language
instance:

```
@observer ingest <post_url>
```

The listener receives the membrane event, passes to the interpreter,
which calls `ingest_post.py` with the URL. The output file is committed
to the repo. The observer posts a confirmation toot back to the custodian:

```
ingested: 2025-10-02_beyond-books.md
nabla: 2 alignment / 1 strain / 3 unpredicted
```

The custodian reviews the output file before any training trigger is
confirmed. The crossing is bidirectional. The record is permanent.

Each action arrives one at a time. The custodian reviews before the
next is confirmed. This is not a pipeline — it is a tethered sequence.

---

## Dependencies

```
feedparser
html2text
requests
mlx
mlx-lm          # for Phi-3 Mini inference
mlx-whisper     # for podcast transcription (optional)
gitpython       # for repo commit operations
PyYAML          # for frontmatter generation
```

---

## Open Questions (v0.1 scope — not blocking)

- Comment threading depth: Substack supports threaded replies. v0.1
  ingests top-level comments only. Nested replies deferred.
- Image handling: currently linked back to CDN. If CDN links rot, local
  asset storage will be needed. Deferred.
- Authentication: paywalled content requires Substack login. Deferred —
  work with what the public feed provides, name the gaps honestly.
- Nabla aggregation: how individual post nablas roll up to a corpus-level
  gradient. Deferred until single post is working.

---

*Nothing here is final.*
*Upstream of: ingest_post.py, setup_mlx.sh, cleanup_mlx.sh, nabla_generate.py*
*Downstream of: substack_node (proposal), skill_node.md, command_channel.md*
*Custodian: The Sacred Lazy One*
