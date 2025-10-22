from fastapi import APIRouter
router=APIRouter()
@router.get('/status')
def status(): return {'module':'jupiter','ok':True}
@router.post('/circuits/layout')
def circuits(area_m2: float, lighting_w_m2: float=12.0): return {'lighting_W': area_m2*lighting_w_m2}
