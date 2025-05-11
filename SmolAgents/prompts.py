from typing import Dict, List, Any
from dataclasses import dataclass
from datetime import datetime
from pydantic import BaseModel


class PromptTemplates(BaseModel):
    task: str

    class DataScientist:
        @classmethod
        def detailed_report(cls, task):
            return f"""
            You're an expert analyst. You make comprehensive reports after visiting many websites.
            Don't hesitate to search for many queries at once in a for loop.
            For each data point that you find, visit the source url to confirm numbers.
            {task}
            """












    def get_detailed_report(self):
        return self.DataScientist.detailed_report(self.task)
