from fastapi import APIRouter
router=APIRouter()
@router.get('/status')
def status(): return {'module':'hermes','ok':True}
@router.post('/osm/import')
def osm(lat: float, lon: float, radius_m: int=200): return {'lat':lat,'lon':lon,'radius_m':radius_m,'note':'OSM placeholder'}
