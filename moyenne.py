def moyenne(notes):
    return sum(notes)/len(notes)

def note_max(notes):
    return max(notes)

notes=[12,15,9,18]
print("Moyenne:",moyenne(notes))
print("note maximale:",note_max(notes))
