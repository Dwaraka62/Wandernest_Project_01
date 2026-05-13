#!/usr/bin/env python3
"""
WSGI wrapper that ensures promptflow LLM tools are imported before app initialization.
This solves the EmptyLLMApiMapping issue by populating the connection_type_to_api_mapping
before Prompt Flow tries to resolve LLM nodes.
"""

# Critical: Import LLM tools before any Prompt Flow app initialization
try:
    import promptflow.tools.llm
    print("[wsgi_wrapper] Successfully imported promptflow.tools.llm")
except Exception as e:
    print(f"[wsgi_wrapper] WARNING: Failed to import promptflow.tools.llm: {e}")

# Now import and create the app
from promptflow.core._serving.app import create_app

# Create WSGI app
application = create_app(engine='flask')
