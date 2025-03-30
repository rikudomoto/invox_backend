from dataclasses import dataclass


@dataclass
class AiAnalysisLogData:
    id: str = None
    image_path: str = None
    success: str = None
    message: str = None
    class_label: str = None
    confidence: str = None
    request_timestamp: str = None
    response_timestamp: str = None
