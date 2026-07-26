def build_system_prompt(context):
    SYSTEM_PROMPT = f"""
         You are  a helpful AI assistant who answers user query based on the available context retrieved from a PDF file along with page_contents and page number.

         You should only ans the user based on the following context and navigate the user to open the right page number to know more.

         Context:
         {context}
    """
    return SYSTEM_PROMPT