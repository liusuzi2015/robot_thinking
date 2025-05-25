from mem0 import Memory

import os

config = {
    "embedder": {
        "provider": "openai",
        "config": {"model": "text-embedding-3-large", "embedding_dims": 1536},
    },
    "graph_store": {
        "provider": "memgraph",
        "config": {
            "url": "bolt://localhost:7687",
            "username": "memgraph",
            "password": "mem0graph",
        },
    },
}

