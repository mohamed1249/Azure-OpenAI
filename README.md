# Azure-OpenAI
This project demonstrates how to leverage Azure OpenAI for document processing tasks, including summarization, tagging, and classification.

**Key functionalities:**

* Extracts text content from PDF pages with a maximum token limit to avoid exceeding API constraints.
* Connects to Azure OpenAI using an API key and endpoint details.
* Constructs chat messages to interact with the Large Language Model (LLM) for different purposes:
    * Summarization: Provides a concise overview of the document's content.
    * Tagging: Generates a list of relevant keywords or labels associated with the document.
    * Classification: Assigns a single category label to the document (e.g., legal document).

**Benefits:**

* Automates document processing tasks, saving time and effort.
* Integrates with Azure OpenAI for access to powerful LLM capabilities.
* Provides a foundation for further development and customization of document processing workflows.

**Future work:**

* Refine prompts for the LLM to improve the clarity and focus of the output (e.g., directly generate tags instead of summarizing first).
* Explore additional functionalities like information extraction or sentiment analysis.
* Integrate the notebook into a larger application for real-world document processing scenarios.

**Target audience:**

* Data scientists interested in exploring Azure OpenAI for document processing.
* Developers looking to automate document analysis tasks.
* Anyone interested in leveraging AI for document understanding.
