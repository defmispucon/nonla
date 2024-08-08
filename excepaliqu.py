# Example nested list of collaborators
tags = [
    ["Leader", "Collaborator1", "Collaborator2"],
    ["Leader2", "CollaboratorA", "CollaboratorB", "CollaboratorC"]
]

# Calculate the number of collaborators for the first group, excluding the leader
collaborators_no = len(tags[0]) - 1

print(f"Number of collaborators (excluding the leader) in the first group: {collaborators_no}")
