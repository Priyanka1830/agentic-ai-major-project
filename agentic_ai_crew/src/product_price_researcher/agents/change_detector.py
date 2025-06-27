from crewai import Agent

class ChangeDetector(Agent):
    def compare(self, old_data, new_data):
        # For now, just return new if it's different from old
        changes = []
        for new in new_data:
            if not old_data or new not in old_data:
                changes.append(new)
        return changes
