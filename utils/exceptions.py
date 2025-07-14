# Custom exception classes

class DataIngestionError(Exception):
    """Exception raised for errors in the data ingestion process."""
    pass

class ModelTrainingError(Exception):
    """Exception raised for errors during model training."""
    pass
