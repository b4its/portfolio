import openai
import os
openai.organization = "org-fMwpbP5OlyTkoVg0qaUGYJrg"
openai.api_key = os.getenv("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")
openai.Model.list()