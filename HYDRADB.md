# HydraDB integration

A trajectory *is* a graph whose nodes carry embeddings — exactly HydraDB's model
(graph + vector + memory in one substrate). HELIX uses **both** of HydraDB's
retrieval paths, for two different jobs.

## Why your dashboard showed "no token usage" (and why that's correct)
HydraDB has two ingestion/retrieval modes:

| path | what it does | HydraDB LLM work | token usage |
|---|---|---|---|
| **Raw embeddings (BYOE)** `embeddings.insert/search` | we compute vectors ourselves (OpenAI) and store/query raw vectors | **none** | **0** (by design) |
| **Managed graph** `upload.knowledge` + `recall.full_recall` | HydraDB extracts entities/relations into a knowledge graph and does graph-aware retrieval | **yes** (its own LLM) | **yes** |

We originally wired only the **BYOE** path (fast, cheap, perfect for per-decision
recall in the agent loop). It works — verified below — but because *we* supply the
vectors, HydraDB does no LLM work, so it generates **zero token usage**. That was the
"no usage" you saw: efficiency, not absence.

We then added the **managed graph** path, which is HydraDB's real differentiator and
*does* show token usage.

## Dual integration in HELIX
1. **BYOE vectors — `HydraVectorStore` (`helix/memory/hydra_store.py`)**
   Every trajectory's task/step records are inserted with `embeddings.insert(upsert=True)`
   and recalled with `embeddings.search(...)` before each task and each recovery. The
   **compact trajectory graph (nodes+edges) is stored in the record metadata**, so the
   graph itself lives in HydraDB. Tenant `helix` (embeddings tenant, dim 1536),
   sub-tenant = collection name.
2. **Managed knowledge graph — `ingest_knowledge` + `graph_recall`**
   Every indexed trajectory is also pushed through `upload.knowledge` (tenant `helix_kg`),
   where HydraDB's LLM extracts entities (apps, APIs, error types) and relations into a
   **queryable trajectory knowledge graph**. `recall.full_recall(graph_context=True)` then
   answers questions like *"how were similar tasks solved and what errors occurred"*.
   This path generates the token usage.

## Verification (live, with the test key)
- **BYOE persisted the benchmark**: searching the `final` collection returns the real
  benchmark records (`82e2fac_1:task`, `:step:a4`, …) with correct scores + metadata —
  this is what produced the **91.2% knowledge-reuse rate** on dev.
- **Managed graph populated**: 87 trajectories ingested via `upload.knowledge`
  (`success_count=87`); `graph_recall(...)` returns real trajectory chunks with their
  solved approaches. → token usage now appears on the HydraDB dashboard.

Reproduce: `scripts/hydra_verify.py` (deep check, both paths) and
`scripts/hydra_ingest_graph.py` (bulk-ingest all trajectories into the graph).

## Activate / configure
```powershell
uv pip install --python .venv\Scripts\python.exe hydra-db-python
$env:HYDRADB_API_KEY="sk_live_..."     # token auth, no URL needed
# optional:
$env:HYDRADB_COLLECTION="final"        # BYOE sub-tenant (fresh name = clean campaign)
$env:HYDRADB_KG="1"                     # managed graph ingestion on (default)
$env:HYDRADB_KG_TENANT="helix_kg"
```
With no key, HELIX falls back to a local numpy vector store, so it always runs.
