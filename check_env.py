import os
import sys

print("GEMINI_API_KEY in env:", "GEMINI_API_KEY" in os.environ)
for k, v in os.environ.items():
    if "GEMINI" in k or "API" in k or "GOOGLE" in k:
        print(f"  {k}: {v[:5]}... (length: {len(v)})")

try:
    from google import genai
    print("google-genai is installed.")
except ImportError:
    print("google-genai is NOT installed.")

try:
    import google.generativeai as legacy_genai
    print("google-generativeai is installed.")
except ImportError:
    print("google-generativeai is NOT installed.")
