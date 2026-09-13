from fastapi import APIRouter
from app.services.simulation import SimulationService

router = APIRouter()
sim_service = SimulationService()

@router.get("/sensor-data", summary="Anlık pano sensör verilerini döndürür.")
async def get_sensor_data():
    """
    Simüle edilmiş pano verilerini döndürür. 
    Bu veri SCADA/Monitoring ekranında tüketilecektir.
    """
    return {"data": sim_service.get_latest_data()}