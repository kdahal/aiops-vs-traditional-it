# Assume rca_model.py has a function called 'identify_probable_cause'
# and a dependency on mock incident data.

import pytest
# NOTE: Adjust the import path based on your final project structure
from src.rca_engine.rca_model import identify_probable_cause 

# --- Mock Data ---

# A mock incident representing a correlated failure (output of Alert Management)
MOCK_INCIDENT_A = {
    "incident_id": "INC-001",
    "alerts": [
        {"id": 1, "service": "API-Gateway", "metric": "Latency", "value": "High", "time": 1700000000},
        {"id": 2, "service": "DB-Replica", "metric": "CPU", "value": "100%", "time": 1700000001},
    ],
    "context": {
        "recent_deployments": ["Service-X v1.2.0"],
        "recent_config_changes": [],
        "time_of_day": "Peak",
    }
}

# A mock incident representing a different failure type (e.g., config error)
MOCK_INCIDENT_B = {
    "incident_id": "INC-002",
    "alerts": [
        {"id": 3, "service": "Auth-Service", "metric": "ErrorRate", "value": "500s", "time": 1700000100},
    ],
    "context": {
        "recent_deployments": [],
        "recent_config_changes": ["Auth-DB-Connection-String"],
        "time_of_day": "Off-Peak",
    }
}

# --- Test Functions ---

def test_rca_engine_detects_deployment_cause():
    """
    Tests if the RCA model correctly identifies a recent deployment 
    as the highest probable cause for Incident A (High CPU/Latency).
    """
    # Simulate the RCA engine output based on the provided context
    cause, confidence = identify_probable_cause(MOCK_INCIDENT_A)
    
    # Assert that the identified cause is related to the recent deployment
    assert "deployment" in cause.lower()
    assert "service-x" in cause
    # Assert confidence is high enough (e.g., > 0.8)
    assert confidence > 0.85

def test_rca_engine_detects_config_cause():
    """
    Tests if the RCA model correctly identifies a recent configuration change 
    as the highest probable cause for Incident B (500 errors).
    """
    cause, confidence = identify_probable_cause(MOCK_INCIDENT_B)
    
    # Assert that the identified cause is related to configuration
    assert "config" in cause.lower()
    assert "connection-string" in cause
    assert confidence > 0.90 # Configuration errors are often highly correlated

def test_rca_engine_handles_no_clear_cause():
    """
    Tests the scenario where no single clear cause is found (e.g., model is unsure).
    The system should return a generic cause and low confidence.
    """
    # Create an incident with confusing/incomplete context
    confused_incident = MOCK_INCIDENT_A.copy()
    confused_incident["context"] = {"recent_deployments": [], "recent_config_changes": []}
    
    cause, confidence = identify_probable_cause(confused_incident)
    
    # Assert it returns a fallback statement and low confidence
    assert "unknown" in cause.lower()
    assert confidence < 0.50