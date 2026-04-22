from promptflow import tool

# The inputs to this function are mapped in the Prompt Flow UI
@tool
def extract_logic(previous_node_output: str, node_metadata: dict = None):
    """
    This function processes the output received from a preceding node.
    """
    
    try:
        # If the previous node returned a string of code or text
        extracted_content = previous_node_output
        
        # Logic to manipulate or 'extract' specific parts
        # Example: Cleaning whitespace or formatting
        processed_code = extracted_content.strip()
        
        return {
            "status": "success",
            "extracted_code": processed_code,
            "length": len(processed_code)
        }
        
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }
