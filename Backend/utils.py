def format_source_display(source):
    """Format source URL for display."""
    source_parts = source.split('/')
    if len(source_parts) > 2:
        return f"https://.../{source_parts[-1]}"
    return source


def get_formatted_response(generated_response):
    """Format the response with sources."""
    sources = set(doc.metadata["source"]
                  for doc in generated_response["source_documents"])
    response_text = generated_response['result']

    sources_container = "\n\nSources:\n"
    for i, source in enumerate(sorted(sources)):
        display_text = format_source_display(source)
        sources_container += f"{i+1}. {display_text}\n"
    return f"{response_text}\n{sources_container}"
