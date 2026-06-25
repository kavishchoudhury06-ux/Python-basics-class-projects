def remove_duplicate_values(original_dict):
    unique_dict = {}
    seen_values = set() # Sets offer O(1) lookup time to track duplicates
    for key, value in original_dict.items():
        # Check if the value has already been added
        if value not in seen_values:
            unique_dict[key] = value
            seen_values.add(value) # Mark the value as seen
    return unique_dict
# Example Usage
sample_data = {
"item1": "apple",
"item2": "banana",
"item3": "apple", # Duplicate value
"item4": "orange",
"item5": "banana", # Duplicate value
}

# Run the function
cleaned_dict = remove_duplicate_values(sample_data)
# Display the results
print("Original Dictionary:", sample_data)
print("Cleaned Dictionary: ", cleaned_dict)

