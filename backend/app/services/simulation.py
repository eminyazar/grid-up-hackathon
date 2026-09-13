import random
from app.models.sensor import PanelSensorState

class SimulationService:
    def __init__(self):
         self.panels = {
             "PANO-1600-A": PanelSensorState("PANO-1600-A"),
             "PANO-1600-B": PanelSensorState("PANO-1600-B")
         }

    def get_latest_data(self):
        """Tüm panolar için anlık veri kümesini döndürür."""
        results = []
        for panel_id, panel in self.panels.items():
             # %15 ihtimalle anomali senaryosu çalıştır
             if random.random() < 0.15:
                 panel.generate_anomaly_state()
             else:
                 panel.generate_normal_state()
             
             results.append(panel.to_dict())
        return results