import random
import time
from app.core.config import settings

class PanelSensorState:
    def __init__(self, panel_id: str):
        self.panel_id = panel_id
        self.timestamp = time.time()
        self.temperature_celsius = 0.0
        self.humidity_percent = 0.0
        self.current_amps = 0.0
        self.partial_discharge_db = 0.0
        self.status = "normal"
        self.anomaly_type = None

    def generate_normal_state(self):
        """Normal çalışma koşulları için veri üretir."""
        self.current_amps = round(random.uniform(settings.NORMAL_CURRENT_MIN, settings.NORMAL_CURRENT_MAX), 2)
        # Akım ve sıcaklık arasında basit bir korelasyon simülasyonu
        base_temp = random.uniform(settings.NORMAL_TEMP_MIN, 40.0)
        temp_increase_due_to_current = (self.current_amps / settings.NORMAL_CURRENT_MAX) * 15.0
        
        self.temperature_celsius = round(base_temp + temp_increase_due_to_current, 2)
        self.humidity_percent = round(random.uniform(settings.NORMAL_HUMIDITY_MIN, settings.NORMAL_HUMIDITY_MAX), 2)
        self.partial_discharge_db = round(random.uniform(0.0, 10.0), 2)
        self.status = "normal"
        self.anomaly_type = None
        self.timestamp = time.time()

    def generate_anomaly_state(self):
        """Anormal (riskli) çalışma koşullarından birini rastgele üretir."""
        anomaly_scenarios = ["high_temp", "overcurrent", "partial_discharge"]
        self.anomaly_type = random.choice(anomaly_scenarios)

        if self.anomaly_type == "high_temp":
            self.temperature_celsius = round(random.uniform(settings.CRITICAL_TEMP, 105.0), 2)
            self.current_amps = round(random.uniform(settings.NORMAL_CURRENT_MAX, settings.CRITICAL_CURRENT - 200), 2)
            self.partial_discharge_db = round(random.uniform(10.0, 25.0), 2)
        
        elif self.anomaly_type == "overcurrent":
            self.current_amps = round(random.uniform(settings.CRITICAL_CURRENT, 2800.0), 2)
            self.temperature_celsius = round(random.uniform(70.0, settings.CRITICAL_TEMP), 2)
            self.partial_discharge_db = round(random.uniform(10.0, 20.0), 2)
        
        elif self.anomaly_type == "partial_discharge":
             self.partial_discharge_db = round(random.uniform(settings.PD_THRESHOLD, 60.0), 2)
             self.current_amps = round(random.uniform(settings.NORMAL_CURRENT_MIN, settings.NORMAL_CURRENT_MAX), 2)
             self.temperature_celsius = round(random.uniform(40.0, 65.0), 2)

        self.humidity_percent = round(random.uniform(settings.NORMAL_HUMIDITY_MIN, settings.NORMAL_HUMIDITY_MAX), 2)
        self.status = "anormal"
        self.timestamp = time.time()
        
    def to_dict(self):
        return {
            "panel_id": self.panel_id,
            "timestamp": self.timestamp,
            "temperature_celsius": self.temperature_celsius,
            "humidity_percent": self.humidity_percent,
            "current_amps": self.current_amps,
            "partial_discharge_db": self.partial_discharge_db,
            "status": self.status,
            "anomaly_type": self.anomaly_type
        }