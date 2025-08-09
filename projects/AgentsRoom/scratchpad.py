class Scratchpad:
    """
    Scratchpad class formatted according to Appendix B of the paper.
    
    Purpose:
    - Stores multiple pieces of text content as a list of (label, content) entries.
    - Outputs the entire content as a structured and formatted text block following
      a fixed order and formatting specification, including labeled sections.
    """

    def __init__(self):
        self.entries = []  # List to hold entries, each as a tuple (label, content)

    def add(self, label: str, content: str):
        """
        Add a new labeled content entry to the scratchpad.
        
        Parameters:
            label (str): The label/category for the content, e.g. "CONFLICT".
            content (str): The textual content associated with the label.
        
        Process:
            Strips leading and trailing whitespace from the content, then appends
            the (label, cleaned content) tuple to the entries list.
        """
        clean_content = content.strip()
        self.entries.append((label, clean_content))

    def format(self) -> str:
        """
        Format and output all stored entries according to Appendix B specification.
        
        Output format example:
            [Creative Writing Task]
            Corresponding text content

            [Central Conflict]
            Corresponding text content
            ...
        
        Details:
        - Outputs entries grouped and ordered by a fixed label order.
        - Skips labels with no corresponding content.
        - If multiple entries share the same label, all are output in order of addition.
        
        Returns:
            str: The fully formatted multi-section text ready for display or saving.
        """
        label_order = [
            "CREATIVE WRITING TASK",
            "CONFLICT",
            "CHARACTER",
            "SETTING",
            "PLOT",
            "EXPOSITION",
            "RISING_ACTION",
            "CLIMAX",
            "FALLING_ACTION",
            "RESOLUTION"
        ]
        parts = []
        for lbl in label_order:
            for entry_label, entry_content in self.entries:
                # Case-insensitive comparison to match entries to the current label
                if entry_label.upper() == lbl:
                    pretty_label = self._label_to_pretty(lbl)
                    # Format with label in square brackets followed by content on new line
                    parts.append(f"[{pretty_label}]\n{entry_content}")
        # Join all labeled sections with double newlines for clarity
        return "\n\n".join(parts)

    def _label_to_pretty(self, label: str) -> str:
        """
        Convert internal label strings into more human-readable, 'pretty' titles
        as used in the paper.
        
        Example:
            "CONFLICT" -> "Central Conflict"
        
        Parameters:
            label (str): Internal label string
        
        Returns:
            str: Pretty printed label title
        """
        mapping = {
            "CREATIVE WRITING TASK": "Creative Writing Task",
            "CONFLICT": "Central Conflict",
            "CHARACTER": "Character Descriptions",
            "SETTING": "Setting",
            "PLOT": "Key Plot Points",
            "EXPOSITION": "Exposition",
            "RISING_ACTION": "Rising Action",
            "CLIMAX": "Climax",
            "FALLING_ACTION": "Falling Action",
            "RESOLUTION": "Resolution"
        }
        # Default to title case if label is not found in mapping
        return mapping.get(label, label.title())

    def __str__(self):
        """
        Override the string conversion to output the formatted text.
        
        Returns:
            str: The formatted scratchpad content (same as format()).
        """
        return self.format()
